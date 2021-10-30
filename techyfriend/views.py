
from django.http import HttpResponse
from django.shortcuts import render
from pytube import YouTube
import os
pathlist=[]
def homepage(request):
    return render(request, 'Home.html')


def aboutpage(request):
    return render(request, 'About.html')


def contactpage(request):
    return render(request, 'Contact.html')

def productpage(request):
    return render(request, 'Products.html')

 
def contactus(request):
    name = request.GET.get('name')
    email = request.GET.get('email')
    message = request.GET.get('message')
    print(name)
    print(email)
    print(message)
    return (HttpResponse("<h1> Responses are submitted </h1>"))


def user(request):
    return render(request,'passwordmanager.html')

def pdfcompressor(request):
    return render(request,"pdf.html")

def compresspdf(request):
    file = request.FILES['pdffile']
    handle_uploaded_file(file)
    print(file)
    
    return HttpResponse("<h1> File is uploaded </h1>")
def handle_uploaded_file(f):  
    with open('static/upload/'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)  
def youtubedownloader(request):
    return render(request,"youtubehome.html")

def givevideo(pathname):
    print(pathname)
    path=f"static/upload/temp/{pathname}"
    os.chdir(path)
    a=os.listdir()
    file=a[0]
    return HttpResponse(f"<iframe src='{path}/{file}' width=100% height=100%> Video </iframe>")


def downloadvideo(request):
    
   
   
    link=request.GET.get('link')
    print("downloading..>",link)
    video = YouTube(link)
        
    video2 = video.streams.filter(progressive=True)
    title2 = video.title
    import random
    while True:
        a=random.randint(1111111111,9999999999)
        if a in pathlist:
            continue
        else:
            pathlist.append(a)
            break
    name=str(a)
    path=f"static/upload/temp/{name}"
    os.mkdir(path)
    path=f"static/upload/temp/{name}"
    
    file=video2.get_highest_resolution().download(path)
    
   
   

    return givevideo(name)