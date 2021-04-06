from django.db import models

# Create your models here.

class Student(models.Model):
    """
    学生信息表
    """
    name = models.CharField(verbose_name="姓名", max_length=30)
    age = models.IntegerField(verbose_name="年龄")
    gender = models.CharField(verbose_name='性别', max_length=30, choices=
    (('male', '男'), ('female', '女')), default='男')

    def __str__(self):
        return self.name

class Course(models.Model):
    """
    课程
    """
    name = models.CharField(verbose_name="课程名", max_length=30)
    scores = models.IntegerField(verbose_name="分数")
    major = models.ForeignKey(Student, related_name="student", on_delete=models.CASCADE)