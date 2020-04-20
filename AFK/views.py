from django.http import HttpResponse
from django.shortcuts import render




def home(request):
    #return HttpResponse('home')
    return render(request, 'home.html')

def blog(request):
    #return HttpResponse('blog')
    return render(request, 'blog.html')

def games(request):
    #return HttpResponse('games')
    return render(request, 'games.html')
def contact(request):
    #return HttpResponse('contact')
    return render(request, 'contact.html')

def gamesingle(request):
    #return HttpResponse('gamesingle')
    return render(request, 'gamesingle.html')

def review(request):
    #return HttpResponse('review')
    return render(request, 'review.html')


    


