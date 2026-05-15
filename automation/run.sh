#!/bin/bash

docker build -t coffee-cypress .

docker run --rm coffee-cypress
