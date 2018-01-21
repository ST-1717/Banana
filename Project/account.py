class Account():
    def __init__(self,name,acc_num,type,date):
        self.__name = name
        self.__acc_num = acc_num
        self.__amount = 0.0
        self.__type = type
        self.__date = date

    def get_acc_num(self):
        return self.__acc_num
    def get_amount(self):
        return self.__amount
    def get_type(self):
        return self.__type
    def get_name(self):
        return self.__name
    def get_date(self):
        return self.__date

    def set_amount(self,amount):
        self.__amount = amount

    def withdraw(self,amt):
        if self.__amount >= amt:
            self.__amount -= amt
            return self.__amount

    def deposit(self,amt):
        if amt > 0:
            self.__amount += amt
            return self.__amount

class transaction_data():
    def __init__(self,acc_num,month,amount,type):
        self.__acc_num = acc_num
        self.__month = month
        self.__amount = amount
        if type == "withdraw" or type == "deposit" :
            self.__type = type

    def get_acc_num(self):
        return self.__acc_num
    def get_month(self):
        return self.__month
    def get_amount(self):
        return self.__amount
    def get_type(self):
        return self.__type
