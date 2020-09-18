from django.db import models


class Education(models.Model):
    degree = models.CharField(max_length=200)
    course = models.TextField()
    institution = models.CharField(max_length=200)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    description = models.TextField()
    user = models.ForeignKey('Person',  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.degree


class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=100)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    user = models.ForeignKey('Person',  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}, {self.company}"


class AwardsAndHonour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    user = models.ForeignKey('Person',  on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.title}, {self.date}"


class Person(models.Model):
    name = models.CharField(max_length=200)
    about = models.TextField()
    title = models.CharField(max_length=200)
    # image = models.FilePathField(path="/img")

    def __str__(self):
        return self.name


class Contact(models.Model):
    AddressType = models.TextChoices('AddressType', 'Current Permanent')

    address = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=14)
    user = models.ForeignKey('Person',  on_delete=models.CASCADE, null=True)
    address_type = models.CharField(blank=True, choices=AddressType.choices, max_length=12)

    def __str__(self):
        return self.address_type
