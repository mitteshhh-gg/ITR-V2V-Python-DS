# After appending,read & print the file to check content
f = open("notes.txt","r")
content = f.read()
print(content)
f.close()
