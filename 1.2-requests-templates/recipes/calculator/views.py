from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def home_view(request):
    pages = {
        'Главная страница': reverse('home'),
        'Рецепт омлета': reverse('omlet'),
        'Рецепт пасты': reverse('pasta'),
        'Рецепт бутерброда': reverse('buter'),
    }
    context = {
        'pages': pages
    }
    return render(request, 'home_page.html', context)


def omlet_view(request):
    count = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'яйца, шт': 2 * count,
            'молоко, л': 0.1 * count,
            'соль, ч.л.': 0.5 * count,
        }
    }
    return render(request, 'calculator/index.html', context)


def pasta_view(request):
    count = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'макароны, г': 0.3 * count,
            'сыр, г': 0.05 * count,
        }
    }
    return render(request, 'calculator/index.html', context)


def buter_view(request):
    count = int(request.GET.get('servings', 1))
    context = {
        'recipe': {
            'хлеб, ломтик': 1 * count,
            'колбаса, ломтик': 1 * count,
            'сыр, ломтик': 1 * count,
            'помидор, ломтик': 1 * count,
        }
    }
    return render(request, 'calculator/index.html', context)
