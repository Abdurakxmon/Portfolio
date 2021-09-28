from django.urls import path
from .import views
app_name = 'about_me'
urlpatterns = [
    path('', views.index, name='index'),
    path('<str:portfolio_slug>', views.PortfolioViewDetail.as_view(), name='portfolio_detail'),

]