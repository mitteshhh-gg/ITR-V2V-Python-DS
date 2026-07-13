#Variables
intNum = 35
floatNum = 115.78
strText = "Hello User"
boolCh = True
complexNum = 3 + 4j

#displaying along with their data-type
print("\nInt : ", intNum)
print("Data-Type : ", type(intNum))

print("\nFloat : ", floatNum)
print("Data-Type : ", type(floatNum))

print("\nString : ", strText)
print("Data-Type : ", type(strText))

print("\nBoolean : ", boolCh)
print("Data-Type : ", type(boolCh))

print("\nComplex Number : ", complexNum)
print("Data-Type : ", type(complexNum))

#type-converison
int_to_float = float(intNum)
float_to_string = str(floatNum)
int_to_string = str(intNum)

print("\nInteger to Float : ", int_to_float)
print("Data-Type : ", type(int_to_float))

print("\nFloat to String : ", float_to_string)
print("Data-Type : ", type(float_to_string))

print("\nInteger to String : ", int_to_string)
print("Data-Type : ", type(int_to_string))
