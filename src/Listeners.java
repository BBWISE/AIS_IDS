import java.awt.event.*;
import java.util.Arrays;

import javax.swing.JOptionPane;

@SuppressWarnings("serial")
public class Listeners extends Main implements ActionListener {
	
	static Main interfaces = new Main();
	static Task func = new Task();
	
	@SuppressWarnings("unchecked")
	public void actionPerformed (ActionEvent event) {
		
		if(event.getSource()==sinkButt) {
			mainCard.show(switcher, "Sink Page");
		}
		else if(event.getSource()==sendButt) {
			
			String names = func.portNameLoader();
			String Names [] = names.split(";;");
			Arrays.sort(Names);
			
			portList.removeAllItems();
			portList.addItem("Select destination");
			for(int i=0;i<Names.length;i++) {
				
				portList.addItem(Names[i].toString());
				
			}
			mainCard.show(switcher, "Send Page");
		}
		else if(event.getSource()==clear) {
			sinkText.setText("");
		}
		else if(event.getSource()==send) {
			func.sends();
			
			sendText.setText("");
		}
		else if(event.getSource()==newPortButt) {
			if(!newPortText.getText().equals("") && !newPortText.getText().equals(null))
				func.addNewSubject(newPortText.getText());
			else
				JOptionPane.showMessageDialog(null, "Enter a Port number.");
			newPortText.setText("");
		}
		
	}

}
