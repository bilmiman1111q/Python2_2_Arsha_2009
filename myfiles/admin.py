from django.contrib import admin
from myfiles.models import *
# Register your models here.

class AdminPortfolio(admin.ModelAdmin):
    list_display = ['id','nomi','company_name','date','url','malumot','tur','rasm1']

admin.site.register(Portfoliyo,AdminPortfolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id','nomi']

admin.site.register(Type,AdminType)

class AdminServise(admin.ModelAdmin):
    list_display = ['id','nomi','malumot','rasm1']

admin.site.register(Servise,AdminServise)

class AdminTeam(admin.ModelAdmin):
    list_display = ['id','ismi','malumot','lavozimi','fecebook_link','instgram_link','tik_tok_link','yutube_link']

admin.site.register(Team,AdminTeam)

class AdminMurojaat(admin.ModelAdmin):
    list_display = ['id','name','mail','title','text','date']

admin.site.register(Murojaat,AdminMurojaat)

class AdminEmil(admin.ModelAdmin):
    list_display = ['id','email']

admin.site.register(Email,AdminEmil)