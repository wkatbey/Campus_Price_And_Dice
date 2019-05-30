from django.urls import path
from . import views

app_name = 'campus'
urlpatterns = [
    path('', views.index, name='index'),
    path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
    path('save_restaurant/', views.save_restaurant, name='save_restaurant'),
    path('restaurant_list/', views.restaurant_list, name='restaurant_list'),
    path('<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('delete_restaurant_<int:restaurant_id>/', views.delete_restaurant, name='delete_restaurant'),
    path('add_item/', views.add_item, name='add_item'),
    path('load_item/<int:item_id>/<int:restaurant_id>', views.load_item, name='load_item'),
    path('user_profile/', views.user_profile, name='user_profile' ),
    path('delete_item_<int:restaurant_id>_<int:item_id>/', views.delete_item, name='delete_item'),
]