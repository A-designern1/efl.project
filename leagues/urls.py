from django.urls import path

from . import views

urlpatterns = [
    path('404', views.NotFound),
    path('<league_name>', views.getLeagues)
    # path('EPL/', views.getEPL),
    # path('EFL_Championship/', views.getEflChamp),
    # path('EFL_League_One/', views.getEfl_L1),
    # path('EFL_League_Two/', views.getEfl_L2),
    # path('National_League/', views.getNL),
]