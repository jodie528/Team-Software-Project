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

# program

class Aims(models.Model):
    class Meta:
        verbose_name_plural = 'Aims'

    aim = models.TextField(default='')

    def __str__(self):
        return self.aim


class Learnoutcomes(models.Model):
    class Meta:
        verbose_name_plural = 'Learning outcomes'

    l_outcomes = models.TextField(default='')
    aims = models.ForeignKey('Aims', on_delete=False, null=True)

    def __str__(self):
        return self.l_outcomes


class Program_cont(models.Model):
    class Meta:
        verbose_name_plural = 'Program contents'

    Program_title = models.CharField(max_length=32)
    Program_code = models.CharField(max_length=32)
    JACS_Code = models.CharField(max_length=32)
    Level_of_study = models.CharField(max_length=32)
    Final_Qualification = models.CharField(max_length=32)
    QAA_FHEQ_Level = models.CharField(max_length=32)
    Intermediate_Qualification = models.CharField(max_length=120)
    Teaching_Institution = models.CharField(max_length=32)
    Faculty = models.CharField(max_length=32)
    Department = models.CharField(max_length=32)
    Other_Department_involved_in_teaching_the_programm = models.CharField(max_length=32)
    Mode_of_Attendnce = models.CharField(max_length=32)
    Duration_of_the_Programme = models.CharField(max_length=32)
    Date_of_production = models.CharField(max_length=32)
    Accrediting_Professional_or_Statutory_Body = models.CharField(max_length=32)
    Background_to_the_programme_and_subject_area = models.TextField(default='')
    Teaching_learning_and_assessment = models.TextField(default='')
    aims1 = models.ForeignKey('Aims', on_delete=False, null=True)
    aims2 = models.ForeignKey('Aims', on_delete=False, related_name='topic_content_type', null=True)
    aims3 = models.ForeignKey('Aims', on_delete=False, related_name='topic_content_typ', null=True)
    aims4 = models.ForeignKey('Aims', on_delete=False, related_name='topic_content_ty', null=True)
    aims5 = models.ForeignKey('Aims', on_delete=False, related_name='topic_content_t', null=True)
    l_outcomes1 = models.ForeignKey('Learnoutcomes', on_delete=False, null=True)
    l_outcomes2 = models.ForeignKey('Learnoutcomes', on_delete=False, related_name='topic_con', null=True)
    l_outcomes3 = models.ForeignKey('Learnoutcomes', on_delete=False, related_name='topic_content', null=True)
    l_outcomes4 = models.ForeignKey('Learnoutcomes', on_delete=False, related_name='topic_conten', null=True)
    l_outcomes5 = models.ForeignKey('Learnoutcomes', on_delete=False, related_name='topic_conte', null=True)

    def __str__(self):
        return self.Program_title
