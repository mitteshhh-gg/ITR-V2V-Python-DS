import matplotlib.pyplot as plt

students = ["Smaran","Amaran","Jeevaran","Dalvaaran"]
mark = [87,92,83,94]

plt.figure(facecolor="lightblue")

plt.plot(
    students,
    mark,
    color = "pink",
    marker="*",
    markeredgecolor = "black",    
    markerfacecolor = "yellow",    
    linewidth = 4,
    markersize = 10
)

plt.grid(axis="y" ,linestyle = "--")
plt.show()