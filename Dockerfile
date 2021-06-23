FROM python:3.9-alpine3.12 AS builder

WORKDIR "/opt"
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev mysql-client mariadb-dev upx
COPY ["requirements.txt", "./"]
RUN pip install -r requirements.txt
COPY ["app.py", "favicon.ico", "./"]
RUN pyinstaller --onefile --distpath /opt app.py

FROM alpine
WORKDIR "/opt"
COPY --from=builder /opt/app ./
CMD ["./app"]
