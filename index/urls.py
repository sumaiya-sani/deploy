
from django.urls import path
from . views import page


from . import views
urlpatterns = [

    path('index',views.page, name="index")
]
