#VARIOUS LIST FUNCTION
#creating list
fruits = ["apple","banana","cherry"]
print("\nList : ",fruits)

#accessing elements
print("\nElement at position 1 : ",fruits[1])

#accessing elements using -ve index
print("\nElement at position -1 : ",fruits[-1])

#slicing elements
print("\nSlicing [1:3] : ",fruits[1:3])

#adding elements
fruits.append("mango")
print("\nAfter appending mango : ",fruits)

#inserting element at a particular position
fruits.insert(1,"peach")
print("\nAfter inserting element : ", fruits)

#changing element 
fruits[0] = "grape"
print("\nAfter changing element at 1st position : ", fruits)

#removing element
fruits.remove("banana")
print("\nAfter removing : ", fruits)








#INDEXING
# f1 = ["mango", "banana","cherry"]
# print(f1[0])
# print(f1[-3])
# print(f1[1])
# print(f1[-2])
# print(f1[-1])
# print(f1[2])