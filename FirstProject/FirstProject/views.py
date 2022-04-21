#I've created the file - Shourav
from django.http import HttpResponse
from django.shortcuts import render

#Code for video-6 .. Initial learning
# def index(request):
#     return HttpResponse('''<h1>Hello</h1><a href="https://www.google.com/">Google</a>''')

# def about(request):
#     return HttpResponse("About")

# def file1(request):
#     file2 = open("Basic_abbreviation.txt", 'r+')
#     return HttpResponse(file2.read())

def index(request):
    params = {'name':'Shourav', 'place':'BD'}
    return render(request, 'index.html', params)

def Output(request):
    mod = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    print(mod)
    print(removepunc)
    print(uppercase)

    analyzed = ""
    punctuation = '''![]{}.;~'''
    if removepunc == 'on':
        for char in mod:
            if char not in punctuation:
                analyzed = analyzed + char
        mod = analyzed
    if uppercase == 'on':
        analyzed = mod.upper()

    if removepunc != 'on' and uppercase != 'on':
        analyzed = mod

    dict1 = {'modified':mod, 'analyzed':analyzed}
    return render(request, 'output.html', dict1)

def Output2(request):
    mod2 = request.GET.get('text2','default')
    dict2 = {'modified2':mod2}
    print(mod2)
    return render(request, 'another.html', dict2)


def newEndpoint(request):
    return render(request, 'EndpointPage.html')

def EndpointOutput(request):
    outputText = request.GET.get('EndpointText', 'default')
    outputText1 = request.GET.get('EndpointText1', 'default')

    EndpointDictionary = { 'output':outputText, 'output1':outputText1}
    return render(request, 'EndpointOutputPage.html',EndpointDictionary)