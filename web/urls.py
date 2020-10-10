from django.urls import path, include

from web.views import Cabinet

namespace='web'
urlpatterns = [
    path('',Cabinet.start,name='cabinet')
    ]