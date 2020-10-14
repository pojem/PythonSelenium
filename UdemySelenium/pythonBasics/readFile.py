file = open('test.txt')

# read all the contents of file

#print(file.read(12)) # print number of chars. new line is also char

#print(file.readline()) #read first line
#print(file.readline()) # read second line

#file.close()

#print line by line using readLine method

#print(file.readlines()) # stored in

aaa = file.readlines()

for i in aaa:
    print(i)

line = file.readline()

while line !="":
    print(line)
    line = file.readline()


file.close()
