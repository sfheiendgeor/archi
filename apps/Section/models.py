from django.db import models

class FB_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)

    class Meta:
        verbose_name = 'FB断面性能'
        verbose_name_plural = 'FB断面形状一覧'

    def __str__(self):
        return str(self.name)
    
    
class R_data(models.Model):
    name = models.CharField(max_length = 50)
    d = models.FloatField('d',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)

    class Meta:
        verbose_name = '棒鋼断面性能'
        verbose_name_plural = '棒鋼断面形状一覧'

    def __str__(self):
        return str(self.name)
    
    
class I_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    t1 = models.FloatField('t1',blank=True, null=True)
    t2 = models.FloatField('t2',blank=True, null=True)
    r1 = models.FloatField('r1',blank=True, null=True)
    r2 = models.FloatField('r2',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)
    Ix = models.FloatField('Ix',blank=True, null=True)
    Iy = models.FloatField('Iy',blank=True, null=True)
    rx = models.FloatField('rx',blank=True, null=True)
    ry = models.FloatField('ry',blank=True, null=True)
    Zx = models.FloatField('Zx',blank=True, null=True)
    Zy = models.FloatField('Zy',blank=True, null=True)

    class Meta:
        verbose_name = 'I形鋼断面性能'
        verbose_name_plural = 'I形鋼断面形状一覧'

    def __str__(self):
        return str(self.name)
    
    
class H_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    t1 = models.FloatField('t1',blank=True, null=True)
    t2 = models.FloatField('t2',blank=True, null=True)
    r1 = models.FloatField('r1',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)
    Ix = models.FloatField('Ix',blank=True, null=True)
    Iy = models.FloatField('Iy',blank=True, null=True)
    rx = models.FloatField('rx',blank=True, null=True)
    ry = models.FloatField('ry',blank=True, null=True)
    Zx = models.FloatField('Zx',blank=True, null=True)
    Zy = models.FloatField('Zy',blank=True, null=True)

    class Meta:
        verbose_name = 'H形鋼断面性能'
        verbose_name_plural = 'H形鋼断面形状一覧'

    def __str__(self):
        return str(self.name)

    
class LH_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    t1 = models.FloatField('t1',blank=True, null=True)
    t2 = models.FloatField('t2',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)
    Ix = models.FloatField('Ix',blank=True, null=True)
    Iy = models.FloatField('Iy',blank=True, null=True)
    rx = models.FloatField('rx',blank=True, null=True)
    ry = models.FloatField('ry',blank=True, null=True)
    Zx = models.FloatField('Zx',blank=True, null=True)
    Zy = models.FloatField('Zy',blank=True, null=True)

    class Meta:
        verbose_name = '軽量H形鋼断面性能'
        verbose_name_plural = '軽量H形鋼断面形状一覧'

    def __str__(self):
        return str(self.name)
    
    
class CT_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    t1 = models.FloatField('t1',blank=True, null=True)
    t2 = models.FloatField('t2',blank=True, null=True)
    r1 = models.FloatField('r1',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)
    Ix = models.FloatField('Ix',blank=True, null=True)
    Iy = models.FloatField('Iy',blank=True, null=True)
    rx = models.FloatField('rx',blank=True, null=True)
    ry = models.FloatField('ry',blank=True, null=True)
    Zx = models.FloatField('Zx',blank=True, null=True)
    Zy = models.FloatField('Zy',blank=True, null=True)

    class Meta:
        verbose_name = 'CT形鋼断面性能'
        verbose_name_plural = 'CT形鋼断面形状一覧'

    def __str__(self):
        return str(self.name)


class C_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    t1 = models.FloatField('t1',blank=True, null=True)
    t2 = models.FloatField('t2',blank=True, null=True)
    r1 = models.FloatField('r1',blank=True, null=True)
    r2 = models.FloatField('r2',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)
    Ix = models.FloatField('Ix',blank=True, null=True)
    Iy = models.FloatField('Iy',blank=True, null=True)
    rx = models.FloatField('rx',blank=True, null=True)
    ry = models.FloatField('ry',blank=True, null=True)
    Zx = models.FloatField('Zx',blank=True, null=True)
    Zy = models.FloatField('Zy',blank=True, null=True)

    class Meta:
        verbose_name = 'C形鋼断面性能'
        verbose_name_plural = 'C形鋼断面形状一覧'

    def __str__(self):
        return str(self.name)
    
    
class RC_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    C = models.FloatField('C',blank=True, null=True)
    t1 = models.FloatField('t1',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)
    Ix = models.FloatField('Ix',blank=True, null=True)
    Iy = models.FloatField('Iy',blank=True, null=True)
    rx = models.FloatField('rx',blank=True, null=True)
    ry = models.FloatField('ry',blank=True, null=True)
    Zx = models.FloatField('Zx',blank=True, null=True)
    Zy = models.FloatField('Zy',blank=True, null=True)

    class Meta:
        verbose_name = 'リップ溝形鋼断面性能'
        verbose_name_plural = 'リップ溝形鋼断面形状一覧'

    def __str__(self):
        return str(self.name)
    

class O_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H', blank=True, null=True)
    t1 = models.FloatField('t1', blank=True, null=True)
    A = models.FloatField('A', blank=True, null=True)
    m = models.FloatField('m', blank=True, null=True)
    Ix = models.FloatField('Ix', blank=True, null=True)
    rx = models.FloatField('rx', blank=True, null=True)
    Zx = models.FloatField('Zx', blank=True, null=True)

    class Meta:
        verbose_name = '鋼管断面性能'
        verbose_name_plural = '鋼管断面形状一覧'

    def __str__(self):
        return str(self.name)
    
    
class P_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H', blank=True, null=True)
    B = models.FloatField('B', blank=True, null=True)
    t1 = models.FloatField('t1', blank=True, null=True)
    A = models.FloatField('A', blank=True, null=True)
    m = models.FloatField('m', blank=True, null=True)
    Ix = models.FloatField('Ix', blank=True, null=True)
    Iy = models.FloatField('Iy', blank=True, null=True)
    rx = models.FloatField('rx', blank=True, null=True)
    ry = models.FloatField('ry', blank=True, null=True)
    Zx = models.FloatField('Zx', blank=True, null=True)
    Zy = models.FloatField('Zy', blank=True, null=True)

    class Meta:
        verbose_name = '角型鋼管断面性能'
        verbose_name_plural = '角型鋼管断面形状一覧'

    def __str__(self):
        return str(self.name)
    
    
class L_data(models.Model):
    name = models.CharField(max_length = 50)
    H = models.FloatField('H',blank=True, null=True)
    B = models.FloatField('B',blank=True, null=True)
    t1 = models.FloatField('t1',blank=True, null=True)
    t2 = models.FloatField('t2',blank=True, null=True)
    r1 = models.FloatField('r1',blank=True, null=True)
    A = models.FloatField('A',blank=True, null=True)
    m = models.FloatField('m',blank=True, null=True)
    Ix = models.FloatField('Ix',blank=True, null=True)
    Iy = models.FloatField('Iy',blank=True, null=True)
    rx = models.FloatField('rx',blank=True, null=True)
    ry = models.FloatField('ry',blank=True, null=True)
    Zx = models.FloatField('Zx',blank=True, null=True)
    Zy = models.FloatField('Zy',blank=True, null=True)

    class Meta:
        verbose_name = '山形鋼断面性能'
        verbose_name_plural = '山形鋼断面形状一覧'

    def __str__(self):
        return str(self.name)






