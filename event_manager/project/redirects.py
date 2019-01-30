from database import models
from database.database_methods import register_new_user, get_hashed_password, create_event, remove_event_from_db, \
    get_event
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .forms import EventForm
from django.shortcuts import redirect, HttpResponse, render


def validate_user(request):
    result = ''
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = authenticate(request, username=mail, password=get_hashed_password(password))

        print(user)

        if user is not None:
            if user.is_active:
                if remember == 'on':
                    login(request, user)
                return redirect('/account/dashboard')
            else:
                result = 'user is suspended!'
        else:
            print("Someone tried to login and failed.")
            print("They used Mail: {} and Password: {}".format(mail, password))
            result = 'mail or password is wrong'
    else:
        result = 'please use POST method'

    return render(request, 'registration/login.html', {'result': result})


def register(request):
    if request.method == 'POST':
        mail = request.POST.get('mail')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        cellphone = request.POST.get('cellphone')
        confirm_password = request.POST.get('confirm_password')

        if not confirm_password == password:
            result = 'passwords not match!'
        else:

            dic = {
                'mail': mail,
                'password': password,
                'first_name': first_name,
                'last_name': last_name,
                'cellphone': cellphone,
            }

            user = register_new_user(dic)
            if user is not None:
                return redirect('dashboard')
            else:
                result = 'user already exists'

                # send an activation mail to user
        return render(request, 'registration/sign-up.html', {'result': result})
        # return redirect(request, 'registration/sign-up.html', {'result': result})
    #
    #     else:
    #         print(user_form.errors, profile_form.errors)
    # else:
    #     user_form = UserForm()
    #     profile_form = UserProfileInfoForm()
    # return render(request, 'dappx/registration.html',
    #               {'user_form': user_form,
    #                'profile_form': profile_form,
    #                'registered': registered})


def logout_user(request):
    logout(request)

    return redirect('/')


@login_required
def create_new_event(request):
    title = request.POST.get('title')
    banner = request.FILES['banner']
    start_date = request.POST.get('start_date')
    body = request.POST.get('body')

    if title is not None and banner is not None and start_date is not None and body is not None:
        create_event(title, body, banner, start_date)
        result = 'event created'
    else:
        result = 'wrong parameters'

    return redirect('account/dashboard-new-event', {'result': result})


@login_required
def accept_request(request):
    return None


@login_required
def remove_event(request):
    e_id = request.GET.get('event')
    remove_event_from_db(e_id)
    return redirect('account/dashboard-event-list')


@login_required
def edit_event(request):
    e_id = request.GET.get('event')
    # form = EventForm(instance=get_event(e_id))

    return render(request, 'events/edit-event.html', {'event': get_event(e_id)})
