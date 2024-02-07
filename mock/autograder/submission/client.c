#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <unistd.h>

#define DEFAULT_PORT 27993
#define MAGIC_STR "cs230"

void solve_question(char* question, char* answer){
    char command[256];
    snprintf(command, sizeof(command), "python3 QA.py \'%s\'", question);
    printf("Command= %s\n", command);
    FILE *fp = popen(command, "r");
    if (fp == NULL) {
        printf("Failed to run command\n" );
        exit(0);
    }
    fgets(answer, 256, fp);
    pclose(fp);
}

    /*These are some instructions*/
    /*With the secret key*/
    /*CS230-Spring-2022*/

int main(int argc, char **argv)
{
        int socket_c;
        int status;
        char *flag = (char *)malloc(70);
        char *ret_str = (char *)malloc(200);
        int port = DEFAULT_PORT;
        int max = 0; // max number of correct answers (for testing)
        char *sid = "richards@cs.umass.edu";
        char *message = (char *)malloc(256);
        char host[256];

        strcpy(host, "127.0.0.1");

        if (argc > 1)
        {
                sid = argv[1];
        }
        if (argc > 2)
        {
                port = atoi(argv[2]);
        }
        if (argc > 3)
        {
                strcpy(host, argv[3]);
        }
        if (argc > 4){
            max = atoi(argv[4]);
        }

        if ((socket_c = socket(AF_INET, SOCK_STREAM, 0)) < 0)
        {
                printf("[*] ERROR IN CREATING SOCKET!\n");
                close(socket_c);
                exit(-1);
        }

        struct sockaddr_in client_address;

        client_address.sin_family = AF_INET;
        client_address.sin_port = htons(port);
        inet_pton(AF_INET, host, &client_address.sin_addr);
        memset(&(client_address.sin_zero), '\0', 8);

        if ((status = connect(socket_c, (struct sockaddr *)&client_address, sizeof(client_address))) < 0)
        {
                printf("[*] ERROR IN CONNECT!\n");
                close(socket_c);
                exit(-1);
        }

        sprintf(message, MAGIC_STR" HELLO %s\n", sid);
        printf("%s", message);
        //printf("message: %s", message);
        status = send(socket_c, message, strlen(message), 0);
        char *recv_mess = (char *)malloc(200);
        int rounds = 0;
        char question[256];
        char answer[256];

        while ((strstr(flag, "BYE")) == NULL)
        {
                memset(recv_mess, '\0', 200);
                status = recv(socket_c, recv_mess, 200, 0);

                if (status < 0)
                {
                        printf("[*] ERROR in recv!\n");
                        exit(1);
                }
                printf("%s", recv_mess);
                sscanf(recv_mess, MAGIC_STR" STATUS %[^\n]\n", question);
                solve_question(question, answer);


                sprintf(ret_str, MAGIC_STR" %s\n", answer);
                status = send(socket_c, ret_str, strlen(ret_str), 0);

                if (status < 0)
                {
                        printf("[*] ERROR in recv!\n");
                        exit(1);
                }

                memset(ret_str, '\0', 200);
                memset(flag, '\0', 70);
                sprintf(flag, "%s", recv_mess);
                ++rounds;
        }
        printf("%s", flag);
        close(socket_c);

        return 0;
}