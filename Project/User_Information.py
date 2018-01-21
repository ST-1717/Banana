from account import Account
from account import transaction_data
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
    for acc in acc_file:
        list = acc.split(',')
        s = Account(list[0], list[1], list[2],list[3])
        s.set_amount(total_amts(list[1]))
        accList.append(s)
    acc_file.close()
    return accList

def total_amts(acc_num):
    amount = open('file/amount.txt','r')
    for a in amount :
        amt = a.split(",")
        if acc_num == amt[2][:-1]:
            if amt[0] == datetime.datetime.now().strftime("%b"):
                return float(amt[1])
    amount.close()

def UserName(id) :
    user_file = open('file/users.txt', 'r')
    for user in user_file :
        list_u = user.split(",")
        if id == list_u[0]:
            return list_u[2]
    user_file.close()

def get_months():
    month = []
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    now = datetime.datetime.now().strftime("%b")
    month.append(now)
    index = months.index(now)
    for i in range(4):
        index -= 1
        month.append(months[index])
    return month

def month_amt(acc_num):
    amount = open('file/amount.txt','r')
    for a in amount :
        amt = a.split(",")
        if acc_num == amt[2][:-1]:
            if amt[0] == datetime.datetime.now().strftime("%b"):
                return float(amt[1])
    amount.close()

def get_amount_month(acc,month):
    amount_month = []
    amount = open('file/amount.txt', 'r')
    for a in amount:
        amt = a.split(",")
        if acc == amt[2][:-1]:
            for i in month :
                if i == amt[0] :
                    amount_month.append(str(amt[1]))
    amount.close()
    return amount_month

def get_transaction(acc,month):
    data = []
    info = open('file/transaction.txt', 'r')
    for i in info :
        tran = i.split(",")
        if acc == tran[0]:
            if month == tran[1] :
                tran_data = transaction_data(tran[0],tran[1],tran[2],tran[3][:-1])
                data.append(tran_data)
    info.close()
    return data

def make_transaction(acc_num, amount, type, acc_info):
    for acc in acc_info:
        first_amt = acc.get_amount()
        if acc.get_acc_num() == acc_num:
            if type == "deposit":
                total_amount = acc.deposit(amount)
                amt = open("file/amount.txt", "r")
                lines = amt.readlines()
                amt.close()
                f = open("file/amount.txt", "w")
                for i in lines:
                    if i != datetime.datetime.now().strftime("%b")+','+str(first_amt)+','+acc_num+"\n":
                        f.write(i)
                f.close()
                add = open("file/amount.txt", "a")
                add.write(datetime.datetime.now().strftime("%b") + "," + str(total_amount) + "," + acc_num + "\n")
                add.close()
                trans = open("file/transaction.txt", "a")
                trans.write(acc_num + "," + datetime.datetime.now().strftime("%b") + "," + str(amount) + "," + type + "\n")
                trans.close()
                return "Transaction Success"
            else:
                total_amount = acc.withdraw(amount)
                amt = open("file/amount.txt", "r")
                lines = amt.readlines()
                amt.close()
                f = open("file/amount.txt", "w")
                for i in lines:
                    if i != datetime.datetime.now().strftime("%b") + ',' + str(first_amt) + ',' + acc_num + "\n":
                        f.write(i)
                f.close()
                add = open("file/amount.txt", "a")
                add.write(datetime.datetime.now().strftime("%b") + "," + str(total_amount) + "," + acc_num + "\n")
                add.close()
                trans = open("file/transaction.txt","a")
                trans.write(acc_num+","+datetime.datetime.now().strftime("%b")+","+str(amount)+","+type+"\n")
                trans.close()
                return "Transaction Success"
    return "Transaction Fail , Please Try Again"
