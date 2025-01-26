file=open('Codingal.txt','r')
print(file.read())
file.close()

file = open('Codingal.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file=open('Codingal.txt','a')
file.write("Hi! i am penguin andI am 2 yr old.")
file.close()


file=open('Codingal.txt','r')
print("Reading first line...")
print(file.readline())
file.close()

file = open('Codingal.txt','r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()

file = open('Codingal.txt','r')
print("Looping through the lines...")
for line in file:
    print(line)
file.close()