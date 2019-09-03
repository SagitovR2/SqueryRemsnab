from django.db import models


class Type(models.Model):
    type = models.CharField(max_length=15)

    def add(self):
        self.save()

    def get_typeofapplience(self):
        return [i.type for i in Type.objects.all()]


class Bringing(models.Model):
    date = models.DateField()
    comment = models.TextField()

    def add(self):
        self.save()


class Abduction(models.Model):
    date = models.DateField()
    comment = models.TextField()

    def add(self):
        self.save()


class Repair(models.Model):
    information = models.TextField()

    def add(self):
        self.save()


class People(models.Model):
    name = models.CharField(max_length=50)
    bringing = models.ForeignKey(Bringing, on_delete=models.PROTECT, null=True)
    abduction = models.ForeignKey(Abduction, on_delete=models.PROTECT, null=True)
    repair = models.ForeignKey(Repair, on_delete=models.PROTECT, null=True)


class Applience(models.Model):
    number_of_applience = models.IntegerField()
    typeofapplience = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    bringing = models.ForeignKey(Bringing, on_delete=models.PROTECT, null=True)
    abduction = models.ForeignKey(Abduction, on_delete=models.PROTECT, null=True)
    repair = models.OneToOneField(Repair, on_delete=models.PROTECT, null=True)

    def add(self):
        self.save()
