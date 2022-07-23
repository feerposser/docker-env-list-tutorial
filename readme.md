<div align="center">

# Docker Compose .env file tutorial

Simple tutorial for how to use environment variables with Docker. 

<small>For this example we are going to use `Python Flask`, but you can use it with any other language and framework that you want to.</small>
<small>Also, we're going to use `docker`and `docker compose`.</small>
 
</div>

<br>
<hr>
<br>

## Why using .env files in our projects?
When we start to learn programming, commonly the basics tutorials for web dev show us the secrets in the project just like `SECRET=mysecretpasswordforcript`. We run the project and everything is fine. And that's ok. But when we start to develop some more real world feature, this is not a good idea, mainly if the project it will be open source or be exposed for some other people inside or outside of the organization.

Above that, when developing an open source application that will run in some production environment (many times also in dev environment), problably it will use some key or auth method for the external access.

The source code it will be exposed on our repo, and if we don't use different keys in dev environment and production environment, the security will be compromissed.

There is many ways to organize secret keys in production and development environments. One of then using `Docker` or `Docker Compose` is implementing an `.env` file (or more than 1 file) and configure our container or `docker-compose.yml` for start to using the variables defined on this archive.

The main goal doing that is take off the secrets of our hard code and putting in some another file that it will be load in the project and the secret values can be set dynamically.

After that we can switch between an open file, where everyone can have access, and the real file, where just you and the authorized users can have access.

Enough talking, let's code.

<br>
<hr>
<br>

## Let's get started

What is in this tutorial:
1. - [x] `.env` file with environment variables
2. - [x] Hello world `Flask` app running showing some secrets loaded by `.env` file
3. - [x] `Dockerfile` for building `Docker image`
4. - [x] Run container using `Docker CLI` and loading variables with flags and .env file
5. - [x] `docker-compose.yml` file for up the service container with environments variables

We're not going to learn Docker or Docker Compose from scratch. This tutorial assumes that you know the basics of each one of then.

<br>
<hr>
<br>

### 1 - creating docker image
> This section it'll be important if you're not running on docker compose where we can build an image automatically.

<details>
<summary>click to view</summary>

<p>First things first, let's create the image that will be used to start the container. For doing that just type it the following command inside the Dockerfile directory:</p>

`docker build . -t docker-tutorial-image`

<p>This will build an image based on Dockerfile with tag 'docker-tutorial-image' or whatever other name you want to.</p>

<p>You can check this out just typing the command bellow for list all available image:</p>

`docker images`
</details>

<br>
<hr>
<br>

### 1.1 - Docker run env with flags
> This section is for creating a simple container that loads environment variables in the container running with flags.

<details>
<summary>click to view</summary>
<p>To start the container by using the image created in the last section, just type the following command:</p>

`docker run -p 80:5000 --name testing -e NAME=myname -d docker-tutorial-image`

<p>The command above connect the 80 host port to the 5000 container port. The --name flag set a name to the container, wich you can check by typing the command:</p>

`docker ps`

<p>and checking the name column. The -e flag is who insert the variables in the container. The -e is folowed by this sintax:</p>

`VARIABLE=VALUE`

<p>The -d flag runs the container in background. Last but not least, the tag image used in the build section.</p>
<p>Now, we can open the browser and check the results by fallowing the URL:</p>

`http://localhost`.

<div align="center">

![image](./assets/img/1.png)
</div>

<p>As you can see, the API run inside the container returns a list with varibles, where the 'NAME' variable have the value set in the -e flag. If you type more -e flags fallowed by VAR-NAME=VALUE, it will be showed in browser.</p>

<div align="center"><small>But just GITHUB, INSTAGRAM, LINKEDIN, NAME and YOUTUBE will appear because of the <a src="./tutorial/app.py">app.py</a> script behaviour. You can change it as you want.</small></div>

</details>

<br>
<hr>
<br>

### 1.2 - Docker run with .env file
>Now we're talking! Let's start to using .env files for real. In this section we will do the same as the last one, but this time with a `.env` file instead of -e flag.

<details>
<summary>click to view</summary>
Loading values from archives is a very common way to deal with secrets in programming.

The [.env file](https://docs.docker.com/compose/env-file/) is a default method available in `Docker` and `Docker Compose` to start any service with the values inside the `.env`.

Is very simple to use. In the `.env` just write your variables with the following sintax:<br>
`VARIABLE_NAME=VALUE`

You can see this in the [.env file](./tutorial/.env) inside the tutorial folder. Sometimes, depending on the string format, the variables will use some special character(s) that can be interpreted by the shell as a comment os something. In this case you can use [simple quotes to avoid the default behaviour](https://github.com/docker/compose/issues/8607#issuecomment-938235797): `VARNAME='VALUE'`.

In that way we can define files for being used in dev and production environment and switch between then, also managing which one you want to expose by using [.gitignore](https://git-scm.com/docs/gitignore).

To start a container loading the file, just type the command bellow inside the tutorial folder:

`docker run -p 80:5000 --name tutorial --env-file .env tutorial`

The only news here is the `--env-file` flag, which is used to define the file that will be used to load the enrivonment variables to the container.

Now, if you open the `http://localhost` address:

<div align="center">

![image](./assets/img/2.png)

</div>

All the variables inside .env are loaded to the container, which runs the Flask API that return then to the browser.

</details>

<br>
<hr>
<br>

### 2 docker-compose.yml file
> In this section we'll see how to use .env file in a `docker compose` project.

<details>
<summary>click do view</summary>

In [Docker Compose](https://docs.docker.com/compose/) things are a little bit different and with more clean commands. In the [docker-compose.yml](./tutorial/docker-compose.yaml) file there are some definitions that able us to just run the fallowing command inside the tutorial folder to get everything up and running:

`docker compose up --build -d`

<small>Depending on the Docker environ version that you're using maybe run with 'docker-compose' instead.</small>

If you refresh the page, will se the exactly same result as before. Let's understand what just it happened.

The `up` command is to set up and run the services defined inside docker-compose file, while `--build` flag is to build the image if the image dont exists and `-d` flag is to run everything on background.

In the service level indentation you'll find a `env_file` definition that uses the `.env file`. This will load the file and bring the variables to the container config. 

Right bellow there is the `environment` definition. The sintax is very simple: `CONTAINER_VARIABLE=${ENV_FILE_VARIABLE}`. The values of the `.env file` variables will be stored in the container variables. Using that you can just change the `env_file` path to switch between files that will be loaded in the service container.

After testing just execute the command to stop the container:
`docker compose down`

</details>

<br>
<hr>
<br>

## Conclusion

In this simple example we're just using a service API that returns the environment variables names and values. But I think you get the idea. The values inside `.env` file can be used for hashing, cryptography, setting configs and all kind of stuff.

You also can create a folder with multiple .env files just like `.env.production`, `production.env` or any file name sintax that you like for production and development too. In this way you can handle the secrets exposure just by using .gitignore file in your repo.

I hope this tutorial helps you to understand how to use environment variables with Docker or Docker Compose. Feel free to leave a comment for any error ou just asking a question. 

Cheers!

Bye (:

Adiós!

au revoir :)

Tchau (: