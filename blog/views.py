from django.shortcuts import render

posts = [
    {
     'auther' : 'Waleed',
     'title' : 'django post',
     'content' : ' first yeah!',
     'posted_date' : 'Aug 27, 2018'
    },
    {
     'auther' : 'Obada',
     'title' : 'django post',
     'content' : ' first yeah!',
     'posted_date' : 'Aug 30, 2018'
    },

 ]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

