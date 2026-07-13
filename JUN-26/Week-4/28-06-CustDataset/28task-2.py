import pandas as pd

cust = pd.read_csv("28-06-CustDataset/28-06-customer.csv")
ord = pd.read_csv("28-06-CustDataset/28-06-order.csv")

print(f"Customer Dataset : \n{cust}")
print(f"Order Dataset : \n{ord}")

#Left-Join
left_join = pd.merge(cust, ord, on="customerID", how= "left")
print(f"Left Join : \n{left_join}")

#Inner-Join
inner_join = pd.merge(cust, ord, on="customerID", how="inner")
print(f"Inner Join : \n{inner_join}")

#Right-Join
right_join = pd.merge(cust, ord, on="customerID", how="right")
print(f"Right Join : \n{right_join}")

#Outer-Join
outer_join = pd.merge(cust, ord, on="customerID", how="outer")
print(f"Outer Join : \n{outer_join}")
