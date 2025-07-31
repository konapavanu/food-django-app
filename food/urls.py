
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name='food'
urlpatterns = [
   path('',views.index,name='index'),
   path('<int:item_id>/',views.detail,name='detail'),
   # path('item',views.item,name='item'),  
   # add item
   path('add/',views.create_item,name='create_item'),
   # update item
   path('update/<int:id>/',views.update_item,name='update_item'),
   #delete item
   path('delete/<int:id>/',views.delete_item,name='delete_item')
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
