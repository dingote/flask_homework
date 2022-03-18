from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
   return render_template('home.html')

@app.route('/signup/')
def signup_form():
   return render_template('signup_form.html')

@app.route('/guardando',methods = ['POST', 'GET'])
def guardando():
   if request.method == 'POST':
      try:
         name = request.form['name']
         email = request.form['email']
         password = request.form['password']

         with sqlite3.connect("users.db") as conn:
            c = conn.cursor()
            sentencia="INSERT INTO user (name,mail,password) VALUES (\""+name+"\", \""+email+"\", \""+password+"\")"
            c.execute(sentencia)
            conn.commit()

      except:  ##Si se da un error
          print('error')
          conn.rollback()

      
      finally:
         return render_template("home.html")
         conn.close()

@app.route('/datos')
def datos():
   conn = sqlite3.connect("users.db")
   conn.row_factory = sqlite3.Row
   
   c = conn.cursor()
   c.execute("select * from user")
   
   rows = c.fetchall(); 
   return render_template("lista.html",rows = rows)

if __name__ == '__main__':
    app.run()
