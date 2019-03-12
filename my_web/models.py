from django.db import models


class module_info(models.Model):

    mod_id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=32)
    title = models.CharField(max_length=32)
    smester_taught = models.CharField(max_length=32)
    smester_asses = models.CharField(max_length=32)
    location = models.CharField(max_length=64)
    date = models.CharField(max_length=64)
    credit = models.PositiveIntegerField(default=0)
    description = models.CharField(max_length=100)
    special_restriction = models.CharField(max_length=128)
    qualification = models.CharField(max_length=128)

class mod_TLM(models.Model):

    type = models.CharField(max_length=32)
    actual_hour = models.IntegerField(default=0)
    scheduled_hour_num = models.IntegerField(default=0)
    scheduled_hour_perc = models.IntegerField(default=0)
    placement_hour_num = models.IntegerField(default=0)
    placement_hour_perc = models.IntegerField(default=0)
    independ_hour_num = models.IntegerField(default=0)
    independ_hour_perc = models.IntegerField(default=0)
    description = models.CharField(max_length=64)
    mod = models.ForeignKey('module_info', on_delete=models.CASCADE)

class mod_AM(models.Model):

    type = models.CharField(max_length=64)
    proportion_mark = models.IntegerField(default=0)
    num_of_hour = models.IntegerField(default=0)
    word_length = models.IntegerField(default=0)
    written = models.IntegerField(default=0)
    course_work = models.IntegerField(default=0)
    practical = models.IntegerField(default=0)
    description = models.CharField(max_length=64)
    mod = models.ForeignKey('module_info', on_delete=models.CASCADE)

class mod_contact(models.Model):

    name = models.CharField(max_length=16)
    depart = models.CharField(max_length=32)
    institution = models.CharField(max_length=32,default='Sheffield')
    email = models.CharField(max_length=32)
    mod = models.ForeignKey('module_info', on_delete=models.CASCADE)

class mod_aims_lo(models.Model):

    type = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    content = models.CharField(max_length=128)
    mod = models.ForeignKey('module_info', on_delete=models.CASCADE)

class mod_TM_AM_links(models.Model):

    type = models.CharField(max_length=32)
    link = models.CharField(max_length=32)
    content = models.CharField(max_length=64)
    mod = models.ForeignKey('module_info', on_delete=models.CASCADE)

class mod_requisites(models.Model):
    pre = models.CharField(max_length=32)
    co = models.CharField(max_length=32)
    excluded = models.CharField(max_length=32)
    mod = models.ForeignKey('module_info', on_delete=models.CASCADE)

