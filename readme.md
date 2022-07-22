<div align="center">

# Docker Compose .env file tutorial

Simple tutorial for how to use environment variables with Docker. 

<small>For this example we are going to use `Python Flask`, but you can use it with any other language and framework that you want to.</small>
<small>Also, we're going to use `docker`and `docker compose`.</small>
 
</div>

## Why using .env files in our projects?
When we start to learn programming, commonly the basics tutorials for web dev show us the secrets in the project just like `SECRET=mysecretpasswordforcript`. We run the project and everything is fine. And that's ok. But when we start to develop some more real world feature, this is not a good idea, mainly if the project it will be open source or be exposed for some other people inside or outside of the organization.

Above that, when developing an open source application that will run in some production environment (many times also in dev environment), problably it will use some key or auth method for the external access.

The source code it will be exposed on our repo, and if we don't use different keys in dev environment and production environment, the security will be compromissed.

There is many ways to organize secret keys in production and development environments. One of then using `Docker` or `Docker Compose` is implementing an `.env` file (or more than 1 file) and configure our container or `docker-compose.yml` for start to using the variables defined on this archive.

The main goal doing that is take off the secrets of our hard code and putting in some another file that it will be load in the project and the secret values can be set dynamically.

After that we can switch between an open file, where everyone can have access, and the real file, where just you and the authorized users can have access.

Enough talking, let's code.

## Let's get started

What is in this tutorial:
1. - [x] `.env` file with environment variables
2. - [x] Hello world `Flask` app running showing some secrets loaded by `.env` file
3. - [x] `Dockerfile` for building `Docker image`
4. - [x] Run container using `Docker CLI` and loading variables with flags and .env file
5. - [x] `docker-compose.yml` file for up the service container with environments variables

### 1 - creating docker image
> This section it'll be important if you're not running on docker compose where we can build an image automatically.

<details>
    <summary>click to view</summary>
    tutorial for docker build . -t name
    docker images
</details>

<br>
<hr>
<br>

### 1.1 - Docker run env with flags
> This section is for creating a simple container loading environment variables in the container run with flags.

<details>
    <summary>click to view</summary>
    docker run image --name container-name -e var=value -p 80:5000
    localhost:5000
</details>

<br>
<hr>
<br>

### 1.2 - Docker run with .env file
Now we're talking! Let's start to using .env files for real.

Loading values from archives is a very common way to deal with secrets in programming.

The [.env file](https://docs.docker.com/compose/env-file/) is a default method available in `Docker` `Docker Compose` to start any service with the values inside the `.env`.

Is very simple to use. In the `.env` just write:<br>
`VARIABLE_NAME=VALUE`

### 2 Flask app running
to do

### 3 Dockerfile
to do

### 4 docker-compose.yml file
to do

### results
To do