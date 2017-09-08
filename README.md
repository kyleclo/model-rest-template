# model-rest-template

This repo contains an example project for setting up a Flask service for a set of models with a common interface.

## Usage 

#### Adding new models

1. Add your new implementation of the `Model` interface to `models.py`.
2. Use `/add` to register your new model.  This records the endpoint containing the implementation in a database and adds an instantiation of the new model to the list of available models.
