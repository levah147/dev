from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"lynx/index.html")

def contact (request):
    return render(request, "core/contact.html")