#read()
with open("myfile.txt", "r") as f:
    content = f.read()
print(content)


with open("myfile.txt", "r") as f:
    content = f.read(10)
print(content)


with open("myfile.txt", "r") as f:
    content = f.read()
print("Number of characters:", len(content))


#readline()
with open("myfile.txt", "r") as f:
    line1 = f.readline()
print(line1.strip())


with open("exmyfilemple.txt", "r") as f:
    for _ in range(3):
        print(f.readline().strip())
        
        
with open("myfile.txt", "r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line.strip())
        
        
#readlines()
with open("myfile.txt", "r") as f:
     lines = f.readlines()
print(lines)


with open("myfile.txt", "r") as f:
    lines = f.readlines()
for line in lines:
    print(line.strip())
    
    
with open("myfile.txt", "r") as f:
    lines = f.readlines()
print("First line:", lines[0].strip())
print("Second line:", lines[1].strip())