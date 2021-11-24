# Download Docker.<br>
https://www.docker.com/products/docker-desktop<br>

# Install Flask library<br>
pip install Flask<br>


# Simple Flask code.<br>

from flask import Flask<br>
app = Flask(__name__)<br>

@app.route("/") <br>
def hello():<br>
    return "Anderson flask app!!"<br>

if __name__ == "__main__":<br>
    app.run(host='0.0.0.0', port=8080, debug=True)<br>
    
    
    
# Create DockerFile<br>

FROM python:3.7<br>

RUN mkdir /app <br>
WORKDIR /app <br>
ADD . /app/ <br>
RUN pip install -r requirements.txt <br>

EXPOSE 8080 <br> 
CMD ["python", "/app/main.py"] <br>



# Build Image<br>
docker build -f DockerFile -t pythonflaskdocker:latest .<br>

# List the image<br>
docker images<br>

# Run container.<br>
docker run -t -d -p 8080:8080 pythonflaskdocker<br>

# List the service<br>
docker ps<br>

