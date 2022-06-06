from pyexpat import model
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
TEHSIL = (
    ('bakalavr','Bakalavr'),
    ('migistr','Magistr'),
    ('doktorant','Doktorant')
)
DERECE = (
    ('fd','Felsefe Doktoru'),
    ('ed','Elmler DOktoru')

)
VEZIFE = (
    ('assis','Assistent'),
    ('bm','Bas Muellim'),
    ('d','Dossent'),
    ('p','Professor')

)
GENDER = (
    ('k','Kisi'),
    ('q','Qadin')
)

BOLME = (
    ('az','AZE'),
    ('ru','RUS'),
    ('eng','ENG')
)
AILE_VEZ = (
    ('e','Evli'),
    ('s','Subay')
)



class Teacher(models.Model):
    ad = models.CharField(max_length=50)
    soyad = models.CharField(max_length=50)
    ata_adi = models.CharField(max_length=50)
    tehsil = models.CharField(max_length=25, choices=TEHSIL)
    elmi_derece = models.CharField(max_length=25, choices=DERECE,null=True,blank=True)
    vezife = models.CharField(max_length=25, choices=VEZIFE,null=True,blank=True)
    gender = models.CharField(max_length=25, choices=GENDER,null=True,blank=True)
    fenler = ArrayField(models.IntegerField(),blank=True,null=True)
    bolme = models.CharField(max_length=25,choices=BOLME)
    dogum_tarixi = models.CharField(max_length=25,blank=True,null=True)
    doguldugu_yer = models.CharField(max_length=25,blank=True,null=True)
    bitirdiyi_universitet = models.CharField(max_length=50)
    ixtisas = models.ForeignKey('Ixtisas',on_delete=models.CASCADE)
    aile_vezyeti = models.CharField(max_length=25,choices=AILE_VEZ)
    partiya_mensubiyeti = models.CharField(max_length=150,blank=True,null=True)
    main_work = models.CharField(max_length=150,blank=True,null=True)
    herbi_mukellefiyet = models.BooleanField()
    faktiki_yasaadigi_unvan = models.CharField(max_length=250)
    qeydiyatda_oldugu_unvan = models.CharField(max_length=250)
    #elmi_meqalelerin_sayi = models.ForeignKey()


class Ixtisas(models.Model):
    ad = models.CharField(max_length=80)
    kod = models.CharField(max_length=25)    



class Fen(models.Model):
    adi = models.CharField(max_length=100)

"""
Table -- >Teacher :
ad
soyad
ata_adi
tehsil --> static --> bakalavr,magisrt,doktorant
elmi_derece --> static --> null=True,blank=True --> Felsefe doktoru,Elmler doktoru
vezifesi --> static --> assistent,bas muellim,dosent,professor
gender --> static --> qadin,kisi
fennler --> arrayfield[fen(idler)]
bolme --> static --> Az,Rus,Eng
dogum_tarixi --> DateField -- olmadi Sting field
doguldugu_yeri --> string
bitirdiyi_ali_mekteb --> string 
ixtisas --> ForeingKey(Ixtisas)
ale_veziyeti --> static --> Evli,Subay
partiya_mensubiyeti --> string --> null=True,blank=True
main_work --> string
herbi_mukellefiyet --> boolean --> he,yox (True,False)
faktiki_yasaadigi_unvan --> string 
qeydiyatda_oldugu_unvan --> string
elmi_meqalelerin_sayi --> BUNA BAX MENIM TABLEIM DAN GELMELIDI



Ixtisas --> Table:
adi --> string 
kodu --> int


Teble --> Fen:
id
adi
"""