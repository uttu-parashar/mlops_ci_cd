import json
import pickle
import numpy as np
import os

# called when the deployment is created or updated
def init():
    global model
    # get the path to the registered model file and load it
    model_path = os.path.join(os.getenv('AZUREML_MODEL_DIR'), 'model.pkl')
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

# called when a request is received
def run(raw_data):
    
    data = json.loads(raw_data)['data']
    np_data = np.array(data)
    
    predictions = model.predict(np_data)
    
    
    log_text = 'Data:' + str(data) + ' - Predictions:' + str(predictions)
    print(log_text)
    

    classnames = ['not-diabetic', 'diabetic']
    predicted_classes = []
    for prediction in predictions:
        predicted_classes.append(classnames[prediction])
    # Return the predictions as JSON
    return json.dumps(predicted_classes)