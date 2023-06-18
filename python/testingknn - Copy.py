detectors=[]
import csv,struct

with open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\detector_used\\detectors_11000.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
            detectors.append(row)


# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
# =======================================================================================================
def stringToBinary(text):
    
    return ''.join(format(ord(i), '08b') for i in text)


def bin_to_float(b):
    """ Convert binary string to a float. """
    bf = int_to_bytes(int(b, 2), 8)  # 8 bytes needed for IEEE 754 binary64
    return struct.unpack('>d', bf)[0]

def int_to_bytes(n, minlen=0):  # helper function
    """ Int/long to byte string. """
    nbits = n.bit_length() + (1 if n < 0 else 0)  # plus one for any sign bit
    nbytes = (nbits+7) // 8  # number of whole bytes
    b = bytearray()
    for _ in range(nbytes):
        b.append(n & 0xff)
        n >>= 8
    if minlen and len(b) < minlen:  # zero pad?
        b.extend([0] * (minlen-len(b)))
    return bytearray(reversed(b))  # high bytes first

# =======================================================================================================
# =======================================================================================================
# =======================================================================================================

import math
def euclideanDistance(instance1, instance2, length):
	distance = 0;
	for x in range(length):
		distance += pow((float(float(instance1[x]) - float(instance2[x]))), 2)
        
	return math.sqrt(distance)

import operator 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
    
	print("   (len(testInstance)",len(testInstance))
	length = len(testInstance)   ############euclidean distance changed length not included attack or normal
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	print(" test neighbors",neighbors) 
	return neighbors

##########################
# -----------------------------------------------------------euclidean  and for testing only 
def euclideanDistance1(instance1,instance2):    
        
        ret = []
        distance=0
        len(instance2)
        for i in range(len(instance2)):
           
           distance= distance+pow(float(float(instance1[i])-float(instance2[i])),2) 
                #ret.append(math.sqrt(distance))
        return math.sqrt(distance)



def testing(knnDistance):
   if knnDistance < .70 :
      #result='attack'
      result=1
      print("attack")
   else:
      result=0
      #result='normal'     
      print("normal")
   return result


# =================================================================
# =================================================================
# =================================================================
# =================================================================
result=[]
testInstance=[]

attackNames =['normal', 'mscan', 'guess_passwd', 'snmpgetattack', 'processtable', 'snmpguess', 'ipsweep', 'mailbomb']

with open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\dataset_used\\'+attackNames[7]+'.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
            #print ("",row)
            testInstance.append(row)
outcome = [];
ii =1;
for e in testInstance:
        testInstance_ = [] #    bin_to_float(stringToBinary(
        
        print(ii)
        ii +=1
        
        testInstance_.append(bin_to_float(stringToBinary(e[0]))) # source_bytes
        testInstance_.append(bin_to_float(stringToBinary(e[1]))) # service
        testInstance_.append(bin_to_float(stringToBinary(e[2]))) # dst_bytes
        testInstance_.append(bin_to_float(stringToBinary(e[3]))) # flag
        testInstance_.append(e[4]) # diff_srv_rate
        testInstance_.append(e[5]) # same_srv_rate
        testInstance_.append(bin_to_float(stringToBinary(e[6]))) # dst_host_srv_count
        testInstance_.append(e[7]) # dst_host_same_srv_rate
        
        outcome.append(int(e[8]))
        
        print("\n",testInstance_)
        
        neighbors = getNeighbors(detectors, testInstance_, 1)
        knnDistance=euclideanDistance1(neighbors[0],testInstance_)
        print(" knnDistance",knnDistance)
        result.append(testing(knnDistance))
        
# =================================================================
# =================================================================
# =================================================================
# =================================================================

#print("\n",*result,sep='\n')
print("result lenght:",len(result))
print("outcome lenght:",len(outcome))
print("The length of the datapoint is: ",len(result))

print("\n\n\n\n")
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import  numpy as np

print("confusion metrics:",confusion_matrix(outcome, result))
print("accuracy:", accuracy_score(outcome, result))
print("precision:", precision_score(outcome, result, average='weighted', labels=np.unique(outcome)))
print("recall:", recall_score(outcome, result, average='weighted', labels=np.unique(outcome)))
print("f1 score:", f1_score(outcome, result, average='weighted', labels=np.unique(outcome)))


