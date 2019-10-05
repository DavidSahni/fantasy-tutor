import requests
from bs4 import beautifulsoup
from enum import Enum

class Extension(Enum):
    Roster = 0
    Team = 1

class EspnRequest:

    baseUrl= 'https://fantasy.espn.com/basketball/'
    pathExt= ''
    param= None

    def __init__(self):
        self.param = Params()

    def SetExtension(self, ext):
        if ext is Extension.Roster:
            self.pathExt = 'league/rosters'
        elif ext is Extension.Team:
            self.pathExt = '/team'
        
    def ExecuteQuery(self):
        query = (self.baseUrl + self.pathExt + "?" +
             self.param.getLeagueParam() + 
             self.param.getSeasonParam() +
             self.param.getTeamParam())
        result = False
        try:
            response = requests.get(query)
            if response.status_code == 200:
                result = response.text
        except Exception as e:
            print(e)
            print("Exception in Execute Query")





    class Params:
        leagueParam: ''
        teamParam: ''
        seasonParam: ''

        def __init__(self, *args, **kwargs):
                seasonParam = '2019'
                leagueParam = '104753'
        
        def getLeagueParam(self):
            if not self.leagueParam:
                return ''
            else: 
                return 'leagueId=' + self.leagueParam

        def getTeamParam(self):
            if not self. teamParam:
                return ''
            else:
                return "teamId=" + self.teamParam

        def getSeasonParam(self):
            if not self.seasonParam:
                return ''
            else: 
                return 'seasonId='+ self.seasonParam



class FantasyParser():

    def __init__(self, rawHtml):
        self.parser = beautifulsoup(rawHtml, 'html.parser')

    def createParser(self, rawHtml):
        self.parser = beautifulsoup(rawHtml, 'html.parser')

    def getRosterTeamNames(self):
        self.parser.



