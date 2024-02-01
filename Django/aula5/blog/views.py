from django.shortcuts import render
from django.http import HttpResponseRedirect

def feed(request):
    context = {
        'posts':[
            {'autor': 'fulano', 'date': '01/02/2024', 'content':'asfacnwqeoimcqie'},
            {'autor': 'ciclano', 'date': '01/02/2023', 'content':'asfacnwqeoimcqie'},
            {'autor': 'beltrano', 'date': '01/02/2025', 'content':'asfacnwqeoimcqie'}
        ]
    }
    return render(request, 'feed.html', context)

def publicate(request):
    if request.method =='POST':
        author = request.POST.get('author')
        content = request.POST.get('content')
        print(author)
        print(content)
        return HttpResponseRedirect('/feed')
    else:
        return render(request, 'publicate.html')


