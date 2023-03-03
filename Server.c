#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main()
{
    system("clear");

    // Create a socket
    int server_socket = socket(AF_INET, SOCK_STREAM, 0);

    // Bind the socket to an IP address and port
    struct sockaddr_in server_address;
    memset(&server_address, 0, sizeof(server_address));
    server_address.sin_family = AF_INET;
    server_address.sin_addr.s_addr = inet_addr("192.168.1.38");
    server_address.sin_port = htons(4444);

    if (bind(server_socket, (struct sockaddr*) &server_address, sizeof(server_address)) < 0) {
        printf("Error: Failed to bind socket.\n");
        exit(1);
    }

    // Listen for incoming connections
    listen(server_socket, 1);
    printf("Listening for incoming connections...\n");

    // Accept an incoming connection
    int client_socket;
    struct sockaddr_in client_address;
    socklen_t client_address_length = sizeof(client_address);
    client_socket = accept(server_socket, (struct sockaddr*) &client_address, &client_address_length);

    // Receive and send data
    char buffer[1024];
    while (1) {
        memset(buffer, 0, sizeof(buffer));
        recv(client_socket, buffer, sizeof(buffer), 0);
        printf("%s", buffer);

        char input_buffer[1024];
        printf("Enter Your Command: ");
        fgets(input_buffer, sizeof(input_buffer), stdin);
        send(client_socket, input_buffer, strlen(input_buffer), 0);
    }

    // Close the sockets
    close(client_socket);
    close(server_socket);

    return 0;
}

