from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.template.loader import render_to_string
# Create your views here.
league_names = {
    'l_list' : 'There are you can find the list of English Leagues in correct order, where the first one is the strongest and the last one is the weakest </br>'
            'EPL - EPL/  </br>      '
            'EFL Championship - EFL_Championship/   </br>    '
            'EFL League One - EFL_League_One/    </br>   '
            'EFL League Two - EFL_League_Two/     </br> '
            'National League - National_League     </br>  ',
    'EPL' : 'leagues/EPL.html',
}
Teams = {
    'arsenal':'leagues/Arsenal.html'
}
def getTeams(request, league, team):
    if team:
        if Teams.get(team):
            url = Teams[team]
            return HttpResponse(render_to_string(url))
    elif league_names.get(league):
        url = league_names[league]
        return HttpResponse(render_to_string(url))
    else:
        return HttpResponseRedirect('404')


def NotFound(request):
    return HttpResponse(render_to_string('leagues/404.html'))








