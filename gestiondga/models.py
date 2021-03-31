from django.db import models

# Create your models here.

class Representante (models.Model):
    cedula = models.CharField(max_length=11, primary_key=True)
    nombre_rep = models.CharField(max_length=50, null=False, blank=False, verbose_name="Nombre Representante Legal")

    def __str__(self):
        txt= "{0} Cedula: {1} " 
        return txt.format(self.nombre_rep, self.cedula)

class Municipio (models.Model):
    nombre_mpio = models.CharField(max_length=25, primary_key=True)
    codigo_mpio = models.CharField(max_length=5)

    def __str__(self):
        return self.nombre_mpio

class DGA (models.Model):
    id_dga = models.AutoField(primary_key=True)
    #id_empresa = models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)
    nombre_responsable = models.CharField(max_length=50, null=False, blank = False)
    nivel_estudio = models.CharField(max_length=22)
    titulo = models.CharField(max_length=25)
    cargo = models.CharField(max_length=25, null=False, blank = False)
    email_dga = models.EmailField()

    #def __str__(self):
        #txt= "{0} Responsable: {1} Cargo:{2} " 
        #return txt.format(self.id_dga, self.nombre_responsable, self.cargo)

class Empresa (models.Model):
    nit = models.CharField(max_length=11, primary_key=True)
    razon_social = models.CharField(max_length=64, null=False, blank = False)
    codigo_ciiu = models.CharField(max_length=5)
    camara = models.CharField(max_length=6)
    municipio = models.ForeignKey(Municipio, null=False, blank=False, on_delete=models.CASCADE)
    direccion = models.CharField(max_length=32, null=False, blank = False)
    telefono = models.CharField(max_length=11, null=False, blank = False)
    correo = models.CharField(max_length=32, null=False, blank = False)
    pagina_web = models.CharField(max_length=25)
    cedula_representante = models.ForeignKey(Representante, null=False, blank=False, on_delete=models.CASCADE) 
    tiposE = [
        ('GRANDE', 'GRANDE'),
        ('MEDIANA' ,'PEQUEÑA'),
        ('PEQUEÑA', 'PEQUEÑA'),
        ('MICRO', 'MICRO')
    ]
    tipo_empresa = models.CharField(max_length=7, choices=tiposE, default='GRANDE', verbose_name="Su Empresa es:")
    tiposGDA = [
        ('INTERNO', 'INTERNO'),
        ('EXTERNO' ,'EXTERNO'),
        ('APOYO GREMIO', 'APOYO GREMIO')
    ]
    tipo_gda = models.CharField(max_length=12, choices=tiposGDA, default='INTERNO', verbose_name="Tipo Departamento Gestion Ambiental")
    fecha_registro_emp = models.DateField()
    fecha_creacion_dga = models.DateField()
    tipodecreto =[
        ('SI', 'SI'),
        ('NO', 'NO')
    ]
    decreto_1076 = models.CharField(max_length=2, choices=tipodecreto, default='SI')
    sector_productivo = models.CharField(max_length=25)
    Responsable_DGA = models.ForeignKey(DGA, null=False, blank=False, on_delete=models.CASCADE) 

    def __str__(self):
        txt= "{0} NIT: {1} " 
        return txt.format(self.razon_social, self.nit)

class Funcionario(models.Model):
    id_funcionario= models.CharField(max_length=11)
    nombre = models.CharField(max_length=50, null=False, blank = False)
    cargo = models.CharField(max_length=25)

    def __str__(self):
        txt= "{0} NIT: {1} " 
        return txt.format(self.nombre, self.cargo)

class Seguimiento(models.Model):
    id = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa, null=False, blank=False, on_delete=models.CASCADE)
    id_funcionario = models.ForeignKey(Funcionario, null=False, blank=False, on_delete=models.CASCADE)
    fecha_seg = models.DateField()
    resultado = models.CharField(max_length=64)

