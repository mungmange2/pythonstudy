import sys 

f = open(sys.argv[1] , 'r') 
data = f.readlines()[::-1]
for line in data:
    print(line)