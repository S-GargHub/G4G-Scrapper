# G4G-Scrapper

## Functionalities
  -  [x]  Method supported - `GET`
  -  [x]  Extract the relevant data such as institute name, ranking etc from the GFG profile page given a username.
  -  [x]  Extract the count of problems solved based on difficulty categories and list all the problems solved along with the problem link.

## Endpoints
## How was it built:
The API is built using Web Scraping the profile page using *BeautifulSoup* and uisng *Flask* to deploy server on web.


## Instructions to run on your local system
* Pre-requisites:
	- Python 3.x
    - Install all the required libraries using the *requirements.txt* file. 
    ``` pip install -r requirements.txt ```

* Directions to execute
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
