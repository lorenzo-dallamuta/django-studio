from django.db import models
# from django.db.models.deletion import CASCADE, SET_NULL
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from accounts.models import User


class Medico(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    data_assunzione = models.DateField()
    specialita = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Medici'

    def __str__(self):
        return f"{self.nome} {self.cognome}"


# class Paziente(models.Model):
#     user = models.OneToOneField(User, on_delete=CASCADE)
#     # medico = models.ForeignKey(Medico, null=True, on_delete=SET_NULL)

#     def __str__(self):
#         return f"{self.nome} {self.cognome}"

#     @receiver(post_save, sender=User)
#     def create_user_profile(sender, instance, created, **kwargs):
#         if created:
#             Paziente.objects.create(user=instance)

#     @receiver(post_save, sender=User)
#     def save_user_profile(sender, instance, **kwargs):
#         instance.profile.save()


class Studio(models.Model):
    nome = models.CharField(max_length=50)
    indirizzo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    medico = models.ManyToManyField('Medico')

    class Meta:
        verbose_name_plural = 'Studi'

    def __str__(self):
        return self.nome
