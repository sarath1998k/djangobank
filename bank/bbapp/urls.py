from . import views
from django.urls import path,include
app_name='bbapp'
urlpatterns = [
    path('',views.index,name='index'),
    path('account/', views.account, name='account'),
    path('ajax/load-branches/',views.load_branches, name='ajax_load_branches'),
    path('success/', views.success, name='success'),
]
