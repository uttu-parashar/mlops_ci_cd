import argparse
from azure.ai.ml.entities import Environment


def main(args):
    # read data
    env = Environment(
        image="mcr.microsoft.com/azureml/openmpi3.1.2-ubuntu18.04",
        conda_file=args.conda_ml_file,
        name=args.env_name,
        description="Environment created from a Docker image plus Conda environment.",
    )
    ml_client.environments.create_or_update(env)


def parse_args():
# setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--conda_yml_file", dest='conda_yml_file',
                        type=str)
    parser.add_argument("--env_name", dest='env_name',
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