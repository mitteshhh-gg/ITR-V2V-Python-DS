class BankAccount:

    def __init__(self,holder,num,bal):
        self.account_holder = holder
        self._account_number = num
        self.__account_balance = bal

    def depositAmount(self):
        a = int(input("Enter deposit amount : "))
        self.__account_balance += a

    def widrawAmount(self):
        balance = self.__account_balance
        # balance = bal
        if balance > 0:
            b = int(input("Enter widhraw amount : "))
            self.__account_balance = balance - b
        else:
            print("Insuffiient Balance : ")

    def display(self):
        print(f"Account holder : {self.account_holder}")
        print(f"Account Number : {self._account_number}")
        print(f"Account Balance : {self.__account_balance}")

b1 = BankAccount("Mitesh",6457,7000)

while(True):
    print("\n---Enter Your Choice---\n1.Deposit Amount.\n2.Widhraw Amount\n3.Display Bank Details.\n4.Exit")
    ch=int(input("\nEnter Choice : "))
    if ch == 1: b1.depositAmount()
    if ch == 2: b1.widrawAmount()
    if ch == 3: b1.display()
    if ch == 4: exit()