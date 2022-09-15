
import re
from flask import Flask,render_template,request,redirect,url_for
from matplotlib.pyplot import table
import mysql.connector as c
import pandas as pd
import database as db
con = c.connect(host = "localhost",user = "root",password = "honeychandu",database = 'project')
cursor = con.cursor()
app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def home():
    if request.method == 'GET':
        data = db.show() 
        return render_template("table.html",table = data)
    if request.method == 'POST':
        percentage = request.form['criteria']
        data = db.showPercentage(percentage)        
        return render_template('table.html',table = data)


   
if __name__ =='__main__':
    app.run(port =5000,debug =True)
    print("welcome!!!!!!!!")