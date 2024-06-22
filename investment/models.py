from django.db import models


class Investment(models.Model):
    date = models.DateField(verbose_name="তারিখঃ")
    name = models.CharField(max_length=100, verbose_name="নিয়োগকারী নামঃ")
    quantity = models.FloatField(verbose_name="টাকার পরিমাণ")
    other_info = models.CharField(max_length=200, verbose_name="মন্তব্যঃ")
    log = models.TextField(verbose_name='লগ', blank=True)

    class Meta:
        verbose_name = 'বিনিয়োগ'
        verbose_name_plural = 'বিনিয়োগ সংক্রান্ত তথ্য'

    def __str__(self):
        return f"{self.date} - {self.name}"


class Land(models.Model):
    date = models.DateField(verbose_name='তারিখঃ')
    gher = models.CharField(max_length=100, verbose_name='ঘেরঃ')
    mouza = models.CharField(max_length=100, verbose_name='মৌজাঃ')
    dag_number = models.CharField(max_length=100, verbose_name='দাগ কত?')
    khatian_number = models.CharField(max_length=100, verbose_name='খতিয়ান নম্বরঃ')
    land_area = models.FloatField(verbose_name='কত শতাংশ')
    cultivable_land = models.FloatField(verbose_name='লেন জমিঃ')
    adjacent_land = models.FloatField(verbose_name='পাড়, ক্যানেলের পরিমাণ')
    owners_name = models.CharField(max_length=100, verbose_name='মালিকদের নাম')
    comments = models.TextField(max_length=200, verbose_name='মন্তব্যঃ')
    log = models.TextField(verbose_name='লগ', blank=True)

    class Meta:
        verbose_name = 'জমি লিজ'
        verbose_name_plural = 'জমি লিজ সংক্রান্ত তথ্য'

    def __str__(self):
        return f"{self.date} - {self.gher}"


class Staff(models.Model):
    date = models.DateField(verbose_name='তারিখঃ')
    name = models.CharField(max_length=100, verbose_name='নাম:')
    post = models.CharField(max_length=100, verbose_name='পদঃ')
    salary = models.FloatField(verbose_name='বেতন')
    address = models.CharField(max_length=400, verbose_name='ঠিকানাঃ')
    number = models.CharField(max_length=100, verbose_name='মোবাইল নাম্বার:')
    comments = models.TextField(max_length=100, verbose_name='মন্তব্যঃ')
    log = models.TextField(verbose_name='লগ', blank=True)

    class Meta:
        verbose_name = 'ষ্টাফ নিয়োগ'
        verbose_name_plural = 'ষ্টাফ নিয়োগ তথ্য'

    def __str__(self):
        return f"{self.date} - {self.name}"
