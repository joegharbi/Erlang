// #include <stdio.h>
// #include <winsock2.h>
// #include <process.h>

// #pragma comment(lib, "ws2_32.lib")

// #define PORT 54321
// #define BUFFER_SIZE 1024

// // Function to handle client connections
// void handle_client(void* client_socket) {
//     SOCKET client = *((SOCKET*)client_socket);
//     char buffer[BUFFER_SIZE];
    
//     // Receive data from client
//     recv(client, buffer, BUFFER_SIZE, 0);
//     // printf("Received message from client: %s\n", buffer);
    
//     // Reverse the message
//     // int len = strlen(buffer);
//     // for (int i = 0; i < len / 2; i++) {
//     //     char temp = buffer[i];
//     //     buffer[i] = buffer[len - i - 1];
//     //     buffer[len - i - 1] = temp;
//     // }
    
//     // Send reversed message back to client
//     // printf("Sending message to client %d \n", client);
//     send(client, buffer, BUFFER_SIZE, 0);
    
//     // Close the client socket
//     closesocket(client);
//     free(client_socket);
//     _endthread();
// }

// int main() {
//     WSADATA wsaData;
//     SOCKET server_socket;
//     struct sockaddr_in server_addr, client_addr;

//     // Initialize Winsock
//     if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
//         printf("WSAStartup failed. Error Code: %d\n", WSAGetLastError());
//         return 1;
//     }

//     // Create socket
//     server_socket = socket(AF_INET, SOCK_STREAM, 0);
//     if (server_socket == INVALID_SOCKET) {
//         printf("Socket creation failed. Error Code: %d\n", WSAGetLastError());
//         WSACleanup();
//         return 1;
//     }

//     // Set up the server address structure
//     server_addr.sin_family = AF_INET;
//     server_addr.sin_addr.s_addr = INADDR_ANY;
//     server_addr.sin_port = htons(PORT);

//     // Bind the socket
//     if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
//         printf("Bind failed. Error Code: %d\n", WSAGetLastError());
//         closesocket(server_socket);
//         WSACleanup();
//         return 1;
//     }

//     // Listen for incoming connections
//     if (listen(server_socket, 5) == SOCKET_ERROR) {
//         printf("Listen failed. Error Code: %d\n", WSAGetLastError());
//         closesocket(server_socket);
//         WSACleanup();
//         return 1;
//     }

//     printf("Server listening on port %d\n", PORT);

//     while (1) {
//         // Accept incoming connections
//         int client_addr_len = sizeof(client_addr);
//         SOCKET client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len);
//         if (client_socket == INVALID_SOCKET) {
//             printf("Acceptance failed. Error Code: %d\n", WSAGetLastError());
//             closesocket(server_socket);
//             WSACleanup();
//             return 1;
//         }

//         // Create a new thread to handle the client
//         HANDLE thread_handle;
//         unsigned thread_id;
//         SOCKET* client_ptr = (SOCKET*)malloc(sizeof(SOCKET));
//         *client_ptr = client_socket;
//         thread_handle = (HANDLE)_beginthreadex(NULL, 0, handle_client, (void*)client_ptr, 0, &thread_id);
//         if (thread_handle == NULL) {
//             printf("Thread creation failed.\n");
//             closesocket(client_socket);
//         }
//         else {
//             // Close the thread handle to avoid memory leak
//             CloseHandle(thread_handle);
//         }
//     }

//     // Close the server socket and clean up
//     closesocket(server_socket);
//     WSACleanup();

//     return 0;
// }

#include <stdio.h>
#include <winsock2.h>
#include <process.h>

#pragma comment(lib, "ws2_32.lib")

#define PORT 54321
#define BUFFER_SIZE 1024

// Function to handle client connections
unsigned int handle_client(void* client_socket) {
    SOCKET client = *((SOCKET*)client_socket);
    char buffer[BUFFER_SIZE];
    
    // Receive data from client
    recv(client, buffer, BUFFER_SIZE, 0);
    
    // Send reversed message back to client
    send(client, buffer, BUFFER_SIZE, 0);
    
    // Close the client socket
    closesocket(client);
    free(client_socket);

    return 0;
}

int main() {
    WSADATA wsaData;
    SOCKET server_socket;
    struct sockaddr_in server_addr, client_addr;

    // Initialize Winsock
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0) {
        printf("WSAStartup failed. Error Code: %d\n", WSAGetLastError());
        return 1;
    }

    // Create socket
    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == INVALID_SOCKET) {
        printf("Socket creation failed. Error Code: %d\n", WSAGetLastError());
        WSACleanup();
        return 1;
    }

    // Set up the server address structure
    server_addr.sin_family = AF_INET;
    server_addr.sin_addr.s_addr = INADDR_ANY;
    server_addr.sin_port = htons(PORT);

    // Bind the socket
    if (bind(server_socket, (struct sockaddr*)&server_addr, sizeof(server_addr)) == SOCKET_ERROR) {
        printf("Bind failed. Error Code: %d\n", WSAGetLastError());
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }

    // Listen for incoming connections
    if (listen(server_socket, 5) == SOCKET_ERROR) {
        printf("Listen failed. Error Code: %d\n", WSAGetLastError());
        closesocket(server_socket);
        WSACleanup();
        return 1;
    }

    // printf("Server listening on port %d\n", PORT);

    while (1) {
        // Accept incoming connections
        int client_addr_len = sizeof(client_addr);
        SOCKET client_socket = accept(server_socket, (struct sockaddr*)&client_addr, &client_addr_len);
        if (client_socket == INVALID_SOCKET) {
            printf("Acceptance failed. Error Code: %d\n", WSAGetLastError());
            closesocket(server_socket);
            WSACleanup();
            return 1;
        }

        // Create a new thread to handle the client
        HANDLE thread_handle;
        unsigned thread_id;
        SOCKET* client_ptr = (SOCKET*)malloc(sizeof(SOCKET));
        *client_ptr = client_socket;
        thread_handle = (HANDLE)_beginthreadex(NULL, 0, handle_client, (void*)client_ptr, 0, &thread_id);
        if (thread_handle == NULL) {
            printf("Thread creation failed.\n");
            closesocket(client_socket);
        }
        else {
            // Close the thread handle to avoid memory leak
            CloseHandle(thread_handle);
        }
    }

    // Close the server socket and clean up
    closesocket(server_socket);
    WSACleanup();

    return 0;
}
