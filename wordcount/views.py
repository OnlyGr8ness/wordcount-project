from django.http import HttpResponse
from django.shortcuts import render
import operator

def home_page(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def count(request):
    fullText = request.GET['fullText']
    wordlist = fullText.split()
    wordDic = {}

    for word in wordlist:
        if word in wordDic:
            #Increase
            wordDic[word] += 1
        elif word.isalpha():
            #add to wordDic
            wordDic[word] = 1
        else:
            pass

    sorted_words = sorted(wordDic.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fullText':fullText, 'count':len(wordlist), 'sorted_words':sorted_words})
