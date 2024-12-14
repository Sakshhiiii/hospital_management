from django.db import models


# Create your models here.
class Doctor(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.IntegerField()
    special=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Patient(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    mobile=models.IntegerField(null=True)
    # mobile no. v=can be blank also
    address=models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    # DOCTORS NAME WILL COME FROM DOCTOR TABLE SO FOREIGN KEY IS USED
    # AND WHEN A DOCTOR IS DELETED FROM THE DOCTOR TABLE IT IS DELETED FROM THE APPOINTMENT TABLE ALSO
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE) # same for patient also
    date1=models.DateField()
    time1=models.TimeField()


    def __str__(self):
        return self.doctor.name+"--"+self.patient.name
    

        