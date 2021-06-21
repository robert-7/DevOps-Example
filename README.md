# DevOps-Example

Focuses on setting up a highly available Python Bottle web app. This includes:

* a mutliple-instanced Bottle web app behind an nginx acting as the load-balancer
* a MySQL cluster behind a MySQL router

## NOTES

* This repo heavily uses [neumayer's innodb-cluster setup](https://github.com/neumayer/mysql-docker-compose-examples/tree/master/innodb-cluster) and modifies it for our needs.
* the service built with Python is really primitive and doesn't do much

## Getting Set Up for Local Development and Testing

Please see [the setup documentation](SETUP.md) regarding this.

## Deploying using docker-compose

Please see [the deployment documentation](deployment/README.md) regarding this.

## Things that are still missing

* haven't tested running this on a remote machine (i.e. the cloud), but it's supposed to accept all traffic... `¯\_(ツ)_/¯`
* I would've preferred to use Ansible for this, but I stuck with docker-compose as I saw some boilerplate code I could use for bringing up a MySQL cluster and just rolled with it
  * I would've liked to take this a step further with Terraform or Kubernetes, but I don't know Terraform and I didn't think I'd have time to set up the help charts for deploying to Kubernetes and testing
* only listens on port 80 (needs to still work on port 443)
* I can also clean up the repo to bring more organization
* the service built with Python is really primitive and doesn't do much. This can be enhanced, but I just need something that tests basic DB connections
* the Python image is huge and can be simplified by building app as a standalone binary in a builder image and copying it into a minimal docker image
  * the pip install command in [Dockerfile](Dockerfile) installs a lot of unnecessary packages that are necessary for deving locally but not for packaging the app
