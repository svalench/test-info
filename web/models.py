from django.contrib.auth.models import User
from django.db import models


class Corparations(models.Model):
    """
    модель для предприятий
    """
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="who created")
    name = models.CharField("Name corparation", max_length=255)


class Depatments(models.Model):
    """
    модель для отделов предприятия
    """
    corp_id = models.ForeignKey(Corparations, on_delete=models.CASCADE, verbose_name="corp id")
    name = models.CharField("Name department", max_length=255)


class Roles(models.Model):
    """
    модель с должностями для пользователей
    """
    corp_id = models.ForeignKey(Corparations, on_delete=models.CASCADE, verbose_name="corp id")
    name = models.CharField("Name role", max_length=255)


class Employees(models.Model):
    """
    модель для сотрудников предприятия в которой ему назначется принадлежность к нему (предприятию), должность
    и цех (подразделение)
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="user id")
    corp_id = models.ForeignKey(Corparations, on_delete=models.CASCADE, verbose_name="corp id")
    role_id = models.ForeignKey(Roles, on_delete=models.SET_NULL,null=True, verbose_name="user id")
    dep_id = models.ForeignKey(Depatments, on_delete=models.SET_NULL, null=True, verbose_name="department id")
