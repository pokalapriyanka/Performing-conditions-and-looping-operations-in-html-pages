from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':20,'b':300,'c':40}
    return render(request,'condition.html',d)

def loops(request):
    d={'name':'Priya'}
    return render(request,'loop.html',context=d)