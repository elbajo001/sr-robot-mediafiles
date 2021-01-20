from django.db import models
from .validators import num_validation

# Create your models here.
class Customer(models.Model):
    GENRE = [
        ('M', 'masculino'),
        ('F', 'femenino'),
    ]
    AGE = [
        ('1', 'menor de 18 años'),
        ('2', 'entre 19 y 50 años'),
        ('3', 'mayor de 51 años'),
    ]
    document = models.CharField(max_length=20, blank=True, null=True, validators=[num_validation],
                                verbose_name='Documento')
    first_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Nombres')
    last_name = models.CharField(max_length=255, blank=False, null=False, verbose_name='Apellidos')
    genre = models.CharField(choices=GENRE, max_length=1, blank=False, null=False, verbose_name='Género')
    age = models.CharField(choices=AGE, max_length=1, blank=False, null=False, verbose_name='Edad')
    phone_num = models.CharField(max_length=13, blank=False, null=False, unique=True, validators=[num_validation],
                                 verbose_name='Número celular')
    phone_num_wa = models.CharField(max_length=13, blank=True, null=True, validators=[num_validation],
                                    verbose_name='Número whatsapp')
    email_address = models.EmailField(max_length=30, blank=True, null=True,
                                      verbose_name='Dirección correo electrónico')
    home_address = models.CharField(max_length=255, blank=True, null=True,
                                    verbose_name='Dirección residencial')
    office_address = models.CharField(max_length=255, blank=True, null=True,
                                      verbose_name='Dirección oficina')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clientes'
        ordering = ['id']

class Visit(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False, blank=False, default=None, editable=False)
    description = models.TextField(blank=False, null=False, verbose_name='descripción')
    media = models.FileField(blank=True, null=True)
    hour_start = models.TimeField(blank=False, null=False, verbose_name='hora inicio')
    hour_end = models.TimeField(blank=False, null=False, verbose_name='hora fin')
    visit_location = models.CharField(max_length=255, blank=True, null=True, verbose_name='ubicación')
    value = models.FloatField(max_length=10, blank=True, null=True,
                                verbose_name='precio')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Visita'
        verbose_name_plural = 'Visitas'
        db_table = 'visita'
        ordering = ['id']