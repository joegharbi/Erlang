import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.SocketException;

public class SimpleServer {

    public static void main(String[] args) {
        try {
            try (ServerSocket serverSocket = new ServerSocket(6000)) {
                // System.out.println("Server listening on port 6000...");

                while (true) {
                    Socket clientSocket = serverSocket.accept();
                    // System.out.println("Client connected: " + clientSocket.getInetAddress());

                    // Start a new thread to handle the client
                    new Thread(() -> handleClient(clientSocket)).start();
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

   private static void handleClient(Socket clientSocket) {
    try (
        BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
        PrintWriter writer = new PrintWriter(clientSocket.getOutputStream(), true);
    ) {
        // System.out.println("Thread ID: " + Thread.currentThread().getId());
        // System.out.println("Client Socket: " + clientSocket);
        // System.out.println("Client InetAddress: " + clientSocket.getInetAddress());
        // System.out.println("Client Port: " + clientSocket.getPort());

        // Read the message from the client
        String clientMessage = reader.readLine();
        // System.out.println("Received from client " + clientSocket.getInetAddress() + ": " + clientMessage);

        // Send the message back to the client
        String response = clientMessage;
        writer.println(response);
        // writer.println();
        // System.out.println("Sent to client " + clientSocket.getInetAddress() + ": " + response);

    } catch (SocketException se) {
        // Handle the SocketException (connection reset) gracefully
        // System.out.println("Client connection reset.");
    } catch (IOException e) {
        e.printStackTrace();
    } finally {
        try {
            // Close the connection
            clientSocket.close();
            // System.out.println("Connection closed for client: " + clientSocket.getInetAddress());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
}
