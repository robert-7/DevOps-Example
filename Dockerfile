FROM python:rc-alpine3.13

WORKDIR "/opt/"
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev mysql-client mariadb-dev
COPY ["requirements.txt", "./"]
RUN pip install -r requirements.txt
COPY ["app.py", "./"]
CMD ["./app.py"]
