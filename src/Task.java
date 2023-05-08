import java.io.*;
import java.net.Socket;
import java.util.*;

import javax.swing.*;

public class Task {
	
	private void portNameSaver(String[] names) {
		String Names = "";
		for(int i=0;i<names.length;i++) {
			if(i==(names.length-1))
				Names += names[i];
			else
				Names += names[i]+";;";
		}
		try {
			FileWriter myWriter = new FileWriter("ports.txt");
			myWriter.write(Names);
			myWriter.close();
			JOptionPane.showMessageDialog(null, "Saved successfully.");
		} catch (IOException e) {
			JOptionPane.showMessageDialog(null, e);
			e.printStackTrace();
		}
	}
	public void addNewSubject(String subjectName) {
		String names = portNameLoader()+";;"+subjectName;
		String Names [] = names.split(";;");
		Arrays.sort(Names);
		
		portNameSaver(Names);
		
	}
	public String portNameLoader() {
		String names="";
		
		File reader;
		try
		{
			reader = new File("ports.txt");
			Scanner myReader = new Scanner(reader);
		      while (myReader.hasNextLine()) {
		    	  names=myReader.nextLine();
		      }
		     myReader.close();
		}catch(
		IOException e)
		{
			e.printStackTrace();
		}
		
		return names;
	}
	public void sinkImplementation(int port) {
	      try {
	         Thread t = new SinkServer(port);
	         t.start();
	      } catch (IOException e) {
	         e.printStackTrace();
	      }
	}
	public void sends() {
		String serverName = "localhost";
	     int port = Integer.parseInt(Main.portList.getSelectedItem().toString());
	     try {
	         //System.out.println("Connecting to " + serverName + " on port " + port);
	         Socket client = new Socket(serverName, port);
	         
	         //System.out.println("Just connected to " + client.getRemoteSocketAddress());
	         OutputStream outToServer = client.getOutputStream();
	         DataOutputStream out = new DataOutputStream(outToServer);
	         
	         //out.writeUTF("Hello from " + client.getLocalSocketAddress());
	         out.writeUTF(Main.sendText.getText());
	         //InputStream inFromServer = client.getInputStream();
	         //DataInputStream in = new DataInputStream(inFromServer);
	         
	         JOptionPane.showMessageDialog(null, "Sent successfully.");
	         client.close();
	     } catch (IOException e) {
	    	 JOptionPane.showMessageDialog(null, e);
	         e.printStackTrace();
	     }
	
	}
}
