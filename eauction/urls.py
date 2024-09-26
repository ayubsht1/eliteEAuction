from django.contrib import admin
from django.urls import path
from .views import HomeView, AuctionView, SellItemsView, WatchListView,CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('auction-list/', AuctionView.as_view(), name='auction-list'),
    path('sell-items/', SellItemsView.as_view(), name='sell-items'),
    path('watch-list/', WatchListView.as_view(), name='watch-list'),
    path('category/', CategoryView.as_view(), name='category'),
    
]
