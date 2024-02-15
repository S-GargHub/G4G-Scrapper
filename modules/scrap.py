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
            categories = {}

            # Iterate through each problem section
            for section in soup.find_all('div', class_='problemdiv col s12'):
                # Extract category name
                category_name = section.get('id')

                # Create empty list for questions if category doesn't exist
                if category_name not in categories:
                    categories[category_name] = []

                # Extract question title and link for each problem
                for problem in section.find_all('li', class_='col m6 s12'):
                    question_link = problem.find('a').get('href')
                    question_title = problem.find('a').text.strip()

                    # Store question information in the dictionary
                    categories[category_name].append({
                        'title': question_title,
                        'link': question_link
                    })

            # Extract categories, count and questions
            for category, questions in categories.items():
                questionList = []
                try:
                    solvedStats[category] = { "count" : soup.find(href="#"+category).text[soup.find(href="#"+category).text.index("(") + 1 : soup.find(href="#"+category).text.index(")")]}
                except:
                    solvedStats[category] = { "count" : 0 }
                for question in questions:
                    questionList.append({"question": question['title'], "link": question['link']})
                solvedStats[category]["questions"] = questionList

            generalInfo = {}

            def extract_detail(key, soup):
                try:
                    label = soup.find('div', text=key)
                    element = label.find_next_sibling('div')
                    return element.text.strip()
                except Exception:
                    return ""  

            def extract_span(key, soup):
                # Extract the rank
                try:
                    rank_element = soup.find('span', class_=key)
                    return rank_element.text.strip()
                except Exception:
                    return ""

            def extract_num(query, soup):
                try:
                    tag = soup.find_all(lambda tag: query.lower() in tag.text.lower() and list(
                        tag.select("div")) == [])[0]
                    return re.search(r'\d+', tag.text).group()
                except Exception:
                    return ""

            generalInfo["username"] = self.username
            generalInfo["Languages"] = extract_detail("Language Used", soup)
            generalInfo["institution"] = extract_detail("Institution", soup)
            try:
                generalInfo["instituteRank"] = extract_span("rankNum", soup)
            except Exception:
                generalInfo["instituteRank"] = ""
            generalInfo["solved"] = extract_num("Total Problem Solved", soup)
            generalInfo["codingScore"] = extract_num(
                "Overall Coding Score", soup)
            generalInfo["monthlyCodingScore"] = extract_num(
                "Monthly Coding Score", soup)
            response["info"] = generalInfo
            response["solvedStats"] = solvedStats

            return response
        else:
            return {"error" : "Profile Not Found"}
