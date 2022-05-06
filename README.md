# Kudos

Django app that allows users to send kudos to other users.

Users can send 3 kudos to other users in their organization. Every monday they get 3 new kudos to send, the kudos are not accumulated if they don't use them.

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Requirements
Docker compose

## Build the app
docker-compose -f local.yml build

## Run the app
docker-compose -f local.yml up

## Notes
- Some data is seeded so that there's something to play with
- An organization is created
- 3 users are created with usernames john, jane, jake
- Each user randomly sends a kudos to one of the other users
- The password for these dummy users is '1234'
