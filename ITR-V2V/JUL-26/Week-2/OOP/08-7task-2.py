#  Q.2

class BankAccount:

    def __init__(self,holder,num,bal):
        self.acc_holder = holder            #public
        self._acc_number = num              #protected
        self.__balance = bal                #private

b1 = BankAccount("Mitesh Vaykar",6457,7000)

print(f"Account Holder : {b1.acc_holder}")
print(f"Account Number : {b1._acc_number}")
print(f"Account Balance : {b1.__balance}")          #error 