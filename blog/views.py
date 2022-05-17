from django.shortcuts import render

# Creating views
def index(request):
    return render(request, "blog/index.html")