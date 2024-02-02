#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/socket.h>
#include<netinet/in.h>
#include<arpa/inet.h>
#include<unistd.h>
#include <ctype.h>
#include <netdb.h>
#include <strings.h>
#include <sys/types.h>
#include <math.h>


#define MAXLINE 500 /* Max text line length */

int open_clientfd(char *hostname, int port) {
    // The client's socket file descriptor.
    int clientfd;

    // The hostent struct is used to get the IP address of the server
    // using DNS.
    //
    // struct hostent {
    //   char *h_name;        // official domain name of host
    //   char **h_aliases;    // null-terminated array of domain names
    //   int  h_addrtype;     // host address type (AF_INET)
    //   int  h_length;       // length of an address, in bytes
    //   char **h_addr_list;  // null-terminated array of in_addr structs
    // };
    struct hostent* hp;

    {
        // serveraddr is used to record the server information (IP address
        // and port number).
        //
        // struct sockaddr_in {
        //   short            sin_family;   // e.g. AF_INET
        //   unsigned short   sin_port;     // e.g. htons(3490)
        //   struct in_addr   sin_addr;     // see struct in_addr, below
        //   char             sin_zero[8];  // zero this if you want to
        // };
    }
    struct sockaddr_in serveraddr;

    // printf("Client is creating a socket.\n\n");

    // First, we create the socket file descriptor with the given
    // protocol and protocol family.
    if ((clientfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) return -1;

    // Query DNS for the host (server) information.
    if ((hp = gethostbyname(hostname)) == NULL) return -2;

    // The socket API requires that you zero out the bytes!
    bzero((char*)&serveraddr, sizeof(serveraddr));

    // Record the protocol family we are using to connect.
    serveraddr.sin_family = AF_INET;

    // Copy the IP address provided by DNS to our server address
    // structure.
    bcopy((char*)hp->h_addr_list[0], (char*)&serveraddr.sin_addr.s_addr,
        hp->h_length);

    // Convert the port from host byte order to network byte order and
    // store this in the server address structure.
    serveraddr.sin_port = htons(port);

    // printf("Echo Client is trying to connect to %s (%s:%d).\n", hostname,
            // inet_ntoa(serveraddr.sin_addr), port);

    // Establish a connection with the server.
    if (connect(clientfd, (struct sockaddr*)&serveraddr, sizeof(serveraddr)) < 0)
        return -1;

    // printf("Client connected.\n");

    // Return the connected file descriptor.
    return clientfd;
}

// --------------------------------------------------------------------------------------------------------

char* decryption(char* message) {
    // heuristically minimum number of characters in substring is 3
    // Remember strtok changes input inplace so this has to come before
    char *dictionary = (char *)malloc((int) strlen(message)/3);
    char * token = strtok(message, " ");
    token = strtok(NULL, " ");// Remove CS230
    token = strtok(NULL, " ");// Remove STATUS

    int max = 0;
    // split token, determine character and respective index
    while(token != NULL) {
        int len = strlen(token);
        char* k = (char *)malloc(len-2);
        char letter;
        int flag = 0;
        int index = 0;

        // get index and character
        //printf("Len %d, Token %s\n", len, token);
        for(int i=0; i<len; i++) {
          char c = token[i];
          if (c == '\n'){
              break;
          }

          if (c == '-') {
              flag = 1;
              continue;
          }
          if (flag == 1) {
              letter = c;
          }
          else {
              k[index] = c;
              //printf("%c\n", c);
              index++;
          }
        }

        int key = atoi(k);
        //printf("K %s, Key %d\n",k, key);
        if (key > max) {
          max = key;
        }
        //printf("Key %d Letter %c\n", key, letter);
        dictionary[key] = letter;
        token = strtok(NULL, " ");
    }

    int len = max;
    //printf("Max %d\n", max);
    //printf("Dict %s\n", dictionary);
    char *unscramble = (char *)malloc(len);
    int index = 0;
    // printf("Dict %c, %c\n", dictionary[0], dictionary[1]);

    for(int i=0; i<len; i++) {
        unscramble[i] = dictionary[index];
        index++;

        if ((i+1) == len) {
            unscramble[i+1] = '\0';
            i++;
        }
//        else {
//            unscramble[i+1] = ' ';
//            i++;
//        }
    }
    printf("UNSCRAMBLE %s\n", unscramble);
    return unscramble;
}

// --------------------------------------------------------------------------------------------------------

int main(int argc, char** argv) {
    int clientfd;       // The client socket file descriptor.
    int port;           // The port number.
    char* host;         // Variable to store the host/server domain name.
    char buf[MAXLINE];  // A buffer to receive data from the server.
    char* email;        // Variable to store <netID>@umass.edu.

    // Checking the program arguments
    if (argc != 4) {
        fprintf(stderr, "usage: %s <netID@umass.edu> <port> <host>\n", argv[0]);
        exit(0);
    }

    // Assigning host, port and email
    email= argv[1];
    port = atoi(argv[2]);   //27993
    host = argv[3];         //128.119.243.147

    buf[0] = '\0';
    strcat(buf,"cs230 HELLO ");
    strcat(buf, email);
    strcat(buf, "\n");
    char* useless;

    int ns,nr;

    // Open the client socket file descriptor given the host and port:
    clientfd = open_clientfd(host, port);
    printf("Working...\n");
    printf("%s", buf);
    ns = send(clientfd, buf, strlen(buf), 0);
    nr = recv(clientfd, buf, MAXLINE, 0);
    buf[nr] = '\0';
    if (nr < 1) {
        printf("Read error\n");
        exit(0);
    }
    int i=0;
    while(1){
        char* buf_duplicate = (char *)malloc(strlen(buf)+1);
        strcpy(buf_duplicate, buf);

        useless=strtok(buf, " "); //cs230
        useless=strtok(NULL, " "); //STATUS or FLAG
        //printf("STATUS %s", useless);
        if(strcmp(useless, "STATUS")!=0){
            // useless=strtok(NULL, " ");
            printf("Flag captured.\n");
            break;
        }
        char *start_of_message = strchr(buf_duplicate, ' ');
if (start_of_message != NULL) {
    start_of_message = strchr(start_of_message + 1, ' ');
}

// Check if we found two spaces
if (start_of_message == NULL) continue;
    // Move to the character after the second space
    start_of_message++;

    // Now start_of_message points to the third part of the string
    printf("MESSAGE %s\n", start_of_message);

    char command[256];
    snprintf(command, sizeof(command), "python3 QA.py %s", start_of_message);
    printf("Command= %s\n", command);
        FILE *fp = popen(command, "r");
        if (fp == NULL) {
            printf("Failed to run command\n" );
            exit(0);
        }
        char res[256];
        fgets(res, sizeof(res), fp);
        pclose(fp);

//        char* res = decryption(buf_duplicate);

        printf("Result as string= %s\n", res);
        buf[0]='\0';
        strcat(buf, "cs230 ");
        strcat(buf, res);
        strcat(buf, "\n");
        // printf("From client: %s", buf);
        // printf("Buf to send created\n");
        i++;

        ns = send(clientfd, buf, strlen(buf), 0);
        printf("Buf sent %d\n---------------------\n%s", ns, buf);
        nr = recv(clientfd, buf, MAXLINE, 0);
        printf("NEXT MESSAGE NR %d\n", nr);
        buf[nr] = '\0';
    }
    // printf("Flag= %s\n",useless);
    // printf("Number of iterations=%d\n",i);
    // Close the file descriptor:
    close(clientfd);
    exit(0);
}
