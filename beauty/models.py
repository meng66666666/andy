from django.db import models

# Create your models here.
class VIP(models.Model):
    vipName = models.CharField(max_length=20,verbose_name='会员名')
    vipPwd = models.CharField(max_length=20,verbose_name='会员密码')

    def __str__(self):
        return self.vipName

    class Meta:
        db_table = 'vip'
        verbose_name = '会员'
        verbose_name_plural = verbose_name