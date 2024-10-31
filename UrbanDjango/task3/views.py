from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')


def shop(request):
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay 2'

    games = {
        game1: '2899 руб.',
        game2: '3499 руб.',
        game3: '1999 руб.',
    }
    return render(request, 'third_task/games.html', {'games': games})


def cart(request):
    return render(request, 'third_task/cart.html')
