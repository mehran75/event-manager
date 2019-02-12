"""event_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from event_manager.project import pages, redirects
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.home, name='home'),

    path('account/', include('django.contrib.auth.urls')),
    # path('account/login', pages.login, name='login'),
    path('account/sign-up', pages.register, name='sign-up'),

    path('account/dashboard', pages.dashboard, name='dashboard'),
    # path('account/dashboard-messages', pages.dashboard_message, name='dashboard-messages'),
    path('account/dashboard-event-list', pages.dashboard_event_list, name='dashboard-event-list'),
    path('account/dashboard-new-event', pages.dashboard_new_event, name='dashboard-new-event'),
    path('account/dashboard-requests', pages.dashboard_requests, name='dashboard-requests'),

    path('events/event-info', pages.event_info, name='event info'),
    path('events/edit-event', redirects.edit_event, name='edit-event'),

    # redirects
    path('account/validate-user', redirects.validate_user, name='validate-user'),
    path('account/register', redirects.register, name='register'),
    path('account/logout-user', redirects.logout_user, name='logout'),
    path('join-event', pages.join_event, name='join-event'),
    path('create-event', redirects.create_new_event, name='create-event'),
    path('remove-event', redirects.remove_event, name='create-event'),

    path('accept-request', redirects.accept_request, name='accept-request'),
    path('reject-request', redirects.reject_request, name='reject-request'),
]
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
