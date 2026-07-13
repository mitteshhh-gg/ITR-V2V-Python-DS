# T-3 Add input for score and handle invalid values.

score = int(input("Enter your score : "))
if(score < 0 or score > 100):
    print("invalid input!")
elif(score >= 90):
    print("Grade A")
elif(score >= 80):
    print("Grade B")
elif(score >= 60):
    print("Grade C")
else:
    print("Failed!")