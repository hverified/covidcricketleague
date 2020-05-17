from django.shortcuts import render


def indexView(request):

    return render(request, "index.html", {})


def contactView(request):

    return render(request, "contact.html", {})
