from flask import Flask, render_template, request, redirect, url_for,session
from wtforms import Form, StringField, PasswordField, validators ,SelectField,FloatField

import User_Information

app = Flask(__name__)

class Account(Form) :
    Login = StringField("NRIC :",[validators.Length(min=9,max=9),validators.required()])
    Password = PasswordField("Password :",[validators.required()])

class Transactions(Form) :
    amount = FloatField("Amount :",[validators.required()],default="0.0")
    type = SelectField('Type of transaction :', [validators.DataRequired()],choices=[('', 'Select'), ('withdraw', 'Withdraw'),('deposit','Deposit')], default='')


@app.route('/Login', methods=['GET','POST'])
def Login():
        form = Account(request.form)
        if request.method == 'POST' and form.validate():
            check = User_Information.check_user(form.Login.data, form.Password.data)
            if check == True:
                session["Username"] = User_Information.UserName(form.Login.data)
                return redirect(url_for('info'))
        return render_template('Login.html', form=form)

@app.route('/account',methods=['GET','POST'])
def info():
    acc = []
    acc = User_Information.Acc()
    month = User_Information.get_months()
    select = request.form.get('comp_select')
    amount_month = User_Information.get_amount_month(select,month)
    total_months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_select = request.form.get("month_select")
    data = User_Information.get_transaction(select,month_select)
    return render_template('acc_info.html',acc_info=acc,name = session['Username'],months=month,amount_month = amount_month,total_months = total_months,data=data)

@app.route('/transaction',methods=['GET','POST'])
def transaction():
   form = Transactions(request.form)
   acc = User_Information.Acc()
   if request.method == 'POST' and form.validate():
        select = request.form.get('comp_select')
        make_trans = User_Information.make_transaction(select,form.amount.data,form.type.data,acc)
        return render_template('transactions.html', form=form, name=session['Username'], acc_info=acc,make_trans=make_trans)
   return render_template('transactions.html',form=form,name=session['Username'], acc_info=acc)


@app.route('/logout')
def logout():
   session.pop('Username', None)
   return redirect(url_for('Login'))

if __name__ == '__main__':
    app.secret_key = 'secret123'
    app.run()
