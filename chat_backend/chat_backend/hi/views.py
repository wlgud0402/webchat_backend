from django.shortcuts import render, HttpResponse

# Create your views here.


def hi(request):
    print("버튼 눌러서 하이요청받음")
    return HttpResponse("하이 들어옴")
