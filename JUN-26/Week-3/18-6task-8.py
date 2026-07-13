with open("data2.txt","r") as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())