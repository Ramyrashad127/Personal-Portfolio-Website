from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import login, signup, profile, add_project, edit_info, edit_project, select_project, setting, change_password, view_profile, delete_project
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', login, name='login'),
    path('signup/', signup, name='signup'),
    path('profile/', profile, name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('add_project/', add_project, name='add_project'),
    path('edit_info/', edit_info, name='edit_info'),
    path('edit_project/<int:project_id>/', edit_project, name='edit_project'),
    path('select_project/', select_project, name='select_project'),
    path('settings/', setting, name='settings'),
    path('change_password/', change_password, name='change_password'),
    path('view_profile/', view_profile, name='view_profile'),
    path('delete_project/<int:project_id>/', delete_project, name='delete_project'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)