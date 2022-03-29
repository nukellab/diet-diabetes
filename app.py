
# importing the necessary dependencies
from flask import Flask, render_template, request,jsonify
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__) # initializing a flask app

@app.route('/',methods=['GET'])  # route to display the home page
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/predict',methods=['POST','GET']) # route to show the predictions in a web UI
@cross_origin()
def index():
    if request.method == 'POST':
        try:
            #  reading the inputs given by the user
            FBST = float(request.form['FBST'])
            GTS = float(request.form['GTS'])
            RBST = float(request.form['RBST'])
            BMI = float(request.form['BMI'])
            Age = float(request.form['Age'])
            Cholesterol =float(request.form['Cholesterol'])
            Sodium = float(request.form['Sodium'])
            red_meat = float(request.form['red_meat'])
            fried_fish = float(request.form['fried_fish'])
            Refined_sugar = float(request.form['Refined_sugar'])
            wine_alcohol = float(request.form['wine_alcohol'])
            beer_alcohol = float(request.form['beer_alcohol'])
            proof_spirit_80percent = float(request.form['proof_spirit_80percent'])

            filename = 'Dibetes_Test_Diet_Day_RF.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage
            # predictions using the loaded model file
            prediction=loaded_model.predict([[FBST,GTS,RBST,BMI,Age,Cholesterol,Sodium,red_meat,fried_fish,Refined_sugar,wine_alcohol,beer_alcohol,proof_spirit_80percent]])
            print('prediction is', prediction)
            # showing the prediction results in a UI
            return render_template('results.html',prediction=round(100*prediction[0]))
        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'
    # return render_template('results.html')
    else:
        return render_template('index.html')



if __name__ == "__main__":
	app.run(debug=True) # running the app