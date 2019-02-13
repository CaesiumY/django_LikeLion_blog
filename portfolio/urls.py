from django.urls import path
import portfolio.views

urlpatterns = [
    path('', portfolio.views.portfolio, name="portfolio"),
]
