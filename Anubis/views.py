from django.shortcuts import render


def index(request):
    context = {}

    return render(request, 'system/index.html', context)
