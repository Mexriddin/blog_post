from django.shortcuts import render
# from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request,"post/homePage.html")


def contact(request):
	return render(request,"post/contact.html", {'values':['Если у вас остались вопросы, то задавайте их мне по телефону', '(99899)***-**-**','user@gmail.com']})