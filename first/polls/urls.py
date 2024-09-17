from django.urls import path
from . import views
#헤헤 오줌발싸
app_name = "polls"
urlpatterns = [
    path("", views.index, name = "index"), #ex: /polls/
    path("<int:question_id>/", views.detail, name="detail"), #ex: /polls/5
    path("<int:question_id>/results", views.results, name="results"), #ex: /polls/5/results
    path("<int:question_id>/vote/", views.vote, name = "vote") #ex: /polls/5/vote
    ]