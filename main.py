# class Person:
#     def __init__(self, name):
#         self.__name = name
#         print("Person Constructor", self.__name)

#     def get__name(self):
#         return self.__name

#     def set__name(self,new_name):
#         if self.__name == new_name:
#             print("The same name")
#         else:
#             self.__name = new_name
#         return self.__name

#     def __del__(self):
#         print("Destructor", self.__name)

#     def __show_name(self):
#         print("Hello", self.__name)


# # Bill = Person()
# # Bill.show_name()
# # Tom = Person()
# # Tom.name = "TOM"
# # Tom.show_name()
# # Jeck = Person("Jeck")
# # Jeck.__show_name()
# # Bobik = Person("Bobik")
# # Bobik.__show_name()
# # Bobik.__name = "AAA"
# # Bobik.__show_name()
# Bill = Person("Bill")
# print(Bill.get__name())
# print(Bill.set__name("Steve"))
from random import randint
print("\t\t\t--------------Wellcome to our BANK!--------------")
input()
while True:
    print("""
          ----MENU----
          press 1 to create new Account
          press 2 to enter some money to your Account
          press 3 to check out from your Account
          press 0 to exit..
          """)
    menu_cheker = int(input())
    if menu_cheker == 0:
        print("You has left =(")
        input()
        break
    elif menu_cheker == 1:
        class Account:
            def __init__(self, card_number, amount, currancy):
                self.__card_number = card_number
                self.__amount = amount
                self.__currancy = currancy

            def set__ammount(self, new_mount):
                try:
                    self.__amount = new_mount
                except Exception as err:
                    print(err)

            def show_info(self):
                print("Card number: ", self.__card_number, "\nAmount: ",
                      self.__amount, "\nCurrancy", self.__currancy)
                amount = int(input("Enter your money: "))
                currancy = input("Enter currancy: UAH, USD, EUR")
                card_number = randint(0000000000, 9999999999)
                credit_card = Account(card_number, amount, currancy)
                credit_card.show_info()



