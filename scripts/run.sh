#!/bin/bash

# Define variables
container_name="cinefy"
container_port=8011

# Check if the container exists and remove it if it does
if docker ps -aqf "name=$container_name" &>/dev/null; then
    echo "Removing existing container: $container_name"
    docker stop $container_name &>/dev/null && docker rm $container_name &>/dev/null
fi

# Run the container locally
echo "Starting container: $container_name"
docker run --name "$container_name" --network celltrakdev -d --publish 8011:8011 cinefy:local
