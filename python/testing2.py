from math import*
import numpy as np
import random
import csv
import sqlite3
import struct
individualSize=8
#individualSize=6
populationSize=1000
mutation_rate = 1
#delete=[]
population = [];
a=[]
normal=[]
euclinormal=[]
rs=.20

distance=0#for find distance
global decimal;
from numpy import binary_repr

for i in range(populationSize): 
   individual=[]
   for i in range(individualSize):
        
         individual.append(str(np.float16(random.random())))
   population.append(individual)
   
#print(*population,sep='\n') ====================



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
# tests
def float_to_bin(f):
    """ Convert a float into a binary string. """
    ba = struct.pack('>d', f)
    ba = bytearray(ba)  # convert string to bytearray - not needed in py3
    s = ''.join('{:08b}'.format(b) for b in ba)
    return s[:-1].lstrip('0') + s[0] # strip all leading zeros except for last

def get_num(x):
         return float(''.join(ele for ele in x if ele.isdigit() or ele == '.'))
         #return float(''.join(ele for ele in range(x) if ele.isdigit() or ele == '.'))       

#----------------------euclidean distance------------------------------------

#print('BBWiSE',bin_to_float('BBWiSE'))


def euclidean_distance(x,y):
                 
     return sqrt(sum(pow(float(get_num(a)-get_num(b)),2) for a, b in zip(x, y)))
#print("\neuclidean_distance",euclidean_distance(parent1,parent2))   


#-------------------------------crossover-------------------------------------------
# ========================== FIRST ENTERING TAKING THE WHOLE DATASET ================================================ BBWiSE
def crossover(individual):
      x=0
      child_pop=[]
      while x < populationSize:
           parent1=random.choice(individual)
           parent2=random.choice(individual)
           start = random.randint(1, len(parent1)-2)
           end = random.randint(1, len(parent1)-2)
           if start > end:
             start, end = end, start
            # print("\nparent1",parent1)
            # print("parent2",parent2)
             child1 = parent1[:start] + parent2[start:end] + parent1[end:]
             child2 = parent2[:start] + parent1[start:end] + parent2[end:]
#----------------------mutation on cross over child-----------------
            # print("\nchild1",child1)
            # print("child2",child2)
             mutchild1=mutation(child1)
            # print("\nmutchild1",mutchild1)
             compare_append(parent1,mutchild1)
             
#------------------------------distance--------------------          
             mutchild2=mutation(child2)
            # print("mutchild2",mutchild2)
             compare_append(parent2,mutchild2)
             
                     
  #..............................                 
             child_pop.append(child1)#child population not final population
             child_pop.append(child2)
           x = x+1       
      # print("child_pop",*child_pop,sep='\n')#only after child-pop.append
    #  print("population",*population,sep='\n')#actual final population as the result of genetic algorithm
      
      return population  
#-----------------------------------------------------------------------------------------------------------

#--------------------------------------mutation--------------------
def mutation(child):
  mutatedCh = []
  mutatedCh=child
  #print("mutatedCh",mutatedCh)
  pos = random.randint(0, len(child) - 1)#take a position of child 
  #print("change element @ ",pos)
  child = list(child)
   
  if random.random() < mutation_rate:
        
        #print("child[pos]",child[pos])
        child=get_num(child[pos])
        
        binary = float_to_bin(child)#conversion
        
        binary=list(binary)
        #print(binary)
        posofa = random.randint(0, len(binary) - 1)#take pos of binary
       
        if (binary[posofa] == '0'):#if it has the value 0 change to 1 
            binary[posofa] = '1'
            #print("change 0 to 1 ",binary)
        else:#else change to 0
            #print("change 1 to 0\n",binary)
            binary[posofa] = '0'
        "".join(binary)               
     # mutation end
        for digit in binary:
             string ="".join(binary)
             #string.append(digit)
        #print(string)
     #back to float
        binary=string  
        #print(binary)
        float = bin_to_float(binary)#conversion
        #print(float);
        #print('bin_to_float(%r): %f' % (binary, float))               
  #assert mutatedCh != ch
  
  
  mutatedCh.insert(pos,'%f'%(float))
  del(mutatedCh[pos+1])
  #print("mutatedCh",mutatedCh)
  return mutatedCh

#----------------------euclidean distance------------------------------------
def euclidean_distance(x,y):
     return sqrt(sum(pow(float(get_num(a)-get_num(b)),2) for a, b in zip(x, y)))
#print("\neuclidean_distance",euclidean_distance(parent1,parent2))   


#-----------------------------------------------------------------------------------------------------------
def compare_append(parentpopulation,childpopulation):
   eucliDist=euclidean_distance(parentpopulation,childpopulation)
   # print("euclidean_distance parent&child",eucliDist)
   # print("fitness(child)",fitness(childpopulation))
   # print("fitness(parent)",fitness(parentpopulation))
   if eucliDist > rs and fitness(childpopulation) > fitness(parentpopulation) :
   #   print("success")
      #if 
   #   print("parent <- child")
      
      population.remove(parentpopulation)
      population.append(childpopulation)
      #print("fail")
   else :
      print("unsucess")
      #childpopulation=mutation(childpopulation)
      #compare_append(parentpopulation,childpopulation)
   return population

         

#print("after compare and append population",*population,sep='\n')
#-----------------------------------------------------------------------------------------------
def stringToBinary(text):
    
    return ''.join(format(ord(i), '08b') for i in text)

def dist_nearest_self(individualpopulation):

   #I'm working on this very function. ============================================================== BBWiSE
   #data = open('only nameof feature.csv', "r")
   data = open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\dataset_used\\KDDTrain+_.csv', "r")
   #data = open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\TestBook.csv', "r")
   reader = csv.reader(data)
   conn = sqlite3.connect(':memory:')
   c = conn.cursor()
   j = conn.cursor()
   c.row_factory = sqlite3.Row
   j.row_factory = sqlite3.Row
   c.execute("create table FeatureTable ( source_bytes text,service text,destination_bytes text,flag text,diff_srv_rate text,same_srv_rate text,dst_host_srv_count text,dst_host_same_srv_rate text)")
   # c.execute("create table FeatureTable (protocol,service,dst_bytes,is_guest_login,dst_host_count,dst_host_same_src_port_rate)");
   conn.commit()
   
   i_ =1
   for e in reader:
      if(i_<=11001):
          
          test= []     
          # test.append(e[0])  
          # test.append(e[1])
          # test.append(e[2])
          # test.append(e[3])
          # test.append(e[4])
          # test.append(e[5])
          # test.append(e[6])
          # test.append(e[7])
          #
          
          print(i_)
          i_ +=1
          
          # test.append(bin_to_float(stringToBinary(e[0])))
          # test.append(bin_to_float(stringToBinary(e[1])))
          # test.append(bin_to_float(stringToBinary(e[2])))
          # test.append(bin_to_float(stringToBinary(e[3])))
          # test.append(e[4])
          # test.append(e[5])
          # test.append(bin_to_float(stringToBinary(e[6])))
          # test.append(e[7])
          
          test.append(bin_to_float(stringToBinary(e[4]))) # source_bytes
          test.append(bin_to_float(stringToBinary(e[2]))) # service
          test.append(bin_to_float(stringToBinary(e[5]))) # dst_bytes
          test.append(bin_to_float(stringToBinary(e[3]))) # flag
          test.append(e[29]) # diff_srv_rate
          test.append(e[28]) # same_srv_rate
          test.append(bin_to_float(stringToBinary(e[32]))) # dst_host_srv_count
          test.append(e[33]) # dst_host_same_srv_rate
          
          c.execute("insert into FeatureTable values (?,?,?,?,?,?,?,?)", test)
          #c.execute("insert into FeatureTable values (?,?,?,?,?,?)", test)
      else:
          break
#print (test)
   conn.commit()
   sql = "SELECT source_bytes,service, destination_bytes, flag,diff_srv_rate, same_srv_rate, dst_host_srv_count, dst_host_same_srv_rate  FROM FeatureTable "
   # sql = "SELECT protocol,service,dst_bytes,is_guest_login,dst_host_count,dst_host_same_src_port_rate FROM FeatureTable"
   j.execute(sql)
   del euclinormal[:]
   for row in j:
      euclinormal.append(euclidean_distance(individualpopulation,row))
   #print("euclinormal",*euclinormal,sep='\n')
   #print("euclidean_distance",*euclinormal,sep='\n')
   #print("alleuclidean_distance",euclinormal,"individualpopulation",*individualpopulation,"normal",*normal,sep='\n')
   return min(euclinormal)

#-----------------------------------------------------------------------------------------------------------------------------

def fitness(individualpopulation) :
   fitness=0
   D=dist_nearest_self(individualpopulation)
   fitness=exp(-(rs/D))
   return fitness
               

#-------------------------------------------------------------------------------------------------------------------------------------
detectors=[]
detectors=crossover(population)

#################################################################################################################################
#################################################################################################################################


#======================== WRITTING THE DATA INTO A CSV FILE ======================================================= BBWiSE
import csv
with open('C:\\Users\\BBWiSE\\eclipse-workspace\\jse\\AIS_IDS\\python\\dataset\\detector_used\\detectors_11000.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(detectors)


'''
import csv
with open('F:/GECBH/internet explorer/artificial intelligence/fwdlinkstoieeepapers/2ndcodeunder constrn/csvzzz/detectors.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print ("\n",row)


'''





























