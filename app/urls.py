from django.urls import path
from .views import HotListView,HotListCategoryView,HotListFeaturedView,ProductsItemViews

urlpatterns = [
    path('hotProducts', HotListView.as_view()),
    path('category', HotListCategoryView.as_view()),
    path('featured', HotListFeaturedView.as_view()),
    path('Products', ProductsItemViews.as_view()),
]
