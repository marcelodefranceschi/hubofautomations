from flask import Flask, render_template, url_for, send_file, request, flash, redirect
from forms import FormLogin, FormSign_up
from flask_sqlalchemy import SQLAlchemy
import subprocess

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c87debc2de2f48486ec7b8e1d1229583'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

database = SQLAlchemy(app)


@app.route('/')
def Index():
    return render_template("Index.html")

@app.route('/A358')
def A358():
    return render_template("A358.html")

@app.route('/A303')
def A303():
    return render_template("A303.html")

@app.route('/A417')
def A417():
    return render_template("A417.html")

@app.route('/Automations')
def Automations():
    return render_template("Automations.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    if form_login.validate_on_submit() and 'login_submit_button' in request.form:
        flash(f'Succesful login for {form_login.email.data}', 'alert-success')
        return redirect(url_for('Automations'))
    return render_template("login.html", form_login=form_login)


@app.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    form_sign_up = FormSign_up()
    if form_sign_up.validate_on_submit() and 'sign_up_submit_button' in request.form:
        flash(f'Succesful account created for {form_sign_up.email.data}', 'alert-success')
        return redirect(url_for('login'))
    return render_template("sign_up.html", form_sign_up=form_sign_up)



@app.route('/Month_endA358')
def Month_endA358():
    return render_template("Month_endA358.html")





@app.route('/PaymentsA358')
def PaymentsA358():
    return render_template("PaymentsA358.html")




@app.route('/TDR_FY')
def run_script():
    file = open(r'C:\Users\marcelo.defranceschi\OneDrive - Mace\Desktop\Projetos Python\PYTHON_files\TDR_FY.py', 'r').read()
    return exec(file)

@app.route('/TDR_FY/')
def TDR_FY():
    print('Button clicked!')
    try:
        subprocess.run(['python', r'C:\Users\marcelo.defranceschi\OneDrive - Mace\Desktop\Projetos Python\PYTHON_files\TDR_FY.py'])
        return 'Script executed successfully.'
    except Exception as e:
        return f'Error executing script: {str(e)}'


@app.route('/Oracle_forecast/')
def Oracle_forecast():
    print('Button clicked!')
    try:
        subprocess.run(['python', r'C:\Users\marcelo.defranceschi\OneDrive - Mace\Desktop\Projetos Python\PYTHON_files\Oracle_forecast_by_task2.py'])
        return 'Script executed successfully.'
    except Exception as e:
        return f'Error executing script: {str(e)}'


@app.route('/PRISM_opening/')
def PRISM_opening():
    print('Button clicked!')
    try:
        subprocess.run(['python',r'C:\Users\marcelo.defranceschi\OneDrive - Mace\Desktop\Projetos Python\PYTHON_files\Opening_PRISM.py'])
        return 'Script executed successfully.'
    except Exception as e:
        return f'Error executing script: {str(e)}'


@app.route('/CEMAR_opening/')
def CEMAR_opening():
    print('Button clicked!')
    try:
        subprocess.run(['python',r'C:\Users\marcelo.defranceschi\OneDrive - Mace\Desktop\Projetos Python\PYTHON_files\Opening_CEMAR.py'])
        return 'Script executed successfully.'
    except Exception as e:
        return f'Error executing script: {str(e)}'




if __name__ == "__main__":
    app.run(debug=True)
