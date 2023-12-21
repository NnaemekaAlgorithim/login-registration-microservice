FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install -r requirements.txt

ARG FLASK_ENV

ENV MYSQL_USER=root
ENV MYSQL_PWD=Mysql_247
ENV MYSQL_HOST=172.26.188.225
ENV MYSQL_PORT=3306
ENV MYSQL_DB=users_db

# Make port 80 available to the world outside this container
EXPOSE 80
