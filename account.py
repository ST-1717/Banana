class Account():
    def __init__(self,id,acc_num,type):
        self.__id = id
        self.__acc_num = acc_num
        self.__amount = 0
        self.__type = type

    def get_acc_num(self):
        return self.__acc_num
    def get_amount(self):
        return self.__amount
    def get_type(self):
        return self.__type
    def get_id(self):
        return self.__id

    def set_amount(self,amount):
        self.__amount = amount

    def withdraw(self,amt):
        if self.__amount<=amt:
            self.__amount -= amt

    def deposit(self,amt):
        if amt>0:
            self.__amount += amt
