
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def form():
    return render_template('calculator.html',name=None,bmi=None)
    
@app.route('/calculate',methods=['POST'])
def bmi():
    name = request.form['name']
    weight= float(request.form['weight'])
    height= float(request.form['height'])
    
    height=height/100
    bmi=round(weight/(height*height),2)
     
    return render_template('calculator.html',
                            name=name,
                            bmi=bmi)
                           
                           
if __name__=='__main__':
    app.run(debug=True)