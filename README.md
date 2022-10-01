# Test of the AWS EC2 github CICD pipeline
- Simple Hello World flask app with 1 endpoint
- docker composed app
- github actions to propagate pushes to AWS server
- automated update on AWS server
- purpose: preparation for mobile app deployment

# AWS EC2 
- free tier t2.micro 
- Ubuntu 22.04

# guide
- setup AWS instances, policies and security https://medium.com/thelorry-product-tech-data/amazon-ec2-deployment-complete-ci-cd-pipeline-using-github-actions-and-aws-codedeploy-8a477123ff7e (dont need IAM, just network security)
- was missing outbind port 443
- ports set in app must be set to inbind 

### install docker
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html#create-container-image-install-docker

```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
sudo service docker start
sudo groupadd docker
sudo usermod -aG docker $USER
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

### install docker compose

    sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose
    docker-compose version


### Github runners
- https://www.youtube.com/watch?v=JS07npwL3Ps
- go to repo settings - actions - runners
- follow instructions there
- instead of `sudo ./run.sh` use `sudo ./svc.sh install` followed by `sudo ./svc.sh start`

### prepare app on server
```
mkdir app
cd app
touch .env
nano .env
```
- insert .env settings, save and close
