from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = 'eauction/home.html'

class AuctionView(TemplateView):
    template_name = 'eauction/auctions/auction_list.html'

class SellItemsView(TemplateView):
    template_name = 'eauction/seller/sell_items.html'

class WatchListView(TemplateView):
    template_name = 'eauction/watchlist/watch_list.html'

class CategoryView(TemplateView):
    template_name = 'eauction/category/category.html'

