from django.urls import path
from . import views

app_name = "farms"

urlpatterns = [
    path('',views.HomeView.as_view(), name="home"),
    path('contact/',views.ContactView.as_view(),name="contact"),
    path('categories/',views.categories,name="categories"),
    path('crop/<slug:slug>/',views.detail, name="crop-detail"),
    path('advisories/',views.advisories,name="advisories"),
    path('about-us/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('create-news/',views.CreateNews.as_view(), name="news")
]
