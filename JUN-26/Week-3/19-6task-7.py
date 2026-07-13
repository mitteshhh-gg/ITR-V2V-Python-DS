# Print line numbers with each line
with open("notes.txt","r") as file:
    lines = file.readlines()

i = 1
for line in lines:
    print(f"{i}: {line.strip()}")
    i += 1