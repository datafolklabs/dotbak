# Lazily Backup Files and Directories

[![Continuous Integration Status](https://travis-ci.org/datafolklabs/dotbak.svg)](https://travis-ci.org/datafolklabs/dotbak)


## Installation

```
$ pip install -r requirements.txt

$ pip install setup.py
```

## Usage

```
$ dotbak README.md

$ dotbak README.md

$ dotbak README.md

|$ ls -lah README.md*
-rw-r--r--    1 user     user        2.4K Sep 12 12:10 README.md
-rw-r--r--    1 user     user        2.4K Sep 12 12:56 README.md.bak
-rw-r--r--    1 user     user        2.4K Sep 12 12:56 README.md.bak.0
-rw-r--r--    1 user     user        2.4K Sep 12 12:56 README.md.bak.1
```

## Development

This project includes a number of helpers in the `Makefile` to streamline common development tasks.

### Environment Setup

The following demonstrates setting up and working with a development environment:

**Docker**:

This project includes a `docker-compose` configuration that sets up all required services, and dependencies for development and testing.  This is the recommended path for local development, and is the only fully supported option.

The following creates all required docker containers, and launches an BASH shell within the `dotbak` dev container for development.
```
$ make dev

|> dotbak <| src #
```

The above is the equivalent of running:

```
$ docker-compose up -d

$ docker-compose exec dotbak /bin/bash
```

**Testing Alternative Versions of Python**

The latest stable version of Python 3 is the default, and target version accessible as the `dotbak` container within Docker Compose.  For testing against alternative versions of python, additional containers are created (ex: `dotbak-py37`, `dotbak-py38`, etc). You can access these containers via:

```
$ docker-compose ps
        Name                      Command               State     Ports
-------------------------------------------------------------------------
dotbak_dotbak-py35_1   /bin/bash                        Up
dotbak_dotbak-py36_1   /bin/bash                        Up
dotbak_dotbak-py37_1   /bin/bash                        Up
dotbak_dotbak-py38_1   /bin/bash                        Up
dotbak_dotbak_1        /bin/bash                        Up


$ docker-compose exec dotbak-py37 /bin/bash

|> dotbak-py37 <| src #
```


**VirtualEnv**:

```
### create a virtualenv for development

$ make virtualenv

$ source env/bin/activate


### run dotbak cli application

$ dotbak --help


### run pytest / coverage

$ make test
```


### Releasing to PyPi

Before releasing to PyPi, you must configure your login credentials:

**~/.pypirc**:

```
[pypi]
username = YOUR_USERNAME
password = YOUR_PASSWORD
```

Then use the included helper function via the `Makefile`:

```
$ make dist

$ make dist-upload
```

## Deployments

### Docker

Included is a basic `Dockerfile` for building and distributing `DotBak`,
and can be built with the included `make` helper:

```
$ make docker

$ docker run -it dotbak --help
```
