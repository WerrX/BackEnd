from django.db import models
#treba inheret from model class
from django.db import models


#ked vytvorime class Films inherneme z classy models.Model
class Films(models.Model):
    #davame tu teraz atributy 4o chceme aby to malo, a davame mu max dlzku
    name = models.CharField(max_length=100)
    #foto = models.CharField(max_length=50)
    foto = models.ImageField(null=True, blank=True)
    description = models.CharField(max_length=2000)

    def __str__(self):
        return self.name

# aby sme vytvorili tabulku v databaze treba urobit migrations pomocou : python manage.py makemigrations Films
#nezabudnit aby to bolo aj v setting instoled apps
# nakoneiec aby to v databaze zobrazovalo treba zadat koment : python manage.py migrate, aplie vsetky migracie ktore este neboli appliaed
#nakoniec treba ist do admin.py -> dalsie kroky tam
#ak chceme zmenit nazov z file object napiseme


