<div align="center">

# Docker .env file tutorial

Simple tutorial for how to use environment variables with Docker. 

<small>For this example we are going to use Python Flask, but you can use it with any other language and framework that you want to.</small>
 
</div>

## Why using .env files with Docker?
When we are developing an open source application that will run in some production environment (many times also in dev environment), problably it will use some key or auth method for some service.

The source code it will be exposed on our repo, and if we don't use different keys in dev environment and production environment, the security will be compromisse.

There is many ways to organize secret keys in production and development environments. One of then using Docker Compose is implementing an .env file and configure our docker-compose.yml for start to using the variables defined on this archive.

### Let's get started

What is in this tutorial:
1. - [x] .env file with environment variables
2. - [x] Hello world Flask app running showing the environment variables
3. - [x] Dockerfile for building Docker image
4. - [x] docker-compose.yml file for up the container

### 1 .env file
to do

### 2 Flask app running
to do

### 3 Dockerfile
to do

### 4 docker-compose.yml file
to do

### results
To do