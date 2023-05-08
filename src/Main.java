import javax.swing.*;
import java.awt.*;

@SuppressWarnings("serial")
public class Main extends JFrame{
	
	public static JButton sinkButt, sendButt, newPortButt;
	public static JButton send, clear;
	
	public static JTextField portText,newPortText;
	public static JTextArea sinkText, sendText;
	
	@SuppressWarnings("rawtypes")
	public static JComboBox portList;
	
	static Listeners listener= new Listeners();
	
	public static CardLayout mainCard = new CardLayout();
	
	public static JPanel switcher = new JPanel(mainCard);
	
	public void gui() {
		JPanel mainPanel = new JPanel(new BorderLayout());
			
			JPanel leftPanel = new JPanel(new GridLayout(20,1));
				leftPanel.setBackground(Color.lightGray);
				
				leftPanel.add(new JLabel(" "));
				leftPanel.add(new JLabel(" "));
				leftPanel.add(new JLabel("  Port:"));
				leftPanel.add(portText = new JTextField("11111",9));
				leftPanel.add(new JLabel(" "));
				leftPanel.add(sinkButt = new JButton("Sink"));
				leftPanel.add(sendButt = new JButton("Send"));
				
					portText.setFont(new Font("Calibril", Font.BOLD, 18));
					sinkButt.setFont(new Font("Calibril", Font.BOLD, 18));
					sendButt.setFont(new Font("Calibril", Font.BOLD, 18));
					
					sendButt.setBackground(Color.gray);
					sinkButt.setBackground(Color.gray);
					
					sendButt.addActionListener(listener);
					sinkButt.addActionListener(listener);
					
					portText.setEditable(false);
					
				
				for(int i=0;i<6;i++) {
					leftPanel.add(new JLabel(" "));
				}
				leftPanel.add(new JLabel("  New Port:"));
				
				JPanel newPort = new JPanel(new FlowLayout(FlowLayout.LEFT));
					newPort.add(newPortText = new JTextField("",7));
					newPort.add(newPortButt = new JButton("Add"));
					
					newPortText.setFont(new Font("Calibril", Font.BOLD, 14));
					newPortButt.setFont(new Font("Calibril", Font.BOLD, 11));
					
					newPortButt.setBackground(Color.gray);
					
					newPortButt.addActionListener(listener);
				leftPanel.add(newPort);
				for(int i=0;i<5;i++) {
					leftPanel.add(new JLabel(" "));
				}
			
			JPanel centrePanel = new JPanel(new GridLayout(1,1));
				
				switcher.add(sinkPage(),"Sink Page");
				switcher.add(sendPage(),"Send Page");
				
				mainCard.show(switcher, "Sink Page");
				
				centrePanel.add(switcher);
				
			mainPanel.add(leftPanel, BorderLayout.WEST);
			mainPanel.add(centrePanel, BorderLayout.CENTER);
		add(mainPanel);
	}
	
	public JPanel sinkPage() {
		
		JPanel sinkPanel = new JPanel(new BorderLayout());
			JPanel sinkTop = new JPanel(new FlowLayout(FlowLayout.CENTER));
				sinkTop.add(new JLabel("SINK"));
				
			JScrollPane sinkScrol = new JScrollPane(sinkText = new JTextArea());
				sinkText.setFont(new Font("Calibril", Font.BOLD, 13));
				sinkText.setEditable(false);
				
			JPanel sinkDown = new JPanel(new FlowLayout(FlowLayout.CENTER));
				sinkDown.add(clear = new JButton("  Clear  "));
					clear.setFont(new Font("Calibril", Font.BOLD, 18));
					clear.setBackground(Color.gray);
					clear.addActionListener(listener);
				
			sinkPanel.add(sinkTop,BorderLayout.NORTH);
			sinkPanel.add(sinkScrol,BorderLayout.CENTER);
			sinkPanel.add(new JLabel("          "), BorderLayout.WEST);
			sinkPanel.add(new JLabel("          "), BorderLayout.EAST);
			sinkPanel.add(sinkDown, BorderLayout.SOUTH);
			
		return sinkPanel;
	}
	@SuppressWarnings({ "rawtypes", "unchecked" })
	public JPanel sendPage() {
		JPanel sendPanel = new JPanel(new BorderLayout());
			
			JPanel sendTop = new JPanel(new FlowLayout(FlowLayout.CENTER));
				sendTop.add(new JLabel("SEND"));
				
			JPanel sendCenter = new JPanel(new BorderLayout());
				
				JPanel sendCenterTop = new JPanel(new FlowLayout(FlowLayout.CENTER));
					sendCenterTop.add(portList = new JComboBox(new Object[] {"Select destination"}));
						portList.setFont(new Font("Calibril", Font.BOLD, 12));
					
				sendCenter.add(sendCenterTop, BorderLayout.NORTH);
				JPanel sendCenterCenter = new JPanel(new BorderLayout());
					
						JScrollPane sendScrol = new JScrollPane(sendText = new JTextArea());
						sendText.setFont(new Font("Calibril", Font.BOLD, 13));
					sendCenterCenter.add(sendScrol, BorderLayout.CENTER);
					
				sendCenter.add(sendCenterCenter, BorderLayout.CENTER);
			JPanel sendDown = new JPanel(new FlowLayout(FlowLayout.CENTER));
				sendDown.add(send = new JButton("  Send >>  "));
					send.setFont(new Font("Calibril", Font.BOLD, 18));
					send.setBackground(Color.gray);
					send.addActionListener(listener);
			sendPanel.add(sendTop,BorderLayout.NORTH);
			sendPanel.add(sendCenter, BorderLayout.CENTER);
			sendPanel.add(new JLabel("          "), BorderLayout.WEST);
			sendPanel.add(new JLabel("          "), BorderLayout.EAST);
			sendPanel.add(sendDown, BorderLayout.SOUTH);
		return sendPanel;
	}

	public static void main(String[] args) {
		Main displays = new Main();
		displays.gui();
		displays.setTitle("AIS_IDS");
		displays.setSize(600,600);
		displays.setLocationRelativeTo(null);
		displays.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		displays.setResizable(true);
		displays.setVisible(true);
		
		int port = Integer.parseInt(portText.getText().toString());
		Task func = new Task();
		func.sinkImplementation(port);
		
		ModelCall.modelCall();
	}

}
