from django.conf.urls import url
from reports import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
]
