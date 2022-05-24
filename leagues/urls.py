from django.urls import path

from . import views, views_team

urlpatterns = [
    # path('add_league/', views_leagues.addLeague, name='add_league'),
    # path('add_team/', views_team.addTeam,  name='add_team'),
    # path('add_user/', views_leagues.addUser,  name='add_user'),
    # path('<league>/<team>', views.getTeams),
    # path('<league>', views.getLeagues),
    path('404', views.NotFound),
    path('getusers/', views.getUser)

    # path('EPL/', views.getEPL),
    # path('EFL_Championship/', views.getEflChamp),
    # path('EFL_League_One/', views.getEfl_L1),
    # path('EFL_League_Two/', views.getEfl_L2),
    # path('National_League/', views.getNL),
]