from flask import Flask,render_template,request,redirect, url_for, session, flash
import mysql.connector
app = Flask(__name__)

@app.route("/logout")
def logout():
    name = ''
    id= ''
    msg = 'Looged Out Sucessfully'
    return render_template('login.htm', msg=msg,name=name,id-id)
    
@app.route('/login', methods=['GET','POST'])
def login():
    msg=''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
username = request.form['username']
password = request.form['password']
mydb = mysql. connector.connect(
host='127.0.0.1',
user='root',
password='4272',
database='Login'
)
mycursor = mydb.cursor()
mycursor.execute('SELECT * FROM LoginDetails WHERE username = % AND password = %s', (username, password))
account = mycursor.fetchone()
else:
if account:
print('login success')
name = account[1]
id = account[0]
msg = 'Logged in Successfully'
print('login successful')
return render_template('welcome.html', msg-msg, name-name, id-id)

else:

msg = 'incorrect Credentials. Kindly check'
return render_template('login.html', msg=msg)
return render_template('login.html')
app.run(debug-True)
return (render)
@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and username in request.form and password
in request.form and email in request.form:
   username = request.form['username']
   password = request.form['password']
   email = request.form['email']
   mydb = mysql.connector.connect(
   host='remoteysql.com',
   user='Rz8hqnlk4',
   password='nd6wK03xe0',
   database='Rz8hqnlk4'
)
mycursor = mydb.cursor()
print(username)
mycursor.execute('SELECT * FROM LoginDetails WHERE Name = %s AND')
account = mycursor.fetchone()
print(account)
if account:
    msg = 'Account already exists! Please Login'
elif not re.match(r'^[^\d]*@[^\d]*\.\.[^\d]*$', email):
    msg = 'Invalid email address!'
elif not re.match(r'(A-Za-z0-9)+', username):
    msg = 'Username must contain only characters and numbers!'
elif not username or not password or not email:
    msg - 'Kindly fill the details!'
else:
    mycursor.execute('INSERT INTO LoginDetails VALUES (NULL, %s, %s, %s)',
 (username, password, email))
    mydb.commit()
    msg = 'Your Regestration is Sucessful'
    name = username
    return render_template('index.html',msg=msg, name=name)
elif request.method == 'POST':
msg = 'Kindly fill the details!'
return render_template('regestration.html', msg=msg)
