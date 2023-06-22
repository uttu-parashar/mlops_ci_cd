def main(args):
    # read data
    train_data = get_data(args.training_data)
    test_data = get_data(args.test_data)
    
    train_labels = train_data["Diabetic"]
    train_data = train_data.drop('Diabetic', axis=1)
    
    test_labels = test_data["Diabetic"]
    test_data = test_data.drop('Diabetic', axis=1)


    # evaluate model
    eval_model(model, train_data, train_labels, test_data, test_labels)

# function that reads the data
def get_data(path):
    print("Reading data...")
    df = pd.read_csv(path)
    
    return df


def eval_model(model, train_data, train_labels, test_data, test_labels):
    
    
    predicted_train_labels = model.predict(train_data)
    accuracy_score_ = accuracy_score(train_labels,predicted_train_labels)
    print("Train Accuracy_score is :",np.round(accuracy_score_,3),"\n","-"*40)
    recall_score_ = recall_score(train_labels,predicted_train_labels)
    print("Train Recall_score_ is :",np.round(recall_score_,3),"\n","-"*40)
    f1_score_ = f1_score(train_labels,predicted_train_labels)
    print("Train f1_Score is :",np.round(f1_score_,3),"\n","-"*40)
    
    predicted_test_labels = best_knn.predict(test_data)
    accuracy_score_ = accuracy_score(test_labels,predicted_test_labels)
    print("Test_Accuracy_score is :",np.round(accuracy_score_,3),"\n","-"*40)
    recall_score_ = recall_score(test_labels,predicted_test_labels)
    print("Test Recall_score_ is :",np.round(recall_score_,3),"\n","-"*40)
    f1_score_ = f1_score(test_labels,predicted_test_labels)
    print("Test_f1_Score is :",np.round(f1_score_,3),"\n","-"*40)
    
    
    
    
def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--training_data", dest='training_data',
                        type=str)
    parser.add_argument("--test_data", dest='test_data',
                        type=str)
    
    parser.add_argument("--model", dest='model',
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
    
    

