from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Create your views here.
def input_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'password': request.POST["password"]
        }
        if form["username"] and form["password"]:
            user = authenticate(username=form["username"],password=form["password"])
            if user is None:
                form['errors'] = u"Такой пользователь не зарегестрирован!"
                return render(request, 'auth.html', {'form': form})
            else:
                login(request, user)
            return redirect('archive')
        else:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'auth.html', {'form': form})
    else:
        return render(request, 'auth.html', {})

def create_user(request):
    if request.method == "POST":
        form = {
            'username': request.POST["username"],
            'mail': request.POST["mail"],
            'password': request.POST["password"]
        }
        art = None
        try:
            art = User.objects.get(username=form["username"])
            art = User.objects.get(email=form["mail"])
            # если юзер существует, то ошибки не произойдет и
            # программа удачно доберется до следующей строчки
            print (u"Такой юзер уже есть")
        except User.DoesNotExist:
            print (u"Такого юзера ещё нет")
        if form["username"] and form["mail"] and form["password"] and art is None:
            art = User.objects.create(username=form["username"],
                                      email=form["mail"],
                                      password=form["password"])
            return redirect('archive')
        else:
            if art is not None:
                form['errors'] = u"Логин или почта уже заняты"
            else:
                form['errors'] = u"Не все поля заполнены"
            return render(request, 'registration.html', {'form': form})
    else:
        return render(request, 'registration.html', {})