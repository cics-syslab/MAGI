#!/usr/bin/env python
"""
This file implements a Server class used in the grading of the final CS230
project. The server waits for a connection (duh, it's a server), and once it
gets a connection, accepts, ensures that the message sent is of the right format
('cs230 HELLO student@umass.edu') and then sends out some number of problems for
the client to solve. Upon receiving the answer from the client (and verifying
that the answer is correct) the server either sends another question or, if all
N questions have been sent and answered, generates and sends a unique hash for
the student to submit.

This can either be imported from an external script or invoked via command line:

    $ python server.py

There are a number of options that can be set. Here are some of the highlights:

    usage: server.py [-h] [-p PORT] [-M MAGIC_STRING] [-v VERBOSITY] [-r ROUNDS]
                     [-T TIMEOUT] [--production] [--grading] [-D DIRECTORY]
                     [--points-for-hello POINTS_FOR_HELLO]
                     [--points-for-goodbye POINTS_FOR_GOODBYE]
                     [--points-per-test POINTS_PER_TEST] [--json]
                     [--continue-on-failure]

    optional arguments:
      -h, --help            show this help message and exit
      -p PORT, --port PORT  Port for the server to hang out on
      -M MAGIC_STRING, --magic-string MAGIC_STRING
                            Set magic string
      -v VERBOSITY, --verbosity VERBOSITY
                            How much do you want the server to complain?[0,1,2,3]
      -r ROUNDS, --rounds ROUNDS
                            How many problems to send to students
      -T TIMEOUT, --timeout TIMEOUT
                            number of seconds before timeout
      --production          Set up a production server: this overrides all other
                            options except for --port, --rounds, --directory, and
                            --continue-on-failure. This cannot be used with the
                            --grading option
      --grading             Set up a grading server: this overrides all other
                            options except for --port, --rounds, --directory, and
                            --continue-on-failure. This cannot be used with the
                            --production option
      -D DIRECTORY, --directory DIRECTORY
                            Set directory to write files to. Create it if it does
                            not exist
      --points-for-hello POINTS_FOR_HELLO
                            How many points awarded for connection?
      --points-for-goodbye POINTS_FOR_GOODBYE
                            How many points awarded for completion?
      --points-per-test POINTS_PER_TEST
                            Number of points awarded for each test completed
      --json                create results.json in CWD
      --continue-on-failure
                            If true the Server will continue sending tests after a
                            Client has failed a test

A sample session might look like:

    $ python server.py --port 12345 --rounds 300 --json -v 1 --timeout 3.1415 --points_per_test 5

These options do the following

    * Listens on port 12345
    * Has the client solve 300 randomly generated math problems
    * Stores the clients progress in results.json
    * Prints light output to stdout
    * Times out after pi seconds
    * allots 5 points for each test successfully completed

For convenience, a production server can be spun up with

    $ python server.py --production

and a grading server can be spun up with

    $ python server.py --grading

These are just presets and their behavior can be found by invoking
`python server.py --help` (or reading above)
"""

import argparse
import json
import select
import socket
import time
from datetime import datetime
from hashlib import sha256
from os import makedirs
from os import path as osp

from . import QA

PORT = 27993
MAGIC_STR = 'cs230'


class Client:
    client_id = 0

    def __init__(self, secure, rounds=300, create_json=False, store_history=False):
        self.id = Client.client_id  # Provide a unique number to each client
        Client.client_id += 1
        self.rounds = rounds

        self.sid = ""
        self.last_active = time.process_time()
        self.secure = secure
        self.score = 0
        self.store_history = store_history
        self.history = []

        self.question = None

        self.json = {
            "output": "",
            "stdout_visibility": "visible",
            "tests": []
        } if create_json else None

        if self.store_history:
            self.history.append("-" * 80)
            self.history.append('START SESSION')
            self.an_historic_event("CREATED CLIENT")

    def solve(self, question: str = ""):

        if question:
            self.question = question
        return QA.solve_question(self.question)

    def set_sid(self, sid):
        self.sid = sid.decode('utf8')
        if self.store_history:
            self.an_historic_event("CLIENT SET SID: {}".format(self.sid))

    def checkpoint(self, score=3, max_score=3, output="Success"):
        """
        Executed when a checkpoint has been reached
        :param score:  The value to increase self.progress by (defaults to 1)
        :param max_score: Maximum score possible at this checkpoint
        :param output: The message to print when creating results.json
        """
        self.score += score
        if self.json:
            self.add_test_to_json(score=score, max_score=max_score, output=output)

        if self.store_history:
            if score < max_score:
                self.an_historic_event("CHECKPOINT REACHED!\n    SCORE: {}/{} POINTS;\n    MESSAGE: {}".format(
                    score, max_score, output))

    def add_test_to_json(self, score, max_score, output="Success"):
        """
        Defaults to giving self.points_per_test out of self.points_per_test if no other values
        are provided.
        :param score:
        :param max_score:
        :param output:
        :return:
        """

        self.json['tests'].append({"score": score, "max_score": max_score, "output": output})

    def write_progress(self, filename=None, directory='.', mode='w'):
        """
        This writes the progress to a file. Note that this should not be used for
        grading with gradescope, and write_json should be used instead
        :param directory:
        :param filename: the filename to write to. If None is provided,
            try to use the students id (self.sid) to generate a file name.
            the SID is expected to be of the form studentname@umass.edu. If this
            is not the case, a RuntimeError is raised
        :param mode: either 'w' for write or 'a' for append. The append option allows
            for multiple iterations of a students history to be tracked, as well as
            using a global file for all students
        :return:
        """
        sid = self.sid
        if not filename:
            if '@' not in sid:
                return
            else:
                filename = sid.split('@')[0] + '.progress'
        with open(osp.join(directory, filename), mode) as f:
            f.write('{}: {}\n'.format(sid, str(self.score)))

    def write_json(self, filename="results.json", directory='.'):
        """
        Write the results of this test to directory/filename
        :param filename: name of json file
        :param directory: directory to write to
        :return:
        """

        # Write progress to json dictionary
        if self.json is not None:
            with open(osp.join(directory, filename), 'w') as f:
                f.write(json.dumps(self.json, indent=2, sort_keys=True))

    def write_history(self, filename=None, directory='.'):
        if self.store_history:
            history = '\n'.join(self.history) + '\nEND SESSION\n' + ('-' * 80) + '\n'
            filename = filename if filename else self.sid.split('@')[0] + '.txt'
            open(osp.join(directory, filename), 'a').write(history)

    def __str__(self):
        return 'Client{}{}'.format(self.id, (':' + self.sid) if self.sid else '')

    def an_historic_event(self, plaque):
        self.history.append("[{}] {}".format(datetime.now().strftime('[%m-%d-%Y %T]'), plaque))


class Server:
    """
    This class spins up a server. This can either be used for production (i.e.,
    students can target it for their code) or for grading (this has an API that
    compatible for autograding)
    """

    def __init__(self, port=None, track_progress=False, magic_string=None, verbosity=0,
                 number_of_problems=300, timeout=30.0, directory='.', create_json=False,
                 points_per_test=3, points_for_hello=50, points_for_goodbye=50, continue_on_failure=True,
                 store_history=False):
        """
        Create a server that optionally tracks progress of students
        :param port: the port number to run this on. If no port provided, default
                     to PORT defined at the top of the file
        :param magic_string: This string is magical. With great power comes great
            responsibility. Use it wisely.
        :param verbosity: 0 for no output, 1 for some output, 2 for more output, 3
            for way more output than you want
        :param number_of_problems: Number of problems to generate for student
        :param points_per_test: Points allotted for each successfully solved problem
        :param points_for_hello: Points allotted for a successful connection
        :param points_for_goodbye: Points allotted for a successful completion
        :param timeout: Number of seconds before timing out
        :param directory: the directory to write results to
        :param create_json: Should we write a 'results.json' file?
        :param continue_on_failure: If a Client fails a test, continue their
            session. Defaults to False, and sessions are terminated when a test
            is failed.
        """
        self.port = port if port is not None else PORT
        self.magic_string = magic_string if magic_string is not None else MAGIC_STR
        self.verbosity = verbosity
        self.clients = {}
        self.sockets = []
        self.number_of_problems = number_of_problems
        self.timeout = timeout
        self.directory = directory
        self.points_per_test = points_per_test
        self.continue_on_failure = continue_on_failure
        self.points_for_hello = points_for_hello
        self.points_for_goodbye = points_for_goodbye
        self.json = create_json
        self.store_history = store_history

        # Create the directory if it doesn't exist

        if not osp.exists(directory):
            try:
                makedirs(directory)
            except OSError as e:
                raise

    def log_header(self):
        """Create the header for a log entry"""
        return datetime.now().strftime('[%m-%d-%Y %T]')

    def debug(self, message):
        """If verbosity is high enough, print a debug message to stdout"""
        if self.verbosity > 2:
            print('\033[1;34m' + '[-] {} {}'.format(self.log_header(), message) + '\033[0m')

    def warning(self, message):
        """If verbosity is high enough, print a warning to stdout"""
        if self.verbosity > 1:
            print('\033[1;33m' + '[!] {} {}'.format(self.log_header(), message) + '\033[0m')

    def error(self, message):
        """Print an error to stdout"""
        print('\033[0;31m' + '[!!!] ERROR: {} {}'.format(self.log_header(), message) + '\033[0m')

    def info(self, message):
        """If verbosity is high enough, print a message to stdout"""
        if self.verbosity > 0:
            print('[+] {} {}'.format(self.log_header(), message))

    def accept(self, listen, secure, waiting):
        clients = self.clients
        sockets = self.sockets
        waiting.remove(listen)
        self.debug('accept')
        try:
            sock, addr = listen.accept()
            self.debug('accepted raddr {}:{}'.format(addr[0], addr[1]))

        except Exception as e:
            self.warning("Caught exception: {}".format(e))
            return

        sockets.append(sock)
        client = Client(secure, rounds=self.number_of_problems, create_json=self.json, store_history=self.store_history)
        clients[sock] = client
        self.info("Created {}".format(client))

    def disconnect(self, sock) -> None:
        sockets = self.sockets
        clients = self.clients
        self.debug('disconnect')
        try:
            sock.close()
        except Exception as e:
            return
        client = clients.pop(sock)
        if self.json:
            client.write_json(filename='results.json', directory=self.directory)

        if self.store_history:
            client.an_historic_event("DISCONNECTING")
            client.write_history()

        self.info('Disconnecting from {}'.format(client))
        sockets.remove(sock)

    def send_status(self, sock, client: Client) -> bool:
        client.question = QA.generate_question()
        client.last_active = time.process_time()

        msg = str.encode('{} STATUS {}\n'.format(self.magic_string, client.question))

        self.debug("Sending message: {}".format(msg))
        try:
            sock.send(msg)
            return True
        except:
            return False

    def send_bye(self, sock, client):
        sid = client.sid.encode('utf8')
        hashed = sha256(sid).digest().hex()
        client.an_historic_event("GENERATED HASH:\n        {}".format(hashed))
        msg = str.encode('{} {} BYE\n'.format(self.magic_string, hashed))
        self.debug("sending bye: {}".format(msg))
        client.checkpoint(score=self.points_for_goodbye, max_score=self.points_for_goodbye,
                          output="Reached end of tests")

        try:
            sock.send(msg)
            return True
        except Exception as e:
            return False

    def handle_hello(self, response, sock, client):
        client.set_sid(response[2])
        client.checkpoint(score=self.points_for_hello, max_score=self.points_for_hello, output="Successfully connected")
        self.debug("Received id {} for client {}".format(client.sid, client))
        self.send_status(sock, client)

    def handle_solution(self, solution, sock, client):
        """
        We have received a solution from the student, so we handle
        it.
        :param solution: string representation of the solution, as received
            from the student
        :param sock:  socket of the student
        :param client: Client instance storing our session with the student
        :return:
        """
        self.debug("Handling solution {}".format(solution))
        try:
            i = solution.decode("utf-8")

        except Exception as e:
            self.debug("Caught exception {}. Disconnecting client {}".format(
                e, self.clients[sock]
            ))
            self.disconnect(sock)
            return

        if i != client.solve():
            self.debug("Client {} failed to solve problem {}".format(
                client, client.question
            ))
            client.rounds -= 1
            client.checkpoint(score=0, max_score=self.points_per_test,
                              output="Test Case: {} ...... FAILED\nExpected: {}\n Actual: {}".format(client.question,
                                                                                                     client.solve(), i))
            self.disconnect(sock)
            if not self.continue_on_failure:
                return

        else:
            self.debug("Client {} solved problem {}".format(
                client, client.question
            ))
            client.rounds -= 1
            client.checkpoint(score=self.points_per_test, max_score=self.points_per_test,
                              output="Test Case: {} ...... SUCCESS".format(client.question))
        if client.rounds == 0:
            self.send_bye(sock, client)
            self.disconnect(sock)

        else:
            self.send_status(sock, client)

    def handle_response(self, response, sock):
        """
        Handle a response from a student
        :param response: list of words responded from student
        :param sock: socket associated with the student
        :return:
        """

        client = self.clients[sock]

        if len(response) < 2 or len(response) > 3:
            self.warning("Ill-formed response '{}', disconnecting".format(response))
            self.disconnect(sock)
            return

        elif response[0] != str.encode(self.magic_string):
            self.warning("Bad magic string '{}', disconnecting".format(response[0]))
            self.disconnect(sock)
            return

        elif len(response) == 3 and response[1] == str.encode('HELLO') and client.question is None:
            self.handle_hello(response, sock, client)

        elif len(response) == 2:
            self.handle_solution(response[1], sock, client)

    def run(self):
        """
        Run the server!
        :return:
        """
        listen = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen.bind(("", self.port))
        listen.listen(1)

        sockets = self.sockets
        sockets.append(listen)
        clients = self.clients

        while True:
            waiting = select.select(sockets, [], [], 1)[0]
            if listen in waiting:
                self.accept(listen, False, waiting)

            for sock in waiting:
                try:
                    msg = sock.recv(1024)

                except Exception as e:
                    self.disconnect(sock)
                    continue

                if len(msg) == 0 or not msg.endswith(b'\n'):
                    self.warning("Found ill-formed message: '{}'".format(msg))
                    self.disconnect(sock)
                else:
                    self.debug("Handling message: {}".format(msg))
                    self.handle_response(msg.split(), sock)

            # garbage collect
            t = time.process_time()
            items = [x for x in clients.items()]
            for sock, client in items:
                if t - client.last_active > self.timeout:
                    self.info("Client timeout: {} > {}".format(t - client.last_active, self.timeout))
                    self.disconnect(sock)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', help='Port for the server to hang out on', type=int, default=PORT)
    parser.add_argument('-M', '--magic-string', help='Set magic string', default=MAGIC_STR)
    parser.add_argument('-v', '--verbosity', help='How much do you want the server to complain?[0,1,2,3]',
                        type=int, default=0)
    parser.add_argument('-r', '--rounds', help='How many problems to send to students', type=int,
                        default=300)
    parser.add_argument('-T', '--timeout', help='number of seconds before timeout', type=float, default=5.0)
    parser.add_argument('--production', action='store_true',
                        help='Set up a production server: this overrides all other options except for --port, --rounds,'
                             ' --directory, and --continue-on-failure. This cannot be used with the --grading option')
    parser.add_argument('--grading', action='store_true',
                        help='Set up a grading server: this overrides all other options except for --port, --rounds, '
                             '--directory, and --continue-on-failure. This cannot be used with the --production option')
    parser.add_argument('-D', '--directory', help='Set directory to write files to. Create it if it does not exist',
                        type=str, default='.')
    parser.add_argument('--points-for-hello', default=50, type=int, help='How many points awarded for connection?')
    parser.add_argument('--points-for-goodbye', default=50, type=int, help='How many points awarded for completion?')
    parser.add_argument('--points-per-test', help='Number of points awarded for each test completed', default=3,
                        type=int)
    parser.add_argument('--json', help="create results.json in CWD", action="store_true")
    parser.add_argument('--store-history', help="store history for each student in file student_id.txt",
                        action="store_true")
    parser.add_argument('--continue-on-failure', help="If true the Server will continue sending tests after a Client"
                                                      " has failed a test", action="store_true")

    args = parser.parse_args()
    if args.production:
        if args.grading:
            raise RuntimeError("Production mode and grading mode are mutually exclusive")

        server = Server(port=args.port, verbosity=args.verbosity, number_of_problems=args.rounds, timeout=60.0,
                        directory=args.directory, points_for_hello=args.points_for_hello,
                        points_for_goodbye=args.points_for_goodbye, points_per_test=3, create_json=False,
                        continue_on_failure=args.continue_on_failure, store_history=True)

    elif args.grading:
        server = Server(port=args.port, verbosity=args.verbosity, number_of_problems=args.rounds, timeout=1.0,
                        directory=args.directory, points_for_hello=args.points_for_hello,
                        points_for_goodbye=args.points_for_goodbye, points_per_test=3, create_json=True,
                        continue_on_failure=args.continue_on_failure, store_history=False)

    else:
        server = Server(port=args.port, magic_string=args.magic_string, verbosity=args.verbosity,
                        number_of_problems=args.rounds, timeout=args.timeout, directory=args.directory,
                        points_for_hello=args.points_for_hello, points_for_goodbye=args.points_for_goodbye,
                        points_per_test=args.points_per_test, create_json=args.json,
                        continue_on_failure=args.continue_on_failure, store_history=args.store_history)
    server.run()
