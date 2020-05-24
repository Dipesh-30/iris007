# -*- coding: utf-8 -*-
"""
Created on Sat May 23 19:28:40 2020

@author: Priyanshi
"""
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def add():
    a = request.args.get("a")
    b = request.args.get("b")
    
    return str(int(a) + int(b))

if __name__=='__main__':
    app.run()
