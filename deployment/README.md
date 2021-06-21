# Deployments

This is where we define how we build our environment. This environment is running entirely in docker-compose. The containers are:

* three MySQL server containers
* one MySQL shell container (used to only provision the MySQL servers)
* one MySQL router container
* three web app containers
* one nginx container (acting as a load-balancer)

## Spinning up, testing, and taking down the containers

```bash
cd deployment
docker-compose up # spin up the containers
# NOTE: wait about two minutes for containers to start
```

You can test the install with a curl command. You should see a response indicating one userID in our database:

```bash
curl "http://127.0.0.1:80/show"
# {"userId": 1}
```

Tear everything down when you're done:

```bash
docker-compose down -v  # take down all containers and remove volumes
```
