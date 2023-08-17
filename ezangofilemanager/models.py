from django.db import models

# Create your models here.

class User(models.Model):

    user_id = models.AutoField(primary_key=True)
    user_type = models.CharField(max_length=20, blank=True)
    username = models.CharField(max_length=30, blank=False)
    firstname = models.CharField(max_length=255, blank=False)
    lastname = models.CharField(max_length=255, blank=False)
    is_connected = models.BooleanField(default=False)


class Client(models.Model):

    cli_id= models.AutoField(primary_key=True)
    cli_name = models.CharField(max_length=255, blank=False)

class Beneficiaire(models.Model):

    ben_id = models.AutoField(primary_key=True)
    ben_name = models.CharField(max_length=255, blank=False)


class Operation(models.Model):
    op_id = models.AutoField(primary_key=True)
    op_ref = models.CharField(max_length=6, unique=True, blank=False, null=False)
    op_type = models.CharField(max_length=255, blank=False, null=False)
    op_cli = models.CharField(max_length=255, blank=False, null=False)
    op_benf = models.CharField(max_length=255, blank=False, null=False)
    op_motif = models.TextField(null=False, blank=False) #TextArea
    op_mtn_dev = models.DecimalField(max_digits=12, decimal_places=2) #gagdet => Textinput dans le HTML
    op_date_creation = models.DateField(auto_now_add=True)
    op_date_dpo_ord = models.DateField(null=False)
    op_date_dpo_etrf = models.DateField(null=False)
    op_date_sort_etrf = models.DateField(null=False)
    op_date_sort_sygma = models.DateField(null=False)
    op_date_dbi_xaf = models.DateField(null=False)
    op_date_crd_awb = models.DateField(null=False)
    op_date_mt103 = models.DateField(null=False)
    op_date_dbi_awb = models.DateField(null=False)
    op_dev = models.CharField(max_length=3)
    op_cvxaf = models.IntegerField(null=False) #gagdet => TextInput
    op_status = models.CharField(max_length=15)
    op_dlai_etrf = models.IntegerField(null=True)
    op_dlai_sygma = models.IntegerField(null=False)
    op_dlai_dxaf = models.IntegerField(null=False)
    op_dlai_crdi_awb = models.IntegerField(null=False)
    op_dlai_mt103 = models.IntegerField(null=False)
    op_dlai_dbi_awb = models.IntegerField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE) #Si pas besoin, on la desactive avec ForeignKey.db_index=False


class Reference(models.Model):

     ref_id = models.AutoField(primary_key=True)
     ref_dos = models.CharField(max_length=6, unique=True)











