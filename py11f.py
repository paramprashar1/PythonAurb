file=open("py11.py","r")
data = file.read(15)
print(data)
print("==============")
data = file.read(30)
print(data)
print("=========")
data = file.readlines()
print(data)
print("Is file closed?",file.closed)
file.close()
print("Is file closed?",file.closed)
