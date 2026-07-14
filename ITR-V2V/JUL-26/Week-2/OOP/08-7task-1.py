# Q.1
class BankAccount:

    def __init__(self,holder,num,bal):
        self.account_holder = holder
        self._account_number = num
        self.__balance = bal

    def depositAmount(self):
        a = int(input("Enter deposit amount : "))
        self.__balance += a

    def widrawAmount(self,amount):
        balance = self.__balance
        self.amount = amount

        if balance > 0:
            self.amount = int(input("Enter widhraw amount : "))
            self.__balance = balance - self.amount
            print(f"Account Balance After Widrawing : {self.__balance}")
        else:
            print("Insuffiient Balance : ")

    def display(self):
        print(f"Account holder : {self.account_holder}")
        print(f"Account Number : {self._account_number}")
        print(f"Account Balance : {self.__balance}")

b1 = BankAccount("Mitesh Vaykar",6457,7000)
while(True):
    print("\n---Enter Your Choice---\n1.Deposit Amount.\n2.Widhraw Amount\n3.Display Bank Details.\n4.Exit")
    ch=int(input("\nEnter Choice : "))
    if ch == 1: b1.depositAmount()
    if ch == 2: b1.widrawAmount(0)
    if ch == 3: b1.display()
    if ch == 4: exit()