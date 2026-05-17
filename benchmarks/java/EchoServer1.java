import java.net.*;
import java.io.*;

public class EchoServer1 {
    public void start(int port) {
        try (ServerSocket serverSocket = new ServerSocket(6000)) {
            Socket clientSocket = serverSocket.accept();
            PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true);
            BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
            
            String inputLine;
            while ((inputLine = in.readLine()) != null) {
            if (".".equals(inputLine)) {
                out.println("good bye");
                break;
             }
             out.println(inputLine);
   }
        } catch (IOException e) {
            // TODO Auto-generated catch block
            e.printStackTrace();
        }
}}