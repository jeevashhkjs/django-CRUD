from django.urls import path
from . import views

urlpatterns = [
    path('tutorial', views.user_methods.as_view({'get': 'get_data'})),
    path('tutorial/post', views.user_methods.as_view({'post': 'post_data'})),
    path('tutorial/delete/<int:target_id>', views.user_methods.as_view({'delete': 'delete_data'})),
    path('tutorial/update/<int:target_id>', views.user_methods.as_view({'put': 'update_data'})),
    path('login', views.user_methods.as_view({'post': 'login'})),
    path('logout', views.user_methods.as_view({'post': 'logout'})),
]
