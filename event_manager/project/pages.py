from django.shortcuts import render


def error_404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'account/login.html')


def register(request):
    return render(request, 'account/sign-up.html')


# ====================================================
#         Dashboard methods
# =======================================================
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
