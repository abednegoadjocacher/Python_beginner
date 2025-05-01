from django.shortcuts import render # type: ignore
from django.http import HttpResponse # type: ignore
from.models import InFo
# Create your views here.




#second_info=InFo()


def index(request):
    #I have created a new data from the admin dashboard
    #first_info= InFo()
    #first_info.author="ADJOCACHER ABEDNEO"
    #first_info.date= '12/02/2025'
    #first_info.details= """I am computer science who is more of backend development.
    #I used Django framework to set up my own portfolio website."""
   #
    #second_info= InFo()
    #second_info.author="ADJOCACHER ABEDNEO"
    #second_info.date= '26/09/2022'
    #second_info.details= """I love to code in python.
    #Python is a friendly programming language for beginners"""
    #
    #third_info= InFo()
    #third_info.author="ADJOCACHER ABEDNEO"
    #third_info.date= '21/11/2023'
    #third_info.details= """I have learnt to fill my mind with positivity. 
    #I always think of myself not going to achieve anything. 
    #The moment I read a book that speaks of the 
    #'The power Of Positive Thinking', my fear of inferiority, the impossible changed.
    #I now tell myself I can become the Backend developer I want to become. 
    #I always see myself doing the work of backend in mind and keep learning to achieve it.
    #'I can do All Things Through Christ that strengthens ME'."""

    # making a list of the info's and using in the frontend
    #info_s=[first_info,second_info,third_info]
    information=InFo.objects.all()
    return render(request, 'index.html',{'information':information})#'info':first_info, 'info_1':second_info, 'info_2':third_info,'info_s':info_s

def counter(request):
    text_count = request.POST['text']
    number_of_words = len(text_count.split())
    return render(request, 'counter.html', {'words_count': number_of_words})
def aboutMe(request):
    author='Abednego Adjocacher'
    return render(request, 'about.html', {'myname': author})