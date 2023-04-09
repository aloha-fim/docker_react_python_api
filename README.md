"# docker_react_python_api" 

CTRL+SH P  "terminal venv" 
CMD J "activate venv"

docker build -t rest-apis-flask-python . "build docker"
docker run -d -p 5005:5000 rest-apis-flask-python




