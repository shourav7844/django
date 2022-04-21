from django.contrib import auth, messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from parking_app.models import registration


def home(request):
    return render(request, 'firstPage.html')


def redirect_url(request):
    if request.POST.get('logInSubmit') == 'SIGN_IN':
        return render(request, 'login/login.html')
    else:
        return render(request, 'register/form.html')


def save(request):
    if request.method == "POST":
        name = request.POST.get('NAME')
        email = request.POST.get('EMAIL')
        password = request.POST.get('PASSWORD')
        try:
            InsertInDatabaseVariable = registration(name=name, email_address=email, password=password)
            RegistrationOK = InsertInDatabaseVariable.save()
            # return render(request, 'register/thankyou.html')
            if RegistrationOK:
                return render(request, 'login/login.html')
        except Exception:
            messages.warning(request, message="Duplicate email detected..!!")

    return render(request, 'register/form.html')

    # return render(request, 'register/form.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('EMAIL')
        password = request.POST.get('PASSWORD')

        user = auth.authenticate(Email_address=email, Password=password)
        if registration.objects.filter(email_address__exact=email).exists():
            user_exists = registration.objects.filter(email_address__exact=email, password__exact=password)
            if user_exists:
                auth.login(request, user)
                return render(request, 'register/thankyou.html')
            else:
                messages.error(request, message="Wrong Password. Please Try again..")
        else:
            messages.error(request, message="UnAuthorized Access Detected...!!")

    return render(request, 'login/login.html')


def thankyou(request):
    return render(request, 'register/thankyou.html')


def firstPage(request):
    return render(request, 'firstPage.html')


def register(request):
    return render(request, 'register/form.html')
