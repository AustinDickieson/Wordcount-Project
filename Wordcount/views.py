#Need http response, cant just send string
from django.http import HttpResponse
#allows http returns

from django.shortcuts import render
import operator

#urls.py sends as request object
def home(request):
    return render(request,'home.html')
    #need to send to home.html

def about(request):
    return render(request,'about.html')

def count(request):
    fulltext = request.GET['fulltext']
    #gets the entered text from home.html and stores in fulltext
    wordlist = fulltext.split()
    #splits string into list by spaces

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            #Increase count
            worddictionary[word] += 1
        else:
            #add to dictionary
            worddictionary[word] = 1

    sortedwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse= True)
    #sorts dictionary into list

    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'sortedwords':sortedwords})
    #returns count.html page and puts fulltext in dictionary with key named fulltext


#URL->Views->html
#urls.py->views.home->home.html
