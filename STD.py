import csv

with open("numbers.csv",newline= "") as f:
    read = csv.reader(f)
    file_data=list(read)
    
data=file_data[0]

def mean(data):
    n =len(data)
    total = 0
    for i in data:
        total += int(i)
    m= total/n
    return m

squaredata = []
for i in data :
    a = int(i)-mean(data)
    a = a**2
    squaredata.append(a)
    
sum = 0
for i in squaredata:
    sum += i
    
result = sum/(len(data) - 1)

import math
std = math.sqrt(result)

print(f"the standard derivation of data is : {std}")

import statistics
s = [60,61,65,63,98,99,90,95,91,96]
print(f"the standard derivation of data is : {statistics.stdev(s)}")