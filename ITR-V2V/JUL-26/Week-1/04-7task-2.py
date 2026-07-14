import matplotlib.pyplot as plt

students = ["Smaran","Amaran","Jeevaran","Dalvaaran"]
mark = [87,92,83,94]

plt.bar(
    students,
    mark,
    color = "pink",
    edgecolor = "black",    
    linewidth = 2
)

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()
