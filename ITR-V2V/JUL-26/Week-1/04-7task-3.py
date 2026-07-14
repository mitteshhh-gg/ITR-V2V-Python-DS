import seaborn as sns 
import matplotlib.pyplot as plt

students = ["Smaran","Amaran","Jeevaran","Dalvaaran"]
mark = [87,92,83,94]

sns.barplot(x=students, y=mark)

plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.show()
