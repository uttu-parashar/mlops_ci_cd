import argparse
import pandas as pd
from sklearn.model_selection import train_test_split



# function that splits the data
def split_data(df):
    X, y = df[['Pregnancies','PlasmaGlucose','DiastolicBloodPressure','TricepsThickness',
    'SerumInsulin','BMI','DiabetesPedigree','Age']].values, df['Diabetic'].values

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

    return X_train, X_test, y_train, y_test

def main(args):
    # read data
        # read data
    df = get_data(args.training_data)

    # split data
    X_train, X_test, y_train, y_test = split_data(df)
    print("Shape of x_train is :",X_train.shape)
    print("Shape of X_test is :",X_test.shape)
    print("Shape of y_train is :",y_train.shape)
    print("Shape of y_test is :",y_test.shape)
    
    X_train["Diabetic"] = y_train
    X_test["Diabetic"] = y_test
    
    X_train.to_csv("output_dir"+"/"+"training_data.csv",index = False)
    X_test.to_csv("output_dir"+"/"+"test_data.csv",index = False)
    

# function that reads the data
def get_data(path):
    df = pd.read_csv(path)
    
    return df

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--input_data", dest='input_data',
                        type=str)
    parser.add_argument("--output_dir", dest='output_dir',
                        type=str)
    

    # parse args
    args = parser.parse_args()

    # return args
    return args

# run script
if __name__ == "__main__":

    # parse args
    args = parse_args()

    # run main function
    main(args)