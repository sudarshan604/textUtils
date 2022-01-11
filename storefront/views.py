from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def analyze(request):
    dtext = request.POST.get('text', 'default ')
    removePunch = request.POST.get('remove', 'default')
    upper = request.POST.get('upper', 'default')
    removeLine = request.POST.get('removeL', 'default')

    analyze = dtext
    punction = "& '#$ !( ) * + - % / : ; < = > ? @ [ \ ] _ { | } ~ ¡ ¦ § ¨ © « ¬ ® °&^"

    if removePunch == "on":
        for char in dtext:
            if char not in punction:
                analyze = analyze+char

    if upper == "on":
        analyze = analyze.upper()

    if removeLine == "on":
        analyze = ""
        for char in dtext:
            if char != "\n" and char != "\r":
                analyze = analyze+char
            else:
                print("no")
    params = {'purpose': 'remove punctuation',
              'analyzed_text': analyze}

    return render(request, "analyze.html", params)
