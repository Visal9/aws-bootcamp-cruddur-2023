# pull in the base image
FROM python:3.10-slim-buster

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