from django.shortcuts import render, Http404, redirect

# from django.contrib.auth import login, authenticate
from django.contrib.auth.views import login_required
from database.database_methods import get_active_events, get_all_events, get_users_count, join_user_in_event, \
    find_event, find_joined_uesr, get_request_list
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.views.decorators.csrf import csrf_protect


def error_404(request):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)


def home(request):
    active_events = get_active_events()
    print(active_events)
    all_events = get_all_events()
    users_count = get_users_count()

    page = request.GET.get('page', 1)

    paginator = Paginator(active_events, 6)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    user_request_status = []
    if request.user.is_authenticated:
        user_request_status = []
        for event in events:
            e = find_joined_uesr(event, request.user)
            if e is None:
                user_request_status.append(-1)
            else:
                user_request_status.append(e)

    return render(request, 'home.html', {'activeEventCount': len(active_events),
                                         'totalEvents': len(all_events), 'usersCount': users_count,
                                         'events': events, 'status_list': user_request_status})


def login(request):
    # if request.user.is_authenticated:
    #     HttpResponseRedirect('/account/dashboard')
    # else:
    return render(request, 'registration/login.html')


def register(request):
    return render(request, 'registration/sign-up.html')


# ====================================================
#         Dashboard methods
# =======================================================
@login_required
def dashboard(request):
    return render(request, 'base_dashboard.html')


@login_required
def dashboard_event_list(request):
    active_events = get_active_events()
    print(active_events)
    all_events = get_all_events()
    users_count = get_users_count()

    page = request.GET.get('page', 1)

    paginator = Paginator(active_events, 6)
    try:
        events = paginator.page(page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(paginator.num_pages)

    user_request_status = []
    if request.user.is_authenticated:
        user_request_status = []
        for event in events:
            e = find_joined_uesr(event, request.user)
            if e is None:
                user_request_status.append(-1)
            else:
                user_request_status.append(e)
    return render(request, 'account/dashboard-event-list.html', {'activeEventCount': len(active_events),
                                                                 'totalEvents': len(all_events),
                                                                 'usersCount': users_count,
                                                                 'events': events})


@login_required
def dashboard_new_event(request):
    return render(request, 'account/dashboard-new-event.html')


# ====================================================
#         event methods
# =======================================================
@login_required
def join_event(request):
    event = request.GET.get('event')
    user = request.user

    if join_user_in_event(user, event):
        return redirect('events/event-info?event=' + event)
    return Http404()


def event_info(request):
    event = request.GET.get('event')

    event = find_event(event)
    is_user_joined_event = None

    if request.user.is_authenticated:
        is_user_joined_event = find_joined_uesr(event, request.user)

    if event is None:
        return render(request, '404.html', status=404)
    else:
        if is_user_joined_event is not None:
            return render(request, 'events/event-info.html',
                          {'event': event, 'status': is_user_joined_event.status})
        else:
            return render(request, 'events/event-info.html',
                          {'event': event, 'status': -1})


@login_required
def dashboard_requests(request):
    requests = get_request_list()

    page = request.GET.get('page', 1)

    paginator = Paginator(requests, 10)
    try:
        requests = paginator.page(page)
    except PageNotAnInteger:
        requests = paginator.page(1)
    except EmptyPage:
        requests = paginator.page(paginator.num_pages)

    return render(request, 'account/dashboard-requests.html', {'requests': requests})
