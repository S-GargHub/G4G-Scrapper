import json
from .scrap import scrap
from collections import OrderedDict

class track():

    def __init__(self, user):
        self.user = user
    
    def solve(self):
        scrapper = scrap(self.user)
        data = OrderedDict(scrapper.fetchResponse())
        if(data != {"error" : "Profile Not Found"}):
            details = []
            links = []
            for key in data['solvedStats'].keys():
                for i in range(len(data['solvedStats'][key]['questions'])):
                    link = data['solvedStats'][key]['questions'][i]['link']
                    data['solvedStats'][key]['questions'][i]['fromBabbar450Sheet'] = False
                    links.append(link)
                    details.append((key, i))
            return data
        
        else:
            return data
