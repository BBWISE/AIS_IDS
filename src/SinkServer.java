import java.io.*;
import java.net.*;

public class SinkServer extends Thread {
	   public static ServerSocket serverSocket;
	   
	   public SinkServer(int port) throws IOException {
	      serverSocket = new ServerSocket(port);
	      //serverSocket.setSoTimeout(10000);
	   }
	   
	   public void run() {
	      while(true) {
	         try {
	            Socket server = serverSocket.accept();
	            
	            DataInputStream in = new DataInputStream(server.getInputStream());
	            
	            String text = Main.sinkText.getText()+
	            		"------------------------------------------------------------------------------------------"+
	            		"\n                          FROM PORT "+server.getRemoteSocketAddress()+
	            		"\n\n"+in.readUTF()+
	            		"\n------------------------------------------------------------------------------------------\n\n";
	            
	            Main.sinkText.setText(text);
	            
	            server.close();
	            
	         } catch (SocketTimeoutException s) {
	            break;
	         } catch (IOException e) {
	            e.printStackTrace();
	            break;
	         }
	      }
	   }
}
