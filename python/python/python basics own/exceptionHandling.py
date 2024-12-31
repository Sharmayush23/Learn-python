#Create Classes for Product, Cart, and Order:

     # Product: Holds details about the product like name, price, and stock.
     # Cart: Handles adding products and calculating the total price.
     # Order: Handles the checkout process and simulates payment.
     # Exception Handling:

     # Invalid Price: When a non-numeric price is entered, raise a ValueError.
     # Insufficient Stock: If a user attempts to add more products than available, raise an InventoryError.
     # Invalid Payment: Handle errors like insufficient funds or payment timeouts with custom exceptions.

class shop:
    pass


#there are three blocks in exception handling
     # try: block of code to be attempted
     # except: block of code will execute if there is an error in try block
     # finally: block of code will always execute regardless of an error
#raise: keyword used to raise an exception manually 
#code
class BANK:
    def __init__(self,balance):
        self.bank_balance =balance

    def withdraw(self,amount):
        if amount<0:
            raise Exception("kuch bhi kya aukat main rah")
        if amount>self.bank_balance:
            raise Exception("insufficient balance fir se")
        
        else:
            self.bank_balance -= amount
            return self.bank_balance
        
b1 = BANK(1000)
try:
    b1.withdraw(22)
except Exception as e:
    print(e)
  

#assert: keyword used to test a condition and trigger an exception if the condition is false
   #assert condition, message
   #assert 2+2 == 4, 'Error: 2+2 is not 4'
   #assert 2+2 == 5, 'Error: 2+2 is not 5'


