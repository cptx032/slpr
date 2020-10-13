# ALPR - SIMPLE SERVER
A very simple server to make possible to use the license plate recognition API of [alpr](https://www.openalpr.com/) by web requests (REST)


## How to test
- run the server with `DEBUG=1 ./manage.py runserver localhost:8000`
- get some image `wget http://i.ytimg.com/vi/gN2jtN9nvvk/maxresdefault.jpg`
- upload the file. Example: `curl -X POST -F "file=@maxresdefault.jpg" localhost:8000/api/v1/lprs/`

## How deploy
- clone the source to your server
- run `docker-compose up --build -d`