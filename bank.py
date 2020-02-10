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
input("Press enter to continue....")

card_case = {}


class Account:
    def __init__(self, card_number, amount, currancy, name):
        self.__card_number = card_number
        self.__amount = amount
        self.__currancy = currancy
        self.name = name

    def set__ammount(self, new_mount):
        try:
            self.__amount = new_mount
        except Exception as err:
            print(err)

    def add_ammount(self, add_money):
        self.__amount = self.__amount + add_money

    def out_ammount(self, check_out):
        if self.__amount >= check_out:
            self.__amount = self.__amount - check_out
            print("З вашого рахунку було списано: ", check_out,self.__currancy)
            input("Press enter to continue...")

        else:
            print("\t\t---Не достатьно коштів на рахунку---\n\t\tмаксимальна сума для зняття: ", self.__amount,self.__currancy)
            input("Press enter to continue...")

    def show_info(self):
        print("\t\t----", self.name.title(), "----\nCard number: ", self.__card_number, "\nAmount: ",
              self.__amount, "\nCurrancy", self.__currancy)


while True:
    print("""
          ---- MENU ----
          press 1 to create new Account
          press 2 to enter some money to your Account
          press 3 to check out from your Account
          press 4 to show info
          press 0 to exit..
          """)

    try:
        menu_cheker = int(input())
        if menu_cheker == 0:
            try:
                print("You has left =(")
                input()
                break
            except Exception as err:
                print(err)
        elif menu_cheker == 1:
            print("\t\t---- NEW ACCOUNT ----")
            print("Enter name of your new Account")
            new_mount = str(input())
            amount = int(input("Enter your money: "))
            currancy = input("Enter currancy: UAH, USD, EUR: ")
            card_number = randint(0000000000, 9999999999)
            credit_card = Account(card_number, amount, currancy, new_mount)
            

        elif menu_cheker == 2:
            print("""
            \t\t----How many money you wont to add?----
            """)
            new_balance = int(input("Enter your money: "))
            credit_card.add_ammount(new_balance)
            
        elif menu_cheker == 3:
            print("""
            \t\t----How many money you wont to check out?----
            """)
            check_out = int(
                input("Enter how match money you want to check out: "))
            credit_card.out_ammount(check_out)
            
        elif menu_cheker == 4:
            credit_card.show_info()
    except Exception as err:
        print("SOMTHING GOING WRONG", err)
