from django.urls import path

from . import views_leagues, views_team

urlpatterns = [
    path('404', views_leagues.NotFound),
    path('<league>/<team>', views_team.getTeams),
    path('<league>', views_leagues.getLeagues),
    # path('EPL/', views.getEPL),
    # path('EFL_Championship/', views.getEflChamp),
    # path('EFL_League_One/', views.getEfl_L1),
    # path('EFL_League_Two/', views.getEfl_L2),
    # path('National_League/', views.getNL),
]