from django.db import models
import datetime
from django.db.models.fields import DateField

# Create your models here.


class employee(models.Model):

    class Meta:
        # テーブル名
        db_table = "employee"
        verbose_name = "アルバイト"  # 追加
        verbose_name_plural = "アルバイト"

    # カラムの定義
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name="名前", max_length=20, unique=True)

    def __str__(self):
        return self.name


class schedule(models.Model):

    class Meta:
        # テーブル名
        db_table = "schedule"
        verbose_name = "シフト予定表"  # 追加

    # カラムの定義
    id = models.AutoField(primary_key=True)
    emp = models.ForeignKey(employee, on_delete=models.PROTECT)
    date = models.DateField(null=True)
    start_at = models.TimeField(null=True)
    end_at = models.TimeField(null=True)

    @classmethod
    def getTodayShift(cls, day):
        TodayShift = cls.objects.filter(
            date=day,
        )
        return TodayShift

    @classmethod
    def getHisShift(cls, name):

        hisShift = cls.objects.filter(
            emp=employee(name=name),
        )
        return hisShift

    def __str__(self):
        return self.id
