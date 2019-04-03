# reup

Small project to recover [Hoover](https://github.com/hoover/snoop) document URLs.

## Docker

##### Import documents

##### Build

Create the docker image
```
docker build -t reup .
```

##### Run

Start the container
```
docker run --env SECRET_KEY=<secret> --env REUP_HOSTNAME=<hostname> -p 8000:<port> reup 
```

##### Import documents

Run the following on the container:
```
python manage.py import_documents <documents csv path>
```
 