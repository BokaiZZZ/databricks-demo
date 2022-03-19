from mlflow.store.artifact.models_artifact_repo import ModelsArtifactRepository
from mlflow.tracking import MlflowClient

# model_uri = MlflowClient.get_model_version_download_uri('best_fake_new_predict_model', '1')
# ModelsArtifactRepository(model_uri).download_artifacts(artifact_path="")
client = MlflowClient()
my_model = client.download_artifacts("edf8055f04ec4a189c884e2bf18ddea9", path="model")
print(f"Placed model in: {my_model}")