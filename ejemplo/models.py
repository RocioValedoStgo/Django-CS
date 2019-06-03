# from django.db import models
# from django.utils import timezone

# # Create your models here.

# class Ejemplo(models.Model) :
#     V1 = 'V1'
#     V2 = 'V2'
#     V3 = 'V3'
#     V4 = 'V4'

#     CATEGORIA_CHOICES = (
#         (V1, 'v1'),
#         (V2, 'v2'),
#         (V3, 'v3'),
#         (V4, 'v4'),
#     )

#     ejemplo_id = models.AutoField(primary_key = True)
#     name = models.CharField(max_length=100, null=True )
#     release_date = models.DateField()
#     list = models.CharField(max_length=10, choices = CATEGORIA_CHOICES)

#     class Meta:
#         db_table = "ejemplo"

# class Profile(models.Model) :

#     # profile_id = models.AutoField(primary_key = True)

#     name = models.CharField(max_length=50, null=False)
#     ap_pat = models.CharField(max_length=50, null=False)
#     ap_mat = models.CharField(max_length=50, null=False)
#     year = models.IntegerField(null = False)
#     delete = models.BooleanField(default = False) #Para hacer un update de ese regidtro
#     created = models.DateTimeField(default = timezone.now)
#     edited = models.DateTimeField(blank=True, null=True, default=None)

#     class Meta:
#         db_table = "Profile"

