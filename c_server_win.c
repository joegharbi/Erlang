#include <stdio.h>
#include <winsock2.h>
#include <windows.h>

#pragma comment(lib, "ws2_32.lib")

DWORD WINAPI ClientHandler(void* data) {
    char buffer[1024];
    int recvMsgSize;
    SOCKET clntSocket = (SOCKET)data;

    while ((recvMsgSize = recv(clntSocket, buffer, 1024, 0)) > 0) {
        send(clntSocket, buffer, recvMsgSize, 0);
    }

    // printf("Client disconnected\n");
    closesocket(clntSocket);

    return 0;
}

int main() {
    WSADATA wsaData;
    SOCKET servSock;
    SOCKET clntSock;
    struct sockaddr_in echoServAddr;
    struct sockaddr_in echoClntAddr;
    unsigned short echoServPort = 54321;
    int clntLen;

    if (WSAStartup(MAKEWORD(2, 0), &wsaData) != 0) {
        printf("WSAStartup() failed");
        exit(1);
    }

    servSock = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    memset(&echoServAddr, 0, sizeof(echoServAddr));
    echoServAddr.sin_family = AF_INET;
    echoServAddr.sin_addr.s_addr = htonl(INADDR_ANY);
    echoServAddr.sin_port = htons(echoServPort);

    bind(servSock, (struct sockaddr*)&echoServAddr, sizeof(echoServAddr));
    listen(servSock, 5);

    while (1) {
        clntLen = sizeof(echoClntAddr);
        clntSock = accept(servSock, (struct sockaddr*)&echoClntAddr, &clntLen);
        // printf("Client connected\n");

        DWORD thread;
        CreateThread(NULL, 0, ClientHandler, (void*)clntSock, 0, &thread);
    }

    return 0;
}
