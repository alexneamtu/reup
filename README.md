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

##### Environmental variables
| Variable | Description |
|---|---|
| DEBUG | Debug state |
| SECRET_KEY | The Django secret key |
| REUP_BASE_URL | The application base url |
| ALLOWED_HOSTS | The application allowed hosts |
| REUP_DOCUMENT_URL_PREFIX | The prefix used to display the updated urls |

##### Import documents

Run the following on the container:
```
python manage.py import_documents <documents csv path>
```

##### Run tests
```shell
pipenv install
pipenv run ./manage.py test
```
