from flask import Flask,render_template,request,redirect
import pickle
import numpy as np

model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict_customer_churn():
    accountlength=float(request.form.get("accountlength"))
    numbervmailmessages=float(request.form.get("numbervmailmessages"))
    totaldayminutes=float(request.form.get("totaldayminutes"))
    totaldaycalls=float(request.form.get("totaldaycalls"))
    totaldaycharge=float(request.form.get("totaldaycharge"))
    totaleveminutes=float(request.form.get("totaleveminutes"))
    totalevecalls=float(request.form.get("totalevecalls"))
    totalevecharge=float(request.form.get("totalevecharge"))
    totalnightminutes=float(request.form.get("totalnightminutes"))
    totalnightcalls=float(request.form.get("totalnightcalls"))
    totalnightcharge=float(request.form.get("totalnightcharge"))
    totalintlminutes=float(request.form.get("totalintlminutes"))
    totalintlcalls=float(request.form.get("totalintlcalls"))
    totalintlcharge=float(request.form.get("totalintlcharge"))
   
   

    
    
    
    result=model.predict(np.array([[accountlength,numbervmailmessages,totaldayminutes,totaldaycalls,totaldaycharge,totaleveminutes,totalevecalls,totalevecharge,totalnightminutes,totalnightcalls,totalnightcharge,totalintlminutes,totalintlcalls,totalintlcharge]]))
    
    if result[0]=="No":
        return "<h1 style='color:green'>CHURN</h1>"
    else:
        return "<h1 style='color:red'>NOT CHURN</h1>"
    

app.run(host='0.0.0.0',port=8080)