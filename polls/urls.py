from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    # i.e. /polls/
    path('', views.IndexView.as_view(), name='index'),
    # i.e. /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #i.e. /polls/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #i.e. /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
