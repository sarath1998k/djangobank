from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    wiki = models.URLField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'District'
        verbose_name_plural = 'Districts'

    def __str__(self):
        return self.name
class Gender(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Gender'
        verbose_name_plural = 'Genders'

    def __str__(self):
        return self.name

class Branches(models.Model):
    name = models.CharField(max_length=200)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.name

class CardPreference(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Card'
        verbose_name_plural = 'cards'

    def __str__(self):
        return self.name
class AccountPreferance(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.name

class AccountDetails(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    mobile_number = models.CharField(max_length=10)
    address_line_1 = models.CharField(max_length=250)
    gender = models.ForeignKey(Gender, on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey(AccountPreferance, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(Branches, on_delete=models.SET_NULL, null=True)
    card = models.ForeignKey(CardPreference, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'AccountDetail'
        verbose_name_plural = 'AccountDetails'

    def __str__(self):
        return self.first_name