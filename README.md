# devops-workshop
## Prep Work
### Register your AWS Educate Account
*Amazon Web Services (AWS) is a public cloud provider, that we will use to launch preconfigured instances for this workshop*
* Visit https://www.awseducate.com/Registration and register your Student account.
* Log in to AWS Educate account, click 'AWS Account' from the menu bar, click "Go to your AWS Educate starter account"
* This will launch a new window, with the AWS console
* Go to Services > EC2
* Create a Key Pair called "CODE" (Max)
* Create the security group (Max)
* Select "Launch Instance"
* Choose Ubuntu, choose keypair and sec group
* SSH to instance with:
```
ssh ubuntu@<PUBLIC_IP> -i /path/to/code.pem
```
* Run following:
```
sudo apt-get install docker-ce
sudo docker swarm init
sudo docker container run \
   --mount type=volume,source=jenkins-max-data,destination="/var/jenkins_home",volume-driver=local \
   -v /var/run/docker.sock:/var/run/docker.sock \
   -p 8080:8080 \
   --name jenkins-max -d \
   jenkins/jenkins:lts

```

## Pseudocode
* Introduce App
* Show Dockerfile
* Show Jenkinsfile
    * Build
    * Test
    * Deploy (docker service update)
* Start AMI in AWS with Docker installed
* ssh to Instance and start jenkins service
* Log into Jenkins UI
* Add github repo
* Do initial build on master
* Make a code change on a new branch with TDD, submit a pull request, view build & test
* Merge PR, view build, test & deploy
