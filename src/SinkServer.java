import java.io.*;
import java.net.*;

import javax.swing.*;

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
	            
	            boolean modelResult = false;
	            
	            System.out.println("1========"+in.available()); // Returns an estimate of the number of bytes that can be read (orskipped over)
	            
	            System.out.println("3========"+in.readByte()); //See the general contract of the readBytemethod of DataInput. Bytesfor this operation are read from the containedinput stream
	            
	            
	            
	            String localAddress = server.getLocalAddress().toString(); // Gets the local address to which the socket is bound.
	            
	            boolean keepAlive = server.getKeepAlive();// Tests if SO_KEEPALIVE is enabled.
	            int receiveBufferSize = server.getReceiveBufferSize(); // Gets the value of the SO_RCVBUF option for this Socket, that is the buffer size used by the platform for input on this Socket.
	            int sendBufferSize = server.getSendBufferSize(); // Get value of the SO_SNDBUF option for this Socket, that is the buffer size used by the platform for output on this Socket.
	            int typeOfService = server.getTrafficClass(); // Gets traffic class or type-of-service in the IP header for packets sent from this Socket
	            
	            System.out.println(server.getRemoteSocketAddress());

	            
	            //String protocol = protocol(in.readByte());
	            
	            System.out.println(localAddress+" "+keepAlive+" "+receiveBufferSize+" "+sendBufferSize+" "+typeOfService);//+" "+protocol);
	            
	            /*
	            'duration' 'protocol_type'	'service'	'flag'	'src_bytes'	'dst_bytes'	'land'	'wrong_fragment'
	            'urgent'	'hot'	'num_failed_logins'	'logged_in'	'num_compromised'	'root_shell'	'su_attempted'
	            'num_root'	'num_file_creations'	'num_shells'	'num_access_files'	'num_outbound_cmds'
	            'is_host_login'	'is_guest_login'	'count'	'srv_count'	'serror_rate'	'srv_serror_rate'	'rerror_rate'
	            'srv_rerror_rate'	'same_srv_rate'	'diff_srv_rate'	'srv_diff_host_rate'	'dst_host_count'
	            'dst_host_srv_count'	'dst_host_same_srv_rate'	'dst_host_diff_srv_rate'	'dst_host_same_src_port_rate'
	            'dst_host_srv_diff_host_rate'	'dst_host_serror_rate'	'dst_host_srv_serror_rate'	'dst_host_rerror_rate'
	            'dst_host_srv_rerror_rate'	'outcome'	
	            
	            */
	            
	            
	            //modelResult = ModelCall.modelCall();
	            
	            if(modelResult) {
	            	String text = Main.sinkText.getText()+
		            		"------------------------------------------------------------------------------------------"+
		            		"\n                          FROM PORT "+server.getRemoteSocketAddress()+
		            		"\n\n"+in.readUTF()+
		            		"\n------------------------------------------------------------------------------------------\n\n";
		            
		            Main.sinkText.setText(text);
	            }
	            else {
	            	JOptionPane.showMessageDialog(null, "An Intruder detected on "+server.getRemoteSocketAddress());
	            }
	            
	            
	            server.close();
	            
	         } catch (SocketTimeoutException s) {
	            break;
	         } catch (IOException e) {
	            e.printStackTrace();
	            break;
	         }
	      }
	   }
	   private String protocol(byte readByte) {
		   System.out.println("llllllll  "+ readByte);
           if (readByte == (byte) 0x06) {
        	   return "TCP";
           } else if (readByte == (byte) 0x11) {
        	   return "UDP";
           } else if (readByte == (byte) 0x01) {
               return "ICMP";
           } else {
        	   return "Unknown";
           }
	   }
	   
}
