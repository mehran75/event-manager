from django.shortcuts import render, HttpResponseRedirect

# from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login_required
from django.views.decorators.csrf import csrf_protect


def error_404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def home(request):
    return render(request, 'home.html', {'activeEventCount': 0, 'totalEvents': 0, 'usersCount': 0})


def login(request):
    # if request.user.is_authenticated:
    #     HttpResponseRedirect('/account/dashboard')
    # else:
    print('here')
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/sign-up.html')


# ====================================================
#         Dashboard methods
# =======================================================
@login_required
def dashboard(request):
    return render(request, 'base_dashboard.html')


def dashboard_event_list(request):
    return render(request, 'account/dashboard-event-list.html')


def dashboard_new_event(request):
    return render(request, 'account/dashboard-new-event.html')


# ====================================================
#         event methods
# =======================================================

def event_id(request):
    return render(request, 'events/event-info.html')


def new_event(request):
    return render(request, 'events/dashboard-new-event.html')
