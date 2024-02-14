from bs4 import BeautifulSoup as bs
import requests
import re

class scrap():

    def __init__(self,username):
        self.username = username
    
    def fetchResponse(self):
        url = 'https://auth.geeksforgeeks.org/user/{}/practice/'.format(self.username)
        profilePage = requests.get(url)

        if profilePage.status_code == 200:
            soup = bs(profilePage.content, 'html.parser')

            response = {}
            solvedStats = {}
            try:
                solvedStats["school"] = { "count" : soup.find(href="#school").text[soup.find(href="#school").text.index("(") + 1 : soup.find(href="#school").text.index(")")]}
            except:
                solvedStats["school"] = { "count" : 0 }
            try:    
                solvedStats["basic"] = { "count" : soup.find(href="#basic").text[soup.find(href="#basic").text.index("(") + 1 : soup.find(href="#basic").text.index(")")]}
            except:
                solvedStats["basic"] = { "count" : 0 }
            try: 
                solvedStats["easy"] = { "count" : soup.find(href="#easy").text[soup.find(href="#easy").text.index("(") + 1 : soup.find(href="#easy").text.index(")")]}
            except:
                solvedStats["easy"] = { "count" : 0 }
            try:
                solvedStats["medium"] = { "count" : soup.find(href="#medium").text[soup.find(href="#medium").text.index("(") + 1 : soup.find(href="#medium").text.index(")")]}
            except:
                solvedStats["medium"] = { "count" : 0 }
            try:
                solvedStats["hard"] = { "count" : soup.find(href="#hard").text[soup.find(href="#hard").text.index("(") + 1 : soup.find(href="#hard").text.index(")")]}
            except:
                solvedStats["hard"] = { "count" : 0 }

            questionTags = []

            if soup.select("#school .page-content ul li a") != []:
                questionTags = soup.select("#school .page-content ul li a")
                questionList = []
                for questionTag in questionTags:
                    questionList.append({ "question" : questionTag.text, "link" : questionTag.get("href")})
                solvedStats["school"]["questions"] = questionList
            else:
                solvedStats["school"]["questions"] = []

            if soup.select("#basic .page-content ul") != []:
                questionTags = soup.select("#basic .page-content ul li a")
                questionList = []
                for questionTag in questionTags:
                    questionList.append({ "question" : questionTag.text, "link" : questionTag.get("href")})
                solvedStats["basic"]["questions"] = questionList
            else:
                solvedStats["basic"]["questions"] = []

            if soup.select("#easy .page-content ul") != []:
                questionTags = soup.select("#easy .page-content ul li a")
                questionList = []
                for questionTag in questionTags:
                    questionList.append({ "question" : questionTag.text, "link" : questionTag.get("href")})
                solvedStats["easy"]["questions"] = questionList
            else:
                solvedStats["easy"]["questions"] = []

            if soup.select("#medium .page-content ul") != []:
                questionTags = soup.select("#medium .page-content ul li a")
                questionList = []
                for questionTag in questionTags:
                    questionList.append({ "question" : questionTag.text, "link" : questionTag.get("href")})
                solvedStats["medium"]["questions"] = questionList
            else:
                solvedStats["medium"]["questions"] = []

            if soup.select("#hard .page-content ul") != []:
                questionTags = soup.select("#hard .page-content ul li a")
                questionList = []
                for questionTag in questionTags:
                    questionList.append({ "question" : questionTag.text, "link" : questionTag.get("href")})
                solvedStats["hard"]["questions"] = questionList
            else:
                solvedStats["hard"]["questions"] = []

            generalInfo = {}

            def extract_detail(key, soup):
                try:
                    return next(filter(
                        lambda div: key.lower() in div.text.lower(),
                        soup.select(".userMainDiv > div")
                    )).select_one("div:nth-child(2)").text.strip()
                except Exception:
                    return ""

            def extract_num(query, soup):
                try:
                    tag = soup.find_all(lambda tag: query.lower() in tag.text.lower() and list(
                        tag.select("div")) == [])[0]
                    return re.search(r'\d+', tag.text).group()
                except Exception:
                    return ""

            generalInfo["name"] = extract_detail("name", soup)
            generalInfo["username"] = self.username
            generalInfo["institution"] = extract_detail("Institution", soup)
            try:
                generalInfo["instituteRank"] = re.search(r'\d+', extract_detail(
                    "Rank", soup)).group()
            except Exception:
                generalInfo["instituteRank"] = ""
            generalInfo["solved"] = extract_num("Problems Solved", soup)
            generalInfo["codingScore"] = extract_num(
                "Overall Coding Score", soup)
            generalInfo["monthlyCodingScore"] = extract_num(
                "Monthly Coding Score", soup)
            response["info"] = generalInfo
            response["solvedStats"] = solvedStats

            return response
        else:
            return {"error" : "Profile Not Found"}
