# Appending into a File

with open("data1.txt","a") as file:
    file.write("\nAppended Line\n")

print("Data Appended")