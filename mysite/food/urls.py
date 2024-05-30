from django.urls import path
from . import views

app_name = 'food'
urlpatterns = [
    #/food/
    # function based views 
    #path('', views.index, name='index'),
    # class based or generic views 
    path('', views.IndexClassView.as_view(), name='index'),
    #/food/1
    # function based views 
    #path('<int:item_id>/', views.detail,name='detail'),
    # class based or generic views 
    path('<int:pk>/', views.FoodDetail.as_view(),name='detail'),
    path('item/',views.item,name='item'),
    #add items
    # function based views
    #path('add',views.create_item,name='create_item'),
    # class based or generic views 
    path('add',views.CreateItem.as_view(),name='create_item'),
    #edit items
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete items
    path('delete/<int:id>/',views.delete_item,name='delete_item'),
]