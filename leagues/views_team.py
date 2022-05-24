from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
from leagues.forms import *

# league_names = {
#     'l_list' : 'There are you can find the list of English Leagues in correct order, where the first one is the strongest and the last one is the weakest </br>'
#             'EPL - EPL/  </br>      '
#             'EFL Championship - EFL_Championship/   </br>    '
#             'EFL League One - EFL_League_One/    </br>   '
#             'EFL League Two - EFL_League_Two/     </br> '
#             'National League - National_League     </br>  ',
#     'EPL/' : 'leagues/league.html',
# }
#
# teams={
#     'arsenal' : {'name' : 'Arsenal', 'description': 'Арсенал лучший клуб в мире', 'victories' : "Чемпион Англии - 13 раз"},
#     'aston_villa' : {'name' : 'Aston Villa', 'victories' : ""},
#     'brentford': {'name' : 'Brentford', 'victories' : ""},
#     'brighton': {'name' : 'Brighton', 'victories' : ""},
#     'burnley': {'name' : 'Burnley', 'victories' : ""},
#     'chelsea': {'name' : 'Chelsea', 'victories' : ""},
#     'crystal_palac': {'name' : 'Crystal Palac', 'victories' : ""},
#     'everton': {'name' : 'Everton', 'victories' : ""},
#     'leeds_united': {'name' : 'Leeds United', 'victories' : ""},
#     'leicester_city': {'name' : 'Leicester City', 'victories' : ""},
#     'liverpool': {'name' : 'Liverpool', 'victories' : ""},
#     'manchester_city': {'name' : 'Manchester City', 'victories' : ""},
#     'manchester_united': {'name' : 'Manchester United', 'victories' : ""},
#     'norwich_city': {'name' : 'Norwich City', 'victories' : ""},
#     'southampton': {'name' : 'Southampton', 'victories' : ""},
#     'tottenham_hotspur': {'name' : 'Tottenham Hotspur', 'victories' : ""},
#     'watford': {'name' : 'Watford', 'victories' : ""},
#     'west_ham_united': {'name' : 'West Ham United', 'victories' : ""},
#     'wolverhampton_wanderers': {'name' : 'Wolverhampton Wanderers', 'victories' : ""},
# }
# def getTeams(request, league, team):
#     data_teams = {
#         "team": teams[team]
#     }
#     if team:
#         if teams.get(team):
#             return HttpResponse(render(request, 'leagues/Team.html', context=data_teams))
#     elif league_names.get(league):
#         url = league_names[league]
#         return HttpResponse(render_to_string(url))
#     else:
#         return HttpResponseRedirect('404')
#
# def addTeam(request):
#     if request.method == 'POST':
#         form = AddTeamForm(request.POST)
#         print(request.POST)
#     else:
#         form = AddTeamForm()
#     return render(request, 'leagues/add_team.html', {'form': form})
#
#
# def NotFound(request):
#     return HttpResponse(render_to_string('leagues/404.html'))
#
#






