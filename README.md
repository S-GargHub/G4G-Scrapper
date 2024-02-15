# G4G-Scrapper

This application is built to scrap the user profile information from website called "GeeksForGeeks"

## API documentation:
The API scrapes the profile page using *BeautifulSoup* and uses *Flask* to deploy server on web.

## Functionalities
  -  [x]  Method - `GET`
  -  [x]  Extract the relevant data such as institute name, ranking etc from the GFG profile page given a username.
  -  [x]  Extract the count of problems solved based on difficulty categories and list all the problems solved along with the problem link.

## Endpoint
  - *http://127.0.0.1:5000/user/<GeeksforGeeksUsername>*
    
---

### Sample API Responses for username *sgarg16*
#### Success Response
```
// http://127.0.0.1:5000/user/sgarg16

{
  "info": {
    "username": "sgarg16",
    "Languages": "C++, C",
    "institution": "Banasthali University Tonk",
    "instituteRank": "707",
    "solved": "14",
    "codingScore": "14",
    "monthlyCodingScore": ""
  },
  "solvedStats": {
    "school": {
      "count": "0",
      "questions": [
        
      ]
    },
    "basic": {
      "count": "10",
      "questions": [
        {
          "question": "Bit Difference",
          "link": "https://practice.geeksforgeeks.org/problems/bit-difference-1587115620/0",
          "fromBabbar450Sheet": false
        },
        {
          "question": "Reverse sub array",
          "link": "https://practice.geeksforgeeks.org/problems/reverse-sub-array5620/0",
          "fromBabbar450Sheet": false
        },
        {
          "question": "Check if a number can be expressed as x^y",
          "link": "https://practice.geeksforgeeks.org/problems/check-if-a-number-can-be-expressed-as-xy1606/0",
          "fromBabbar450Sheet": false
        }
      ]
    },
    "easy": {
      "count": "2",
      "questions": [
        {
          "question": "Generate Binary Numbers",
          "link": "https://practice.geeksforgeeks.org/problems/generate-binary-numbers-1587115620/0",
          "fromBabbar450Sheet": false
        },
        {
          "question": "Missing number in array",
          "link": "https://practice.geeksforgeeks.org/problems/missing-number-in-array1416/0",
          "fromBabbar450Sheet": false
        }
      ]
    },
    "medium": {
      "count": "2",
      "questions": [
        {
          "question": "k largest elements",
          "link": "https://practice.geeksforgeeks.org/problems/k-largest-elements4206/0",
          "fromBabbar450Sheet": false
        },
        {
          "question": "Possible groups",
          "link": "https://practice.geeksforgeeks.org/problems/possible-groups2013/0",
          "fromBabbar450Sheet": false
        }
      ]
    },
    "hard": {
      "count": "0",
      "questions": [
        
      ]
    }
  }
}
```


## Instructions to run on your local system
* Clone the repository:
  - git clone https://github.com/S-GargHub/G4G-Scrapper.git

* Pre-requisites:
   - Python 3.x
   - Install all the required libraries using the *requirements.txt* file. 
    ``` pip install -r requirements.txt ```

* Directions to execute
    - ``` python3 app.py``` or ``` py app.py```
    - Open the web browser and visit the localhost, *http://127.0.0.1:5000/user/GeeksforGeeksUsername*
    - To view the user details, send a request to the above URL giving the g4g username.

* Directions to test
  - Run  ```pytest test_api.py```

## Pre requisities
   - Docker installed on your machine
   - Python and any other dependencies specific to the project. Install all the required libraries using the *requirements.txt* file. 
    ``` pip install -r requirements.txt ```

## Steps to deploy it the application on Docker Hub and EC2 cloud as part of CI using circleCI:

1. Build the REST api discussed above. I used flask server as my REST framework and BeautifulSoup to Scrap the webpage.
2. Try to run it locally to check all the endpoints
3. Set Up the GitHub Repository
4. Configure DockerHub
   - To host the Docker images, created an account on Dockerhub and configured the repository under user. I named it "scrapper"
5. Dockerize the Application
   - Create a ".Dockerfile" in the root of the project to define the Docker image for the application.
   - Test building and running your Docker image locally to ensure it works as expected:
     	- Build the docker: ```docker build -t <YOUR_DOCKER_IMAGE>:latest .```
     	- Tag the docker image: ```docker image tag g4g-profile-scrapper:latest <YOUR_DOCKER_REPO>:latest```
     	- Push the docker image: ```docker image push <YOUR_DOCKER_REPO>:latest```
     	- Run the docker: ```docker run -p 5000:5000 <YOUR_DOCKER_REPO>:latest```. The application must be up and running.
6. Configure Tests:
   - Create the test methods in the repository.
   - Command for testing - pytest
   - ```docker run -it --rm <YOUR_DOCKER_REPO>:latest /bin/sh -c "pytest"```
7. Configure AWS EC2 Instance:
   - Create a AWS account.
   - Launch an EC2 instance. Ensure to configure the security group to allow SSH traffic (port 22).
   - Create an SSH key pair and associate it with the EC2 instance by adding the public key to the ~/.ssh/authorized_keys file.
8. Connect to EC2
   - Locally check permission of rsa keys: - ls -al pem_key_file
   - Change permission: chmod 400 pem_key_file
   - Connect: - ssh -i pem_key_file ec2-user@ipaddres
9. Setup and configure CircleCI:
   - Create account on Circle CI and connect to github.
   - Add the project to CircleCI by logging in and following the prompts.
   - Create a config.yml file in the .circleci directory of the project.  Define the build and deployment workflow in config file. As part of this project, we have defined 3 jobs - **tests, build, deploy**
     - Tests Job: This job installs Python dependencies, runs the server in the background, runs unit tests, and stores test results and artifacts.
     - Build Job: This job builds the Docker image, tags it, logs in to Docker Hub, and pushes the image.
     - Deploy Job: This job installs Docker on an EC2 instance, logs in to Docker Hub, pulls the image, and runs it on the instance.
   - In the circleci project settings, add the "$DOCKERHUBUSER" and "DOCKERHUB_PASSWORD" environment variables. Also, add the ssh key for Github and the corresponding EC2 instance private keys.
10. Trigger Deployment:
    - Push changes to the GitHub repository to trigger the CircleCI pipeline.
    - CircleCI will build and test the code and deploy it to Docker Hub and EC2 cloud as part of CI.
      - As part of circleci config, we are accessing ec2 instance via ssh, installing docker, start docker service, login to the docker repository, pull the docker image, and run the docker iamge. Now using the public ip of instance we can hit the api on browser
