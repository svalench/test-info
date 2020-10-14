from django.urls import path, include

from web.ajax import update_data_user, get_departments, create_or_update_departments
from web.views import Cabinet

namespace = 'web'
urlpatterns = [
    path('', Cabinet.start, name='cabinet'),
    path('add-corparation/', Cabinet.create_corp, name='create_corp'),
    # ajax methods
    path('upd_user/', update_data_user, name='upd_data_user'),
    path('get-deps/', get_departments, name='get_deps_ajax'),
    path('save-or-update/deps/',create_or_update_departments,name='save-or-update-deps'),
]
