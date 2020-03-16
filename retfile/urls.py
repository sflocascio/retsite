"""retfile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.contrib.auth.models import User
#from core.backends import HomeRegistrationView
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path,  include
from core import views
from django.conf.urls.static import static
from django.contrib.auth.models import User
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.index, name='home'),
    path('process', views.process, name='process'),
    path('process_v2', views.process_v2, name='process_v2'),
    #path('create_object', views.create_object, name='create_object'),
    #path('create_object_new', views.create_object_new, name='create_object_new'),
    path('create_object_form', views.create_object_form, name='create_object_form'),
    path('create_session_form', views.create_session_form, name='create_session_form'),
    #path('upload_file', views.upload_file, name='upload_file'),
    path('admin/', admin.site.urls),
    path('<pk>/', views.session_detail, name='session_detail'),
    path('<pk>/detail/upload', views.upload_screenshot, name='upload_screenshot'),
    path('<pk>/detail/', views.session_detail_v2, name='session_detail_v2'),
    path('<pk>/detail/update', views.update_technology_cell_id, name='update_technology_cell_id'),
    path('<pk>/detail/atenna', views.process_antenna_file, name='process_antenna_file'),
    path('<pk>/table/', views.session_table, name='session_table'),
    path('<pk>/export/', views.export_csv, name='export_csv'),
    path('<pk>/delete', views.delete_all_files, name='delete_all_files'),
    # path('accounts/', include('registration.backends.simple.urls')),
    # path('accounts/register/',
    #     HomeRegistrationView.as_view(),
    #     name="registration_register"),
    

    # path(
    #     'accounts/password/reset/',
    #     PasswordResetView.as_view(
    #         template_name='registration/password_reset_form.html'),
    #     name="password_reset"),
    # path(
    #     'accounts/password/reset/done/',
    #     PasswordResetView.as_view(
    #         template_name='registration/password_reset_done.html'),
    #     name="password_reset_done"),
    # path(
    #     'accounts/password/reset/<uidb64>/<token>/',
    #     PasswordResetConfirmView.as_view(
    #         template_name='registration/password_reset_confirm.html'),
    #     name="password_reset_confirm"),
    # path(
    #     'accounts/password/done/',
    #     PasswordResetCompleteView.as_view(
    #         template_name='registration/password_reset_complete.html'),
    #     name="password_reset_complete"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
