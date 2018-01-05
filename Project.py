from flask import Flask, render_template, request, redirect, url_for,session
from wtforms import Form, StringField, PasswordField, validators

import User_Information

app = Flask(__name__)

class Account(Form) :
    Login = StringField("NRIC :",[validators.Length(min=9,max=9),validators.required()])
    Password = PasswordField("Password :",[validators.required()])

@app.route('/Login', methods=['GET','POST'])
def Login():
    form = Account(request.form)
    if request.method == 'POST' and form.validate():
        check = User_Information.check_user(form.Login.data, form.Password.data)
        if check == True:
            return redirect(url_for('info'))
    return render_template('Login.html', form=form)

@app.route('/account')
def info():
    acc = []
    acc = User_Information.Acc()
    return render_template('acc_info.html',acc_info=acc)

if __name__ == '__main__':
    app.run()
