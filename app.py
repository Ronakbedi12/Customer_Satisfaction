from flask import Flask,render_template,url_for,request
import joblib
import pandas as pd

model=joblib.load('LogisticRegression.lb')
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/prediction',methods=["GET","POST"])
def prediction():
    if request.method=="POST":
        age=int(request.form['Enter_age'])
        distance=int(request.form['Flight_distance'])
        entertainment=int(request.form['Inflight_entertainment'])
        bag_handling=int(request.form['Baggage_handling'])
        cleanliness=int(request.form['Cleanliness'])
        departure_delay=int(request.form['Departure_delay_in_minutes'])
        arival_delay=int(request.form['Arrival_delay_in_Minutes'])
        gender=request.form['Gender']
        customer_type=request.form['Customer_type']
        travel_type=request.form['Travel_type']
        travel_class=request.form['Travel_class']
       
        a=0
        b=0
        c=0
        d=0
        e=0
        if gender=="Male":
            a=1
        if customer_type=="Disloyal":
            b=1
        if travel_type=="Personal":
            c=1   
        if travel_class=="Eco":
            d=1
        if travel_class=="Eco-Plus":
            e=1         


        all_data=[[age,distance,entertainment,bag_handling,cleanliness,departure_delay,arival_delay,a,b,c,d,e]]
        df=pd.DataFrame(all_data)
        pred=model.predict(df)
        
        if pred==[1]:
            return "Satisfied"
        else:
            return "Not Satisfied"

if __name__=="__main__":
    app.run(debug=True)
    