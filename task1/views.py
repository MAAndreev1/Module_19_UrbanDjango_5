from django.shortcuts import render
from django.http import HttpResponse
from task1.models import *


# Create your views here.
def main_template(request):
    pagename = 'Главная страница'
    context = {'pagename': pagename,}
    return render(request, 'menu.html', context)

def shop_template(request):
    pagename = 'Игры'
    games = Game.objects.all()
    context = {
        'games': games,
        'pagename': pagename,
    }
    return render(request, 'shop_template.html', context)

def basket_template(request):
    pagename = 'Корзина'
    context = {'pagename': pagename,}
    return render(request, 'basket_template.html', context)

def sign_up_by_html(request):
    user_list = Buyer.objects.all()
    info = {}
    context = {'info': info,}

    if request.method == 'POST':
            # Получаем данные:
            username = request.POST.get('username')
            password = request.POST.get('password')
            repeat_password = request.POST.get('repeat_password')
            age = request.POST.get('age')

            # Обработка данных:
            if password == repeat_password and int(age) >= 18:

                for user in user_list:
                    if str(username) == user.name:
                        info.update({'error': 'Пользователь уже существует'})
                        return render(request, 'registration_page.html', context)
                # Если пользователь новый
                Buyer.objects.create(name=username, balance=1000, age=age)
                # Http ответ пользователю:
                return HttpResponse(f"Приветствуем нового пользователя, {username}!")

            else:

                if password != repeat_password:
                    info.update({'error': 'Пароли не совпадают'})
                elif int(age) < 18:
                    info.update({'error': 'Вы должны быть старше 18'})
                return render(request, 'registration_page.html', context)

    # Если это GET
    return render(request, 'registration_page.html', context)
