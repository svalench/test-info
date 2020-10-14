from django.urls import path, include

from web.ajax import update_data_user
from web.views import Cabinet

namespace = 'web'
urlpatterns = [
    path('', Cabinet.start, name='cabinet'),
    path('add-corparation/', Cabinet.create_corp, name='create_corp'),
    path('upd_user/', update_data_user, name='upd_data_user')
]
