#!/usr/bin/env sh
# Script to generate .env.example

# Remove the values from env vars in .env
sed -r 's/(.*\=)("?)(.*)(\"?)/\1/g' .env >.env.example
# git add .env.example
git update-index --add .env.example
