from azure.ai.ml.entities import ManagedOnlineDeployment, CodeConfiguration           
import argparse


def main(args):
    # read data
    model = Model(path="./model")

    blue_deployment = ManagedOnlineDeployment(
        name="blue",
        endpoint_name="endpoint-example",
        model=model,
        environment="deployment-environment",
        code_configuration=CodeConfiguration(
            code="./src", scoring_script="score.py"
        ),
        instance_type="Standard_DS2_v2",
        instance_count=1,
    )

    ml_client.online_deployments.begin_create_or_update(blue_deployment).result()


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