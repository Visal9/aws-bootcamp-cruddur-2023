# Week 1 — App Containerization

## Installing Docker Extension in Gitpod

Install Docker extension on your Gitpod environment: mouse right click → go to “view” → go to extensions → write in search “Docker” → click “install”. Using this extension we can easily manage docker containers.

<p align="center">
<img align="center"  src="./images/docker-vs-extention.png" alt="docker-extension">
</p>

![installing-extension](./images/vs-docker-extwntion-install.png)

## Containerizing Backend of the app
#### Write backend docker file
 In backend folder I create [Dockerfile](https://github.com/Visal9/aws-bootcamp-cruddur-2023/blob/main/backend-flask/Dockerfile) which gives instruction to docker how to create docker image for backend app:
 

 ```
 # pull in the base image
FROM python:3.12.0a5-slim

# set the working directory of the container (aka guest operating system) - make a new folder(?)
WORKDIR /backend-flask

# copy requirement file from host to container
COPY requirements.txt requirements.txt

# inside container, run installation of python libraries
RUN pip3 install -r requirements.txt

# copy files from host to container - . refers to everything in current directory to container directory
# first period - everything outside container
# second period - everything inside container
COPY . .

# set environment variables - inside the container - remain set when container is running
ENV FLASK_ENV=development

EXPOSE ${PORT}

# command to run flask
# python3 -m flask run --host=0.0.0.0 --port=4567
# 0.0.0.0 known as the 'everything address'
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=4567"]

```

Before build docker image I make sure my python app run locally without any issue 

##### Now, lets try this configuration manually in our environment:

1- Go to /backend-flask

2- Run “pip3 install -r requirements.txt”

![install-app](./images/backend-manual-install.png)

3- ```export FRONTEND_URL="*"```   ```export BACKEND_URL="*"``` we have to set these env variables otherwise backend app won't work

 4- Run App by running ```python3 -m flask run --host=0.0.0.0 --port=4567``` command

![run-app](./images/backend-run-app.png)

5- check port tab and see whether port 4567 is open ad make sure that is available publicly by clicking lock icon and under state in shows as ```open(public)```

![port-open](./images/backend-port-rnng-with-highligt.png)

6- 6- Click  the link address and add this part to end of the  URL ```/api/activities/notifications``` and refresh then we will see the following:
![backend-response](./images/backend-responce.png)


### Build Docker Image from Docker File

1. Make sure that you are in (/aws-bootcamp-cruddur-2023) directory
2. Run this command ```docker build -t backend-flask ./backend-flask```

![docker-build](./images/docker-build-terminal.png)

3. We can see our image is built
<p align="center">
<img align="center"  src="./images/backend-docker-image.png" alt="docker-extension">
</p>

<p align="center">
<img align="center"  src="./images/docker-images-command-output.png" alt="docker-extension">
</p>



### Create a container using our backend image

1. Run the following command

```FRONTEND_URL="*" BACKEND_URL="*" docker run --rm -p 4567:4567 -it backend-flask```
As you can remember when we run our app manually we set two env variables otherwise our app won't work perfectly so we have to set those env variables when we run docker container like above command

<p align="center">
<img align="center"  src="./images/backend-container.png" alt="docker-extension">
</p>

<p align="center">
<img align="center"  src="./images/docker-ls-command-output.png" alt="docker-extension">
</p>

2. We can access our docker container logs to check everything is work fine
![container-logs](./images/docker-contsiner-log-view.png)
![container-log-console](./images/docker-logs-console-view.png)

3. Check the server if running by visiting the URL
<p align="center">
<img align="center"  src="./images/backend-responce.png" alt="backend-output">
</p>

