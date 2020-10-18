import mlflow

if __name__ = "__main__":
    mlflow.set_experiment(experiment_name='projet62')
    with mlflow.start_run()

    mlflow.log_param('a', 1)
    mlflow.log_metric('b', 2)