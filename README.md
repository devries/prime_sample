# Sample prime number web application.

This application produces and infinitely scrolling page of all prime numbers.

# Local Installation

Make sure python and poetry are installed in your system. Install the
required packages by running

  poetry install

in the project directory.

# Testing

Run the unit tests using the command

  poetry run pytest

# Local server

Run the local test server using the command

  poetry run python app.py

# Build Docker container

Build the container using the command

  docker built -t primeweb:latest .

# Run Docker container

Run the docker container using the command

  docker run --rm -p 8080:8080 primeweb:latest
