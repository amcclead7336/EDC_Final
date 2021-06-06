import json

from flask import Flask, request
# TO generate UI for sending request via browser
from flasgger import Swagger
import pickle5 as pickle
import pandas as pd

with open("model_config.json", 'r') as file:
    config_json = json.load(file)

# Load model from file - read mode

model_directory = config_json["model_directory"]
with open(f"../{model_directory}/model.pkl", 'rb') as file:
    tm_model = pickle.load(file)

app = Flask(__name__)

# Enable this app for swagger and it will auto generate UI
swagger = Swagger(app)


@app.route('/bca_model_file', methods=['POST'])
def predict_y_file():
    # BELOW docstring lines are required to support swagger documentation
    """ Endpoint returning Breast Cancer prediction
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: true
    """
    columns = ["age", "job", "marital", "education", "default", "housing", "loan", "contact", "month", "day_of_week",
               "duration",
               "campaign", "pdays", "previous", "poutcome", "emp.var.rate", "cons.price.idx", "cons.conf.idx",
               "euribor3m", "nr.employed"]

    # Create a test dataframe to use for prediction - Column name has to be SAME as training set
    df_tm = pd.read_csv(request.files["input_file"])
    df_tm = df_tm[columns]
    print("-------- PD Dataframe for prediction: -------\n", df_tm)

    for i, classmap_individual in enumerate(config_json["classmap"], 1):
        print(i, classmap_individual)

        if i == 10:
            i = 14

        print(df_tm.iloc[0, i])

        df_tm.iloc[0, i] = classmap_individual.index(df_tm.iloc[0, i])

    # Make prediction using the input data
    prediction = tm_model.predict(df_tm)
    if prediction[0] == 0:
        re = "No"

    else:
        re = "Yes"
    print("Debug: Prediction: ", re)

    # Send the prediction as response - will need to convert number to string
    return re


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5010)
