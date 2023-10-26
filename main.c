#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>


#define PORT 8080
void handle_client_request(int client_socket) {
    FILE *html_file;
    char response[1024];

    html_file=fopen("index.html", "r");
    sprintf(response, "HTTP/1.1 200 OK\nContent-Type: text/html\n\n");
    send(client_socket, response, strlen(response), 0);

    while (fgets(response, 1024, html_file)) {
        send(client_socket, response, strlen(response), 0);
    }

    fclose(html_file);
}
int main() {
    int server_socket, client_socket;
    struct sockaddr_in server_addr, client_addr;
    socklen_t client_addr_len = sizeof(client_addr);

    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket < 0) {
        perror("Error in socket creation");
        exit(1);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);
    server_addr.sin_addr.s_addr = INADDR_ANY;

    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Error in binding");
        exit(1);
    }

    if (listen(server_socket, 10) == 0) {
        printf("Server listening on port %d\n", PORT);
    } else {
        perror("Error in listening");
        exit(1);
    }

    while (1) {
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_addr_len);
        if (client_socket < 0) {
            perror("Error in accepting");
            exit(1);
        }

        handle_client_request(client_socket);

        close(client_socket);
    }

    close(server_socket);
    return 0;
}
