# Non-Blocking Flask Service

This flask application aims to explain the difference and advantages of a
non-blocking service. In this repository, two simple methods are compared.
One method is used for adding two numbers and the other one is used for
multiplying two numbers. In order to display a delay during the execution of
the methods, for each one of them a 3 second sleeping time is added.

## Installation

Clone the repository from github via `git clone` and navigate to the project
directory.

Install `pipenv` via `brew` for MacOs

```sh
brew install pipenv
```

For Ubuntu

```sh
sudo apt install python-pip
python3 -m pip install --user pipenv
```

Install all required Python packages via

```sh
pipenv install
```

In order to activate virtual env, run

```sh
pipenv shell
```

## Testing

You can run the tests via:

  ```sh
  pytest test
  ```

## Running the Application

The application can be run both via:

```sh
flask app
```

if the application is installed locally or,

 ```sh
docker run -p 4000:4000 valdrinkuchi/flask_app:latest
```

if the application is not installed locally. A docker image is provided in the
docker hub which can be pulled and run on the desired port. This step does not
need any installation of the Flask Application. However, it assumes that a docker
runtime is present.

The application is served using gunicorn server and 4 workers when run from the docker
image. If you want to run the locally installed app using gunicorn you can use the
command found in the `entrypoint.sh`

```sh
gunicorn -w 4 -b 0.0.0.0:4000 app:app
```

## Api-Overview

For testing purposes two end points are provided:

1. `/sync` on this endpoint the request will be processed as a synchronous one.
   The numbers to be added and multiplied are hardcoded as `4` and `5`. As as
   response a json object similar to this one should be retrieved:

    ```sh
    `0.0.0.0:4000/sync`
    {
      "output": {
        "addition": 9,
        "elapsed_time": 6.002140346000001,
        "multiply": 20
      }
    }
    ```

2. `/async` on this endpoint the request will be processed as an asynchronous one.
   Same as above the numbers are hardcoded as `4` and `5` and the response should
   look similar to this:

    ```sh
    `0.0.0.0:4000/async`
    {
      "output": {
        "addition": 9,
        "elapsed_time": 3.0059341060004954,
        "multiply": 20
      }
    }
    ```

As you can see from the response data that the `elapsed_time` is `% 50` less when
the execution is made asynchronously. The multiplication process does not have to wait
for the addition method to finish, in turn, it is executed in a separate event loop.
Thus making the execution time `% 50` shorter.

## Used tools

* `Flask` and `Flask[async]`
* `AsyncIo` library for making asynchronous calls
* `pytest` for testing the application
* `pytest-asyncio` for testing async methods
* `gunicorn` as a WSGI HTTP Server
* `docker` for containerization and portability

## Security

When deploying any application security aspects that need to be considered:

1. Firewall can be used to block access to unnecessary ports, thus making only
   necessary ports available.
2. If the application is using a database, the database should be kept in a private
   network.
3. If the application is using secret data like private `API KEYS` when deployed
   using secrete manager is a good solution to consider.
4. Rate Limiter for the application endpoints can be set.This will control how ofter
   one can access the provided `API`. Flask has own extensions for this like `flask_limiter`
