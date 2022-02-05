<!-- vim-markdown-toc -->

## Folder structure
    ├── backend                             # backend 
        ├── app                             # django project
        ├── core                            # core app for models
        ├── dashboard                       # App for templates, prediction and logs
        ├── leaning                         # testing and learning for final dashboard
        └── Dockerfile                      # Django Dockerfile
    ├── tf-server                           # Custom tensorflow/serving image
    └── docker-compose.yml                  # Runs Everything
    

## APP

## Docker

Docker build command for tf-serve
```bash
docker build -t tensorflow-serving ./tf-serve
```
Docker run command for tf-serve
```bash
docker run --name tensorflow-serving -h 0.0.0.0 --network="host" --rm -d tensorflow-serving:latest
```
Sample Url
```bash
http://localhost:8501/v1/models/linear_model:predict
```