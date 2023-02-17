import datetime

from django.db.models import Q
from django.shortcuts import render
from myfiles. models import *
# Create your views here.
def index(malumot):
    if 'sabject' in malumot.POST:
        emile = malumot.POST.get('mile')
        Email(email=emile).save()
    if 'WORD' in malumot.POST:
        text = str(malumot.POST.get('WORD'))
        print(text)


        text = text.strip()
        qidrish = Q(nomi__startswith = text)| Q(company_name__startswith = text)|\
                  Q(date__startswith = text)| Q(url__startswith = text)|\
                  Q(malumot__startswith = text)| Q(tur__nomi__startswith = text)

        works = Portfoliyo.objects.filter(qidrish)
        turlar = Type.objects.all()
        team = Team.objects.all()
        return render(malumot, 'index.html', {'works': works, 'tur': turlar, 'team': team},)


    elif malumot.method == "POST":
        ismi = malumot.POST.get('name')
        mail = malumot.POST.get('email')
        mavzu = malumot.POST.get('subject')
        xabar = malumot.POST.get('message')
        vaqt = datetime.datetime.now()

        Murojaat(name=ismi,mail=mail,title=mavzu,text=xabar,date=vaqt).save()


    works = Portfoliyo.objects.all()
    turlar = Type.objects.all()
    team = Team.objects.all()
    return render(malumot, 'index.html', {'works': works, 'tur': turlar, 'team': team},)

def filter(malumot):
    work = Portfoliyo.objects.filter(tur_id=id)
    return render(malumot,'index.html',{'work': work})

def portfolio(malumot):
    return render(malumot,'portfolio-details.html')

def singele_portfolilo(malumot, id):
    work = Portfoliyo.objects.get(id=id)
    return render(malumot,'portfolio-details.html', {'work': work})
