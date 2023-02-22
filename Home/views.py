from django.shortcuts import render, redirect, HttpResponse
from .models import Contact
from django.contrib import messages
from Blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def index(request):
    pubDate = {
        "month": "February 22, 2023"
    }
    return render(request, "home/index.html", pubDate)


def about(request):
    return render(request, "home/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("contact")
        msg = request.POST.get("msg")

        if not(len(name) < 3 or len(email) < 5 or len(phone) < 12 or len(msg)< 20):
            form = Contact(name=name, email=email, phone=phone, msg=msg)
            form.save()
            messages.success(request, "Ваше сообщение было успешно отправлено администратору !")
        else:
            messages.error(request, "Заполните форму правильно!")
    return render(request, "home/contact.html")

def search(request):
    query = request.GET.get('query')

    if len(query) > 100:
        allPosts = Post.objects.none()
        messages.warning(request, "Запрос слишком большой !")

    else:
        allTitle = Post.objects.filter(title__icontains=query)
        allContent = Post.objects.filter(text__icontains=query)
        allAuthor = Post.objects.filter(author__icontains=query)
        allDates = Post.objects.filter(timeStamp__icontains=query)
        allPosts = allTitle.union(allContent, allAuthor, allDates)

    if allPosts.count() < 1:
        messages.warning(request, "Результат поиска не найден")

    context = {
        "allPosts": allPosts,
        "query": query
    }
    return render(request, 'home/search.html', context=context)

def userSignup(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get("pass2")

        if pass1 == pass2:
            user = User.objects.create_user(username=username, email=email, password=pass2)
            user.first_name = fname
            user.last_name = lname
            user.save()
            messages.success(request,  "Ваш учетная запись успешно создана")

            return redirect("/")
        return HttpResponse("404 - Не верный запрос")

def userLogin(request):
    if request.method == "POST":
        loginusername = request.POST.get("loginusername")
        loginpass = request.POST.get("loginpass")

        user = authenticate(request, username=loginusername, password=loginpass)

        if user is not None:
            login(request, user=user)
            messages.success(request, "Вы успешно вошли")
            return redirect("/")

        else:
            messages.error(request, "Неверный логин или пароль ")
            return redirect("/")

    return HttpResponse("404 - Плохой запрос")


def userLogout(request):
    logout(request)
    messages.success(request, "Вы успешно вышли")
    return redirect("/")
