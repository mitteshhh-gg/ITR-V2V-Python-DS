# Append a new line to notes.txt.
f = open("notes.txt","a")

f.write("\nAppended Line")
f.close()
print("Completed!")