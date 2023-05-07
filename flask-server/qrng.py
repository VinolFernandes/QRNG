import sys
sys.path.append('path/to/venv/Lib/site-packages')
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute,IBMQ
from qiskit.tools.monitor import job_monitor
import random

IBMQ.enable_account('2d83cf62bb682c3c5b94ec885c851e1b01366e7b4a220c549572d904b77395f911c089cb469ca7685580db427b98940777453e49bc6afe3fa1fc8f1c77a31838')
provider = IBMQ.get_provider(hub='ibm-q')

import cv2
import mediapipe as mp
#import pandas
#Face Mesh

arguments = sys.argv

mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()
#Image
image = cv2.imread(arguments[1])

print(image)

height , width , _ = image.shape
print('height=',height,'width=',width)
rgb_image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
#cv2.imshow("Image",rgb_image)
#Facial Landmark
result = face_mesh.process(rgb_image)
data1=[]
for facial_landmarks in result.multi_face_landmarks:
    for i in range(0,468):
        pt1 = facial_landmarks.landmark[i]
        x = int(pt1.x * width)
        y = int(pt1.y * height)
        #Cantor pairing function:
        data1.append(((x + y) + (x + y + 1)) / 2 + x)
        print('x=',x,'y=',y)
        cv2.circle(image,(x,y),2,(100,100,0),-1)
    print(data1)
    print(len(data1))
cv2.imwrite("img2.jpeg", image)

"""-------------------------------------------------------------------------------------------------------"""
def binaryToDecimal(n):
    decimal = 0
    power = 1
    while n>0:
        rem = n%10
        n = n//10
        decimal += rem*power
        power = power*2
        
    return decimal
x = 0
b=[]
q = QuantumRegister(9,'q')
c = ClassicalRegister(9,'c')
circuit = QuantumCircuit(q,c)
while x < 32:
    x = x + 1
    circuit.h(q) # Applies hadamard gate to all qubits
    circuit.t(q)
    circuit.measure(q,c) # Measures all qubits 

    backend = provider.get_backend('ibmq_qasm_simulator')
    job = execute(circuit, backend, shots=1)

#     print('Executing Job...\n')                 
#     job_monitor(job)
    counts = job.result().get_counts()

    print('RESULT: ',counts.keys(),'\n')
    temp=list(counts.keys())
    dec=binaryToDecimal(int(temp[0]))
    print('Decimal Eqauivalent: ',dec,'\n')
    b.append(dec)
print(b)
"""--------------------------------------------------------------------------------------------------------------"""

# import random
# import array
# random.shuffle(data1)

arr=[]
for k in range(0,32):
    if(b[k]<=468):
        arr.append(data1[b[k]])
    else:
        arr.append(data1[b[k]-468])
print(arr)
"""--------------------------------------------------------------------------------------------------------------"""
import numpy as np
X = np.array(arr)
X = np.asarray(X, dtype = 'int')
print(X)
b = X
c = []
seq = []
subseq = []

lenn = len(b)
mod = len(b) % 4
actual = lenn - mod
for p in range(0,actual,4):
    c.append(b[p:p+4])
#print(c)
for p in range(0, len(c) + 2):
    counter_subseq = 0
    a = [0, 0, 0, 0]
    for q in range(0, 4):
        if p >= len(c):
            a[q] = 0
            p = p + 1
        else:
            a[q] = c[p][q]
            p = p + 1
    check = False
    for i in seq:
        if a == i:
            check = True
            break
    if check == False:
        l = []
        l.append(a[0])
        l.append(a[1])
        l.append(a[2])
        l.append(a[3])
        seq.append(l)
    while check == False:
        summ = (a[0] + a[2]) % 512;
        temp = a[0]
        counter = a[0]
        for i in range(0, 3):
            a[i] = a[i+1]
        a[3] = summ
        t1 = a[0]
        t2 = a[1]
        t3 = a[2]
        t4 = a[3]
        for i in seq:
            if i == a:
                check = True
                break
        if check == False:
            counter_subseq += 1
            l = []
            l.append(a[0])
            l.append(a[1])
            l.append(a[2])
            l.append(a[3])
            seq.append(l)
    if counter_subseq > 0:
        subseq.append([c[p-4:p], counter_subseq])
zx=0
for i in seq:
    zx=zx+1
    print(i)
seed = []
useed=[]
for i in range(len(subseq)):
    seed.append(subseq[i][0])
print(seed)
for i in range(len(seed)):
    useed.append([seed[i][0],subseq[i][1]])
print(useed)
print(len(useed))


k=0
for i in seq:
  k+=1
  print(i[0],end=', ')

print('')  
print('total number of sequence generated :',k)
print("seed value vs number of subsequence generated")
for i in useed:
  print(i[0],end='  \t')
  print(i[1])
print("Total number of seed values = ",len(useed))
"""---------------------------------------------------------------------------------------------"""
# Key length can be changed
key=[]
p=0
for j in seq[512:]:#set to 0
    if j[0]!=0:
        key.append(j[0])
        p=p+1
    if p>=1024:#change length here
        break
        
output = arguments[2]

joinedKey=""
for i in range(len(key)):
    a=str(int(key[i]))
    joinedKey=joinedKey+a
print(joinedKey)

def BinaryToDecimal(binary):
        
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return (decimal) 

str_data =' '
count_bit=0
for i in range(0, len(joinedKey), 2):
    temp_data = int(joinedKey[i:i + 8])
    decimal_data = 48+BinaryToDecimal(temp_data)%74
    
    if decimal_data>57 and decimal_data<65:
        decimal_data=random.randint(48, 57)
    if decimal_data>90 and decimal_data<97:
        decimal_data=random.randint(48, 57) 
    # Decoding the decimal value returned by
    # BinarytoDecimal() function, using chr()
    # function which return the string corresponding
    # character for given ASCII value, and store it
    # in str_data
    str_data = str_data + chr(decimal_data)
    count_bit=count_bit+1

# printing the result
print("The Binary value after string conversion is:",str_data)
print("Number of characters: ",count_bit)

file = open(output, 'w')

file.write(str_data)