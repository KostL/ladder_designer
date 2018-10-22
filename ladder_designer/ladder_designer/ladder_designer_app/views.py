from django.shortcuts import render

def index(request):
    return render(
        request,
        "index.html", 
        {
            'content': "<strong>Hello Django!</strong> on "
        }
    )