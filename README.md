# MLflow practice

## High Level Architecture

<img width="1291" alt="mlflow" src="https://user-images.githubusercontent.com/97444802/159104126-4d5b322e-8ebf-4622-86a9-9843dd385d9e.png">

## List all models

```bash
export MLFLOW_TRACKING_URI=databricks
```

```python
python list_model.py
```
![gcp_list_model](https://user-images.githubusercontent.com/97444802/159104675-c9233860-5240-44b9-919a-decc90233887.png)

## Download model
Generate an access token in databricks workspace instance and export into the cloud environment. 
```bash
export DATABRICKS_TOKEN=<my_databricks_token>
```
```python
python predict_fake_news.py
```
![gcp_predict_test](https://user-images.githubusercontent.com/97444802/159104507-e6b3ad24-4008-4b8f-82c6-f9b695aa450e.png)

## Run FastAPI
```python3
python main.py
```
![fast_api](https://user-images.githubusercontent.com/97444802/159104856-ae69fe20-6b20-4886-9bcd-7d6df66a1a08.png)

![fastapi_response](https://user-images.githubusercontent.com/97444802/159104872-7938a29d-1a4f-413b-ba09-17e21fbdc816.png)

