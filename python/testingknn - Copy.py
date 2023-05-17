detectors=[]
import csv,struct

with open('detectors.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
           # print ("",row)
            detectors.append(row)

        
#print("\n",detectors)


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
   #if knnDistance < .90 :
   if knnDistance < .80 :
      result='attack'
      print("attack")
   else:
      result='normal'     
      print("normal")
   return result


###-----------------------------------------------

# result=[]
# testInstance=[]
#
# with open('testinst.csv', 'r') as f:
# #with open('C:\\Users\BBWiSE\\Documents\\Projects\Development of an Artificial Immun System-based Network Intrusion Detectioin System Using Negative and Positive Selection\\python\\TestBook.csv', 'r') as f:
#     reader = csv.reader(f)
#     for row in reader:
#             print ("",row)
#             testInstance.append(row)
#print(len(testInstance))
# for i in range(len(testInstance)):
#         #print(type(testInstance[i]))
#         neighbors = getNeighbors(detectors, testInstance[i], 1)
#         print("testInstance[i]",*testInstance[i], sep=',')
#         knnDistance=euclideanDistance1(neighbors[0],testInstance[i])
#         print("\n knnDistance",knnDistance)
#         result.append(testing(knnDistance))
#











# =================================================================
# =================================================================
# =================================================================
# =================================================================
result=[]
testInstance=[]

with open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\Book2.csv', 'r') as f:
#with open('C:\\Users\BBWiSE\\Documents\\Projects\Development of an Artificial Immun System-based Network Intrusion Detectioin System Using Negative and Positive Selection\\python\\TestBook.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
            #print ("",row)
            testInstance.append(row)
for i in range(len(testInstance)):
        #print(type(testInstance[i]))
        testInstance_ = [] #    bin_to_float(stringToBinary(
        
        testInstance_.append(bin_to_float(stringToBinary(testInstance[i][0])))
        testInstance_.append(bin_to_float(stringToBinary(testInstance[i][1])))
        testInstance_.append(bin_to_float(stringToBinary(testInstance[i][2])))
        testInstance_.append(bin_to_float(stringToBinary(testInstance[i][3])))
        testInstance_.append(testInstance[i][4])
        testInstance_.append(testInstance[i][5])
        testInstance_.append(bin_to_float(stringToBinary(testInstance[i][6])))
        testInstance_.append(testInstance[i][7])
        
        print("\n",testInstance_)
        
        neighbors = getNeighbors(detectors, testInstance_, 1)
        #print("testInstance["+i+"]",*testInstance[i], sep=',')
        knnDistance=euclideanDistance1(neighbors[0],testInstance_)
        print(" knnDistance",knnDistance)
        result.append(testing(knnDistance))
# =================================================================
# =================================================================
# =================================================================
# =================================================================






print("\n",*result,sep='\n')
