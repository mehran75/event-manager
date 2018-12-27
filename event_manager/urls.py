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
from django.urls import path
from django.conf.urls import handler404
from event_manager.project import pages


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pages.home, name='home'),

    path('account/login', pages.login, name='Login'),
    path('account/sign-up', pages.register, name='sign-up'),

    path('account/dashboard', pages.dashboard, name='dashboard'),
    path('account/dashboard-event-list', pages.dashboard_event_list, name='dashboard-event-list'),
    path('account/dashboard-new-event', pages.dashboard_new_event, name='dashboard-new-event'),

    path('events/event-id', pages.event_id, name='event info'),
    path('events/new-event', pages.new_event, name='new event'),
]

