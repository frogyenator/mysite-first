from django.db import models

# Create your models here.
class User(models.Model):
    gender = (
        ('male','男'),
    ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True,verbose_name='用户名')
    password = models.CharField(max_length=256)
    email = models.EmailField('邮箱',unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男',verbose_name='性别')
    c_time = models.DateTimeField('注册时间',auto_now_add=True)
    has_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-c_time']
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name

class ConfirmString(models.Model):
    code = models.CharField(max_length=256)
    user = models.OneToOneField('User')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.name + ": " + self.code

    class Meta:
        ordering = ['-c_time']
        verbose_name = '确认码'
        verbose_name_plural = verbose_name