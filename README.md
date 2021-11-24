# Download Docker.
https://www.docker.com/products/docker-desktop

# Install Flask library
pip install Flask


# Simple Flask code.

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Anderson flask app!!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
    
    
    
# Create DockerFile

FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requirements.txt

EXPOSE 8080
CMD ["python", "/app/main.py"]



# Build Image
docker build -f DockerFile -t pythonflaskdocker:latest .

# List the image
docker images

# Run container.
docker run -t -d -p 8080:8080 pythonflaskdocker

