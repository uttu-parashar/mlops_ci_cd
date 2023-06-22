import argparse
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes



def main(args):
    # read data
    file_model = Model(
        path=args.model_path,
        type=AssetTypes.CUSTOM_MODEL,
        name=args.model_name,
        description="Model created from local file.",
    )
    ml_client.models.create_or_update(file_model)


def parse_args():
# setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--model_path", dest='model_path',
                        type=str)
    parser.add_argument("--model_name", dest='model_name',
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