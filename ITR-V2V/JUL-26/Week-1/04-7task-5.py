import matplotlib.pylab as mp

x = [3,19,25,32,48,34,32,13,41,29]
y = [5,10,15,20,25,30,35,40,45,50]

mp.scatter(
    x,
    y,
    color = "pink",
    edgecolor = "black" 

)

mp.title("Scatter Plotting")
mp.xlabel("X - Label")
mp.ylabel("Y - Label")
mp.show()