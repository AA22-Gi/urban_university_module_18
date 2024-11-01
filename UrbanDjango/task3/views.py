from django.shortcuts import render


# Create your views here.
def platform(request):
    return render(request, 'third_task/platform.html')


def shop(request):
    game1 = 'Atomic Heart - 1499 руб. '
    game2 = 'Cyberpunk 2077 - 3499 руб. '
    game3 = 'PayDay 2 - 1999 руб. '

    games = {
        'game1': game1,
        'game2': game2,
        'game3': game3,
    }
    return render(request, 'third_task/games.html', games)


def cart(request):
    return render(request, 'third_task/cart.html')
