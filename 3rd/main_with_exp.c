#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
//필요한 모듈 불러오기

#define PORT 8080
//포트 넘버 정의
void handle_client_request(int client_socket) {//html파일을 핸들링하는 함수
    FILE *html_file;//html 파일을 FILE 형식으로 정의
    char response[1024];//response 를 char 배열로 정의

    html_file=fopen("index.html", "r"); //파일 읽기 전용으로 열기
    sprintf(response, "HTTP/1.1 200 OK\nContent-Type: text/html\n\n");//응답 헤더 문자열로 만들기
    send(client_socket, response, strlen(response), 0);//response를 client_socket 에 넣어서 보내기

    while (fgets(response, 1024, html_file)) {//html_file에 들어간 문자열이 공백이 아닐 때
        send(client_socket, response, strlen(response), 0);//response 한 줄씩 보내기
    }

    fclose(html_file);//파일 닫기
}
int main() {
    int server_socket, client_socket;//socket 정의
    struct sockaddr_in server_addr, client_addr;//sockaddr_in structure 정의
    socklen_t client_addr_len = sizeof(client_addr);//client_addr_len 정의

    server_socket = socket(AF_INET, SOCK_STREAM, 0);//socket 에 AF_INET, SOCK_STREAM 넣기
    if (server_socket < 0) {
        perror("Error in socket creation");//에러 핸들링
        exit(1);
    }

    server_addr.sin_family = AF_INET;
    server_addr.sin_port = htons(PORT);//htons(PORT)를 해주는 이유는 호스트 바이트 순서의 IP 포트 번호를 네트워크 바이트 순서의 IP 포트 번호로 변환해야 하기 때문
    server_addr.sin_addr.s_addr = INADDR_ANY;//아무 input 이나 수용

    if (bind(server_socket, (struct sockaddr *)&server_addr, sizeof(server_addr)) < 0) {
        perror("Error in binding");//에러 핸들링
        exit(1);
    }

    if (listen(server_socket, 10) == 0) {
        printf("Server listening on port %d\n", PORT);
    } else {
        perror("Error in listening");//에러 핸들링
        exit(1);
    }

    while (1) {
        client_socket = accept(server_socket, (struct sockaddr *)&client_addr, &client_addr_len);//accept 시 socket 생성
        if (client_socket < 0) {
            perror("Error in accepting");//에러 핸들링
            exit(1);
        }

        handle_client_request(client_socket);//위의 함수 호출해서 html 출력

        close(client_socket);//socket 닫기
    }

    close(server_socket);//socket 닫기
    return 0;
}
