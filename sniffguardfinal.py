print("Welcome to SniffGuard :) ")
from scapy.all import sniff,wrpcap,IP,TCP,UDP  #Scapy is a powerful Python library for network packet manipulation.
from collections import defaultdict #this module is used to set the default values to 0
from datetime import datetime
import os
from email.message import EmailMessage
import smtplib

count_packets = defaultdict(int)
count_syn = defaultdict(int)
count_udp = defaultdict(int)
suspicious_packets = []

packets_threshold = 100
syn_threshold = 30 #if more than 30 syn packets from an ip then it will be set as malicious
udp_threshold = 30

#this packet will be called whenever every packet is to come up(sorry for the messed up and rushed english lmao )
def packet_capture(packet):
    if IP in packet:
        source_ip = packet[IP].src 
        count_packets[source_ip] += 1
        
        if TCP in packet:
            flag = packet[TCP].flags
            #now checking if the packet is syn (0x02)
            if flag == 0x02: #means a syn flag 
                count_syn[source_ip] +=1 #incrementing the syn count for this particular ip 
        if UDP in packet:
            count_udp[source_ip] +=1
            
                
        if count_packets[source_ip] > packets_threshold:
            print(f"Alert!! -> Packet flooding noticed from {source_ip}")
            suspicious_packets.append(packet)
            
        if count_syn[source_ip] > syn_threshold:
            print(f"Alert!! -> Syn flood attack noticed from {source_ip}")
            suspicious_packets.append(packet)
            
        if count_udp[source_ip] > udp_threshold:
            print(f"Alert!! -> UDP flood attack noticed from {source_ip}")
            suspicious_packets.append(packet)
            
            
            
def send_email_alert(file_path):
    SENDER_EMAIL = "sender_email"
    RECEIVER_EMAIL = "reciever_email"
    EMAIL_PASSWORD = "your_password"


    msg = EmailMessage()
    msg['Subject'] = 'SniffGuard Alert: Suspicious Packets Detected'
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECEIVER_EMAIL
    msg.set_content('SniffGuard has detected suspicious network activity. The .pcap file is attached.')

    with open(file_path, 'rb') as f:
        file_data = f.read()
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=os.path.basename(file_path))

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, EMAIL_PASSWORD)
        smtp.send_message(msg)
        print(f"[+] Email alert sent to {RECEIVER_EMAIL}")   
        
        
        
        
        
capture_count = int(input("Enter the number of packets you want to capture to sniff and analyze them"))
sniff(iface = "lo",prn = packet_capture,count = capture_count, timeout=60)  #sniff and capture the number of packets the user want to capture

#Now after finding and storing the suspicious packets in a list then we are gonna store them in .pcap file which we can analyze as well through wireshark

if suspicious_packets:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # Create a unique filename with timestamp like for eg: If the current date and time were 2023-09-15 at 14:30:45, the output would be "20230915_143045". This will be thus used to generate a unique filename.
    filename = f"suspicious_packets_{timestamp}.pcap" #for example the name of the file can be "suspicious_packets_20230915.pcap" thus making it impossible to have pcap files with same name 
    wrpcap(filename, suspicious_packets)  # Save suspicious packets to file
    print(f" :) Suspicious packets saved to {filename}")
    send_email_alert(filename)
else:
    print("  No suspicious packets detected.")

         
            


            
            
    
    
    
