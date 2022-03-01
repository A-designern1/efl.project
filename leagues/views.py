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
    return HttpResponse('EFL Championship teams in alphabet order </br>'
                        'Barnsley' 
                        'Birmingham City' 
                        'Blackburn Rovers' 
                        'Blackpool' 
                        'Bournemouth' 
                        'Bristol City' 
                        'Cardiff City'
                        'Coventry City' 
                        'Derby County' 
                        'Fulham' 
                        'Huddersfield Town' 
                        'Hull City' 
                        'Luton Town' 
                        'Middlesbrough' 
                        'Millwall' 
                        'Nottingham Forest' 
                        'Peterborough United' 
                        'Preston North End' 
                        'Queens Park Rangers' 
                        'Reading' 
                        'Sheffield United' 
                        'Stoke City'  
                        'Swansea City' 
                        'West Bromwich Albion')


def getEfl_L1(request):
    return HttpResponse('"EFL League One" teams in aphabet order'
                        'Accrington Stanley'
                        'AFC Wimbledon'
                        'Bolton Wanderers'
                        'Burton Albion'
                        'Cambridge United'
                        'Charlton Athletic'
                        'Cheltenham Town'
                        'Crewe Alexandra'
                        'Doncaster Rovers'
                        'Fleetwood Town'
                        'Gillingham'
                        'Ipswich Town'
                        'Lincoln City'
                        'Milton Keynes Dons'
                        'Morecambe'
                        'Oxford United'
                        'Plymouth Argyle'
                        'Portsmouth'
                        'Rotherham United'
                        'Sheffield Wednesday'
                        'Shrewsbury Town'
                        'Sunderland'
                        'Wigan Athletic'
                        'Wycombe Wanderers')


def getEfl_L2(request):
    return HttpResponse('"EFL League Two" teams in alphabet order'
                        'Barrow'
                        'Bradford City'
                        'Bristol Rovers'
                        'Carlisle United'
                        'Colchester United'
                        'Crawley Town'
                        'Exeter City'
                        'Forest Green Rovers'
                        'Harrogate Town'
                        'Hartlepool United'
                        'Leyton Orient'
                        'Mansfield Town'
                        'Newport County'
                        'Northampton Town'
                        'Oldham Athletic'
                        'Port Vale'
                        'Rochdale'
                        'Salford City'
                        'Scunthorpe United'
                        'Stevenage'
                        'Sutton United'
                        'Swindon Town'
                        'Tranmere Rovers'
                        'Walsall')


def getNL(request):
    return HttpResponse('"National League" teams in alphabet order'
                        'Aldershot Town'
                        'Altrincham'
                        'Barnet'
                        'Boreham Wood'
                        'Bromley'
                        'Chesterfield'
                        'Dagenham & Redbridge'
                        'Dover Athletic'
                        'Eastleigh'
                        'FC Halifax Town'
                        'Grimsby Town'
                        "King's Lynn Town"
                        'Maidenhead United'
                        'Notts County'
                        'Solihull Moors'
                        'Southend United'
                        'Stockport County'
                        'Torquay United'
                        'Wealdstone'
                        'Weymouth'
                        'Woking'
                        'Wrexham'
                        'Yeovil Town')
