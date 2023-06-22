import argparse
import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

def main(args):
    # read data
    df = get_data(args.training_data)
    
    Y_train = df["Diabetic"]
    X_train = df.drop('Diabetic', axis=1)

    # train model
    model = train_model(args.reg_rate, X_train, y_train)
    
    # now you can save it to a file
    with open(str(args.output_dir)+"/"+"model.pkl', 'wb') as f:
        pickle.dump(model, f)

    
# function that reads the data
def get_data(path):
    print("Reading data...")
    df = pd.read_csv(path)    
    return df


# function that trains the model
def train_model(reg_rate, X_train,y_train):
    print("Training model...")
    model = LogisticRegression(C=1/reg_rate, solver="liblinear").fit(X_train, y_train)

    return model


def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--training_data", dest='training_data',
                        type=str)
    parser.add_argument("--reg_rate", dest='reg_rate',
                        type=float, default=0.01)
    
    parser.add_argument("--output_dir", dest='output_dir',
                        type=str)

    # parse args
    args = parser.parse_args()

    # return args
    return args

# run script
if __name__ == "__main__":
    # add space in logs
    print("\n\n")
    print("*" * 60)

    # parse args
    args = parse_args()

    # run main function
    main(args)

    # add space in logs
    print("*" * 60)
    print("\n\n")
