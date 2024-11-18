from django.shortcuts import render,redirect
from app1.models import Movie
# Create your views here.
def home(request):
    m = Movie.objects.all()  ##select * from
    context = {'movie': m}
    return render(request, 'home.html',context)

def addmovies(request):
    if (request.method == "POST"):  ##it is a dictionary
        t = request.POST['t']
        d = request.POST['d']
        l = request.POST['l']
        yr = request.POST['yr']
        img = request.FILES['img']

        m = Movie.objects.create(title=t, description=d,language=l,year=yr,image=img)  ##insert into
        m.save()
        return redirect('home')

    return render(request,'add.html')


def desc(request,p):
    m=Movie.objects.get(id=p)
    context={'movie':m}

    return render(request,'description.html',context)

def delete(request,p):
    m=Movie.objects.get(id=p)
    m.delete()

    return redirect('home')


def edit(request, p):
        k = Movie.objects.get(id=p)
        if (request.method == "POST"):
            k.title = request.POST['t']
            k.description = request.POST['d']
            k.language = request.POST['l']
            k.year = request.POST['yr']

            if (request.FILES.get('img') == None):
                k.save()
            else:
                k.image = request.FILES.get('img')

            k.save()

            return redirect("home") #goto the home page in return after submission

        context = {'movie': k}

        return render(request, 'edit.html', context)

