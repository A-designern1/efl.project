from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def getLeagues(request):
    return HttpResponse(
        'There are you can find the list of English Leagues in correct order, where the first one is the strongest and the last one is the weakest </br>'
        'EPL - EPL/  </br>      '
        'EFL Championship - EFL_Championship/   </br>    '
        'EFL League One - EFL_League_One/    </br>   '
        'EFL League Two - EFL_League_Two/     </br> '
        'National League - National_League     </br>  ')


def getEPL(request):
    return HttpResponse('EPL teams in alphabet order  </br>'
                        ' </br>'
                        'Arsenal  </br>'
                        'Aston Villa  </br>'
                        'Brentford  </br>'
                        'Brighton  </br>'
                        'Burnley  </br>'
                        'Chelsea  </br>'
                        'Crystal Palac  </br>'
                        'Everton  </br>'
                        'Leeds United  </br>'
                        'Leicester City  </br>'
                        'Liverpool  </br>'
                        'Manchester City  </br>'
                        'Manchester United  </br>'
                        'Newcastle United  </br>'
                        'Norwich City  </br>'
                        'Southampton  </br>'
                        'Tottenham Hotspur  </br>'
                        'Watford  </br>'
                        'West Ham United  </br>'
                        'Wolverhampton Wanderers  </br>')


def getEflChamp(request):
    return HttpResponse('EFL Championship')


def getEfl_L1(request):
    return HttpResponse('EFL League One')


def getEfl_L2(request):
    return HttpResponse('EFL League Two')


def getNL(request):
    return HttpResponse('National League')
