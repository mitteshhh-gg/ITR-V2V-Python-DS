#VARIOUS FUNTION OF TUPLE
#creation of tuple
coords = (10,20)
print("\nTuple-1 : ", coords)

#accessing elements
print("Element at 2nd position in tuple : ", coords[1])

#accesing elements using negative index 
fruits = ("apple","banana","cherry")
print("\nTuple-2 : ", fruits)
print("Accessing element using negative index(-1):",fruits[-1])

#slicing a tuple 
nums = (10,20,30,40,50)
print("\nTuple-3:",nums,"\nSlicing[0:4] : ",nums[0:4])
#finding index
print("Index of 20 : ",nums.index(20))

#counting elements
numbers = (1,2,1,3,1,)
print("\nTuple-4 : ",numbers)
print("Counting number of 1's : ",numbers.count(1))

#concatenation
t1 = (1,2,3)
t2 = (4,5)
t3 = t1 + t2
print("\nAfter Concatenation : ",t3)

