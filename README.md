<!-- vim-markdown-toc -->

## Folder structure
    ├── app                                 # Django app
        ├── core                            # core app for models
        ├── logging                         # logging and prediction 
        └── Dockerfile                      # Django Dockerfile
    ├── tf-server                           # Custom tensorflow/serving image
    └── docker-compose.yml                  # Runs Everything
    

## APP

## Docker

Docker build command for tf-serve
```bash
docker build -t object-detect ./tf-serve
```
Docker run command for tf-serve
```bash
docker run --name object-detect -h 0.0.0.0 --network="host" --rm -d object-detect:latest
```
Sample Url
```bash
http://localhost:8501/v1/models/linear_model:predict
```