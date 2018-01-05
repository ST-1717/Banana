from account import Account
import datetime

def check_user(id, password):
    user_file = open('file/users.txt', 'r')
    for ulist in user_file:
        list_u = ulist.split(",")
        if list_u[0] == id and list_u[1] == password:
            return True
    user_file.close()
    return False

def Acc():
    accList = []
    acc_file = open('file/account.txt', 'r')
    for ulist in acc_file:
        list = ulist.split(',')
        s = Account(list[0], list[1], list[2])
        s.set_amount(total_amts(list[1]))
        accList.append(s)
    return accList

def total_amts(acc_num):
    amount = open('file/amount.txt','r')
    for a in amount :
        amt = a.split(",")
        if acc_num == amt[2][:-1]:
            if amt[0] == datetime.datetime.now().strftime("%b"):
                return int(amt[1])


