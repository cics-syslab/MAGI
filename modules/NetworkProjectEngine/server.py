#!/usr/bin/env python

import socket
import time
from datetime import datetime
from hashlib import sha256

import select

from magi.managers import TestManager
from . import QA


class Client:
    client_id = 0

    def __init__(self, secure, rounds=300, store_history=False, hidden=True):
        self.id = Client.client_id  # Provide a unique number to each client
        Client.client_id += 1
        self.rounds = rounds

        self.sid = ""
        self.last_active = time.process_time()
        self.secure = secure
        self.store_history = store_history
        self.history = []

        self.question = None
        if self.store_history:
            self.history.append("-" * 80)
            self.history.append('START SESSION')
            self.an_historic_event("CREATED CLIENT")
        self.visibility = "after_published" if hidden else "visible"

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
        TestManager.new_test(score=score, max_score=max_score, output=output, visibility=self.visibility)
        if self.store_history:
            if score < max_score:
                self.an_historic_event("CHECKPOINT REACHED!\n    SCORE: {}/{} POINTS;\n    MESSAGE: {}".format(
                    score, max_score, output))

    def write_history(self):
        if self.store_history:
            history = '\n'.join(self.history) + '\nEND SESSION\n' + ('-' * 80) + '\n'
            TestManager.append_output(history)

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

    def __init__(self, port=12240, magic_string="cs230", verbosity=0,
                 number_of_problems=300, timeout=30.0,
                 points_per_test=3, points_for_hello=50, points_for_goodbye=50, continue_on_failure=True,
                 store_history=False, hidden_test=True):
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
        self.port = port
        self.magic_string = magic_string
        self.verbosity = verbosity
        self.clients = {}
        self.sockets = []
        self.number_of_problems = number_of_problems
        self.timeout = timeout
        self.points_per_test = points_per_test
        self.continue_on_failure = continue_on_failure
        self.points_for_hello = points_for_hello
        self.points_for_goodbye = points_for_goodbye
        self.store_history = store_history

        self.terminated = False
        self.hidden = hidden_test

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
        client = Client(secure, rounds=self.number_of_problems, store_history=self.store_history, hidden=self.hidden)
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
            if self.terminated:
                break

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


