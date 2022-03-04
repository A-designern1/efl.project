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
    'EPL' : 'EPL teams in alphabet order  </br>'
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
                            'Wolverhampton Wanderers  </br>',
    'EFL_Championship' : 'EFL Championship teams in alphabet order </br>'
                                'Barnsley   </br>'
                                'Birmingham City  </br>'
                                'Blackburn Rovers  </br>'
                                'Blackpool  </br>'
                                'Bournemouth  </br>'
                                'Bristol City  </br>'
                                'Cardiff City  </br>'
                                'Coventry City  </br>'
                                'Derby County  </br>'
                                'Fulham  </br>'
                                'Huddersfield Town  </br>'
                                'Hull City  </br>'
                                'Luton Town  </br>'
                                'Middlesbrough  </br>'
                                'Millwall  </br>'
                                'Nottingham Forest  </br>'
                                'Peterborough United  </br>'
                                'Preston North End  </br>'
                                'Queens Park Rangers  </br>'
                                'Reading  </br>'
                                'Sheffield United  </br>'
                                'Stoke City  </br>'
                                'Swansea City  </br>'
                                'West Bromwich Albion  </br>',
    'EFL_League_One' : '"EFL League One" teams in aphabet order  </br>'
                                'Accrington Stanley  </br>'
                                'AFC Wimbledon  </br>'
                                'Bolton Wanderers  </br>'
                                'Burton Albion  </br>'
                                'Cambridge United  </br>'
                                'Charlton Athletic  </br>'
                                'Cheltenham Town  </br>'
                                'Crewe Alexandra  </br>'
                                'Doncaster Rovers  </br>'
                                'Fleetwood Town  </br>'
                                'Gillingham  </br>'
                                'Ipswich Town </br>'
                                'Lincoln City  </br>'
                                'Milton Keynes Dons  </br>'
                                'Morecambe  </br>'
                                'Oxford United </br>'
                                'Plymouth Argyle  </br>'
                                'Portsmouth  </br>'
                                'Rotherham United  </br>'
                                'Sheffield Wednesday  </br>'
                                'Shrewsbury Town  </br>'
                                'Sunderland  </br>'
                                'Wigan Athletic  </br>'
                                'Wycombe Wanderers  </br>',
    'EFL_League_Two' : '"EFL League Two" teams in alphabet order  </br>'
                                'Barrow  </br>'
                                'Bradford City  </br>'
                                'Bristol Rovers  </br>'
                                'Carlisle United  </br>'
                                'Colchester United  </br>'
                                'Crawley Town  </br>'
                                'Exeter City  </br>'
                                'Forest Green Rovers  </br>'
                                'Harrogate Town  </br>'
                                'Hartlepool United  </br>'
                                'Leyton Orient  </br>'
                                'Mansfield Town  </br>'
                                'Newport County  </br>'
                                'Northampton Town  </br>'
                                'Oldham Athletic  </br>'
                                'Port Vale  </br>'
                                'Rochdale  </br>'
                                'Salford City  </br>'
                                'Scunthorpe United  </br>'
                                'Stevenage  </br>'
                                'Sutton United  </br>'
                                'Swindon Town  </br>'
                                'Tranmere Rovers  </br>'
                                'Walsall  </br>',
    'National_League' : '"National League" teams in alphabet order  </br>'
                                'Aldershot Town  </br>'
                                'Altrincham  </br>'
                                'Barnet </br>'
                                'Boreham Wood </br>'
                                'Bromley </br>'
                                'Chesterfield </br>'
                                'Dagenham & Redbridge </br>'
                                'Dover Athletic </br>'
                                'Eastleigh </br>'
                                'FC Halifax Town </br>'
                                'Grimsby Town </br>'
                                "King's Lynn Town </br>"
                                'Maidenhead United </br>'
                                'Notts County  </br>'
                                'Solihull Moors  </br>'
                                'Southend United  </br>'
                                'Stockport County  </br>'
                                'Torquay United  </br>'
                                'Wealdstone  </br>'
                                'Weymouth  </br>'
                                'Woking  </br>'
                                'Wrexham  </br>'
                                'Yeovil Town  </br>'
}
def getLeagues(request, league_name):
    LeagueName = league_name
    if league_names.get(LeagueName):
        return HttpResponse(league_names[LeagueName])

    else:
        return HttpResponseRedirect('404')

def NotFound(request):
    return HttpResponse(render_to_string('leagues/404.html'))





















































          # 'There are you can find the list of English Leagues in correct order, where the first one is the strongest and the last one is the weakest </br>'
    #             # 'EPL - EPL/  </br>      '
    #             # 'EFL Championship - EFL_Championship/   </br>    '
    #             # 'EFL League One - EFL_League_One/    </br>   '
    #             # 'EFL League Two - EFL_League_Two/     </br> '
    #             # 'National League - National_League     </br>  ')
    #     # elif LeagueName:
    #     #     return HttpResponse(league_names[LeagueName])
    #     # elif league_name == 'EFL_Championship/':
    #     #     #     return HttpResponse('EFL Championship teams in alphabet order </br>'
    #     #     #                         'Barnsley'
    #     #     #                         'Birmingham City'
    #     #     #                         'Blackburn Rovers'
    #     #     #                         'Blackpool'
    #     #     #                         'Bournemouth'
    #     #     #                         'Bristol City'
    #     #     #                         'Cardiff City'
    #     #     #                         'Coventry City'
    #     #     #                         'Derby County'
    #     #     #                         'Fulham'
    #     #     #                         'Huddersfield Town'
    #     #     #                         'Hull City'
    #     #     #                         'Luton Town'
    #     #     #                         'Middlesbrough'
    #     #     #                         'Millwall'
    #     #     #                         'Nottingham Forest'
    #     #     #                         'Peterborough United'
    #     #     #                         'Preston North End'
    #     #     #                         'Queens Park Rangers'
    #     #     #                         'Reading'
    #     #     #                         'Sheffield United'
    #     #     #                         'Stoke City'
    #     #     #                         'Swansea City'
    #     #     #                         'West Bromwich Albion')
    #     #     # elif league_name == 'EFL_League_One/':
    #     #     #     return HttpResponse('"EFL League One" teams in aphabet order'
    #     #     #                         'Accrington Stanley'
    #     #     #                         'AFC Wimbledon'
    #     #     #                         'Bolton Wanderers'
    #     #     #                         'Burton Albion'
    #     #     #                         'Cambridge United'
    #     #     #                         'Charlton Athletic'
    #     #     #                         'Cheltenham Town'
    #     #     #                         'Crewe Alexandra'
    #     #     #                         'Doncaster Rovers'
    #     #     #                         'Fleetwood Town'
    #     #     #                         'Gillingham'
    #     #     #                         'Ipswich Town'
    #     #     #                         'Lincoln City'
    #     #     #                         'Milton Keynes Dons'
    #     #     #                         'Morecambe'
    #     #     #                         'Oxford United'
    #     #     #                         'Plymouth Argyle'
    #     #     #                         'Portsmouth'
    #     #     #                         'Rotherham United'
    #     #     #                         'Sheffield Wednesday'
    #     #     #                         'Shrewsbury Town'
    #     #     #                         'Sunderland'
    #     #     #                         'Wigan Athletic'
    #     #     #                         'Wycombe Wanderers')
    #     #     # elif league_name == 'EFL_League_Two/':
    #     #     #     return HttpResponse('"EFL League Two" teams in alphabet order'
    #     #     #                         'Barrow'
    #     #     #                         'Bradford City'
    #     #     #                         'Bristol Rovers'
    #     #     #                         'Carlisle United'
    #     #     #                         'Colchester United'
    #     #     #                         'Crawley Town'
    #     #     #                         'Exeter City'
    #     #     #                         'Forest Green Rovers'
    #     #     #                         'Harrogate Town'
    #     #     #                         'Hartlepool United'
    #     #     #                         'Leyton Orient'
    #     #     #                         'Mansfield Town'
    #     #     #                         'Newport County'
    #     #     #                         'Northampton Town'
    #     #     #                         'Oldham Athletic'
    #     #     #                         'Port Vale'
    #     #     #                         'Rochdale'
    #     #     #                         'Salford City'
    #     #     #                         'Scunthorpe United'
    #     #     #                         'Stevenage'
    #     #     #                         'Sutton United'
    #     #     #                         'Swindon Town'
    #     #     #                         'Tranmere Rovers'
    #     #     #                         'Walsall')
    #     #     # elif league_name == 'National_League/':
    #     #     #     return HttpResponse('"National League" teams in alphabet order'
    #     #     #                         'Aldershot Town'
    #     #     #                         'Altrincham'
    #     #     #                         'Barnet'
    #     #     #                         'Boreham Wood'
    #     #     #                         'Bromley'
    #     #     #                         'Chesterfield'
    #     #     #                         'Dagenham & Redbridge'
    #     #     #                         'Dover Athletic'
    #     #     #                         'Eastleigh'
    #     #     #                         'FC Halifax Town'
    #     #     #                         'Grimsby Town'
    #     #     #                         "King's Lynn Town"
    #     #     #                         'Maidenhead United'
    #     #     #                         'Notts County'
    #     #     #                         'Solihull Moors'
    #     #     #                         'Southend United'
    #     #     #                         'Stockport County'
    #     #     #                         'Torquay United'
    #     #     #                         'Wealdstone'
    #     #     #                         'Weymouth'
    #     #     #                         'Woking'
    #     #     #                         'Wrexham'
    #     #     #                         'Yeovil Town')