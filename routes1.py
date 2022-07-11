
from django.shortcuts import render
import flask
from flask import Flask, render_template
from flask import request
from flask import session
from flask import redirect
from flask import url_for
import main
from main import f
from main import lines


app=Flask(__name__)

def valid_login(x,y):
    x=str(x)+'\n'
    y = str(y)+'\n'
    if str(x) in main.lines:
        if str(y) in main.lines:
            return 1

def get_name_1(xyxy):
    xxuu = str(xyxy)+'\n'
    x=0
    while x < len(main.lines):
        if xxuu == main.lines[x]:
            return(main.lines[x+2])
        else:
            x = x+3
    return 0
@app.route("/", methods ={'POST','GET'})
def login():
    
    if request.method=='POST':
        if request.form['username']:
            if valid_login(request.form['username'],request.form['password']):
                xxoo = get_name_1(request.form['username'])
                xty = len(lines)
                lines[xty-1] = lines[xty-1]+'\n'
                return render_template('main.html',value1=xxoo,value2=lines)

            

    return render_template('main.html',value1=0)
app.run()
