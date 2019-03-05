#from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context ={}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)

def receive_data(request):
    if request.POST:
        print('有提交')

    #select = request.POST.get('select', None)

    text = request.POST.get('text', None)
    print(text)
    return render(request, 'print.html', locals())