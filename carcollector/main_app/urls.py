from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>/', views.cars_detail, name='details'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_oil/', views.add_oil, name='add_oil'),


    path('medals/', views.MedalList.as_view(), name='medals_index'),
    path('medals/<int:pk>/', views.MedalDetail.as_view(), name='medals_detail'),
    path('medals/create/', views.MedalCreate.as_view(), name='medals_create'),
    path('medals/<int:pk>/update/', views.MedalUpdate.as_view(), name='medals_update'),
    path('medals/<int:pk>/delete/', views.MedalDelete.as_view(), name='medals_delete'),

    
    path('cars/<int:car_id>/assoc_medal/<int:medal_id>/', views.assoc_medal, name='assoc_medal'),

     
    path('cars/<int:car_id>/unassoc_medal/<int:medal_id>/', views.unassoc_medal, name='unassoc_medal'),
    path('accounts/signup/', views.signup, name='signup'),
]