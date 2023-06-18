import csv

#======================== WRITTING THE DATA INTO A CSV FILE ======================================================= BBWiSE
def saver(datap,attackName):
    with open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\dataset_used\\'+attackName+'.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(datap)

#attackNames =['neptune', 'normal', 'saint', 'mscan', 'guess_passwd', 'smurf', 'apache2', 'satan', 'buffer_overflow', 'back', 'warezmaster', 'snmpgetattack', 'processtable', 'pod', 'httptunnel', 'nmap', 'ps', 'snmpguess', 'ipsweep', 'mailbomb', 'portsweep', 'multihop', 'named', 'sendmail', 'loadmodule', 'xterm', 'worm', 'teardrop', 'rootkit', 'xlock', 'perl', 'land', 'xsnoop', 'sqlattack', 'ftp_write', 'imap', 'udpstorm', 'phf']
attackNames =['normal', 'mscan', 'guess_passwd', 'snmpgetattack', 'processtable', 'snmpguess', 'ipsweep', 'mailbomb']

for a in attackNames:
    datapoin=[]
    
    print(a)
    
    data = open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\dataset_used\\KDDTest+_.csv', "r")
    reader = csv.reader(data)
    
    for e in reader:
       if(e[41]==a):
           test= []
           print(e[41])
           
           test.append(e[4]) # source_bytes
           test.append(e[2]) # service
           test.append(e[5]) # dst_bytes
           test.append(e[3]) # flag
           test.append(e[29]) # diff_srv_rate
           test.append(e[28]) # same_srv_rate
           test.append(e[32]) # dst_host_srv_count
           test.append(e[33]) # dst_host_same_srv_rate
           test.append(e[41]) # outcome
           
           datapoin.append(test)
           
    
    saver(datapoin,a)
       
