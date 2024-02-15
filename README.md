# G4G-Scrapper

This application is built to scrap the user profile information from website called "GeeksForGeeks"

## Functionalities
  -  [x]  Method supported - `GET`
  -  [x]  Extract the relevant data such as institute name, ranking etc from the GFG profile page given a username.
  -  [x]  Extract the count of problems solved based on difficulty categories and list all the problems solved along with the problem link.

## Endpoints
## How was it built:
The API scrapes the profile page using *BeautifulSoup* and uses *Flask* to deploy server on web.

## Instructions to run on your local system
* Pre-requisites:
   - Python 3.x
   - Install all the required libraries using the *requirements.txt* file. 
    ``` pip install -r requirements.txt ```

* Directions to execute
   ```bash
   git clone "repo_path"
   cd repo
   ```
    - ``` python3 app.py``` or ``` py app.py```
    - Open the browser of your choice and visit your localhost, either *http://127.0.0.1:5000/user/GeeksforGeeksUsername*
    - Below is the Sample API Response for user *sgarg16*
---

### Sample API Responses
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

* Directions to test
  - Run  ```pytest test_api.py```

##Pre requisities
   - Docker installed on your machine
   - Python and any other dependencies specific to the project. Install all the required libraries using the *requirements.txt* file. 
    ``` pip install -r requirements.txt ```

## Steps to follow:

1. Build the Api server
2. Set Up the GitHub Repository
3. Configure DockerHub
   - To host the Docker images, created an account on Dockerhub and configured your repository.
4. Dockerize the Application
   - Create a Dockerfile in the root of the project to define the Docker image for the application.
   - Test building and running your Docker image locally to ensure it works as expected:
     	- Build the docker: ```docker build -t <YOUR_DOCKER_IMAGE>:latest .```
     	- Tag the docker image: ```docker image tag g4g-profile-scrapper:latest <YOUR_DOCKER_REPO>:latest```
     	- Push the docker image: ```docker image push <YOUR_DOCKER_REPO>:latest```
     	- Run the docker: ```docker run -p 5000:5000 <YOUR_DOCKER_REPO>:latest```. The application must be up and running.
5. Configure Tests:
   - Create the test methods in the repository
   - ```docker run -it --rm <YOUR_DOCKER_REPO>:latest /bin/sh -c "pytest"```
7. Setup and configure CircleCI:
   - Add your project to CircleCI by logging in and following the prompts.
   - Create a config.yml file in the .circleci directory of your project.  Define the build and deployment workflow in config file. As part of this project, we have defined 3 jobs - **tests, build, deploy**
   - In the circleci project settings, add the "$DOCKERHUBUSER" and "DOCKERHUB_PASSWORD" environment variables. Also, add the ssh key for Github and the corresponding EC2 instance private keys.
9. Configure AWS EC2 Instance:
   - Launch an EC2 instance. Ensure to configure the security group to allow SSH traffic (port 22).
   - Create an SSH key pair and associate it with your EC2 instance by adding the public key to the ~/.ssh/authorized_keys file.
10. Trigger Deployment:
    - Push changes to the GitHub repository to trigger the CircleCI pipeline.
    - CircleCI will build and test your code and deploy it to Docker Hub and EC2.

