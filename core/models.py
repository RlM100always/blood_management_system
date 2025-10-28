from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_donor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

class BloodBank(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

class Donor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    blood_group = models.CharField(max_length=5, choices=[
        ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")
    ])
    date_of_birth = models.DateField(blank=True, null=True)
    last_donation_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.username

class BloodRequest(models.Model):
    request_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blood_requests")
    blood_group = models.CharField(max_length=5, choices=[
        ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")
    ])
    units_required = models.PositiveIntegerField()
    urgency = models.CharField(max_length=50, choices=[
        ("Low", "Low"), ("Medium", "Medium"), ("High", "High"), ("Emergency", "Emergency")
    ])
    request_date = models.DateTimeField(auto_now_add=True)
    is_approved = models.BooleanField(default=False)
    fulfilled_by_blood_bank = models.ForeignKey(BloodBank, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Blood Request for {self.blood_group} by {self.request_by.username}"

class Donation(models.Model):
    donor = models.ForeignKey(Donor, on_delete=models.CASCADE, related_name="donations")
    blood_bank = models.ForeignKey(BloodBank, on_delete=models.CASCADE, related_name="received_donations")
    donation_date = models.DateField(auto_now_add=True)
    blood_group = models.CharField(max_length=5, choices=[
        ("A+", "A+"), ("A-", "A-"), ("B+", "B+"), ("B-", "B-"),
        ("AB+", "AB+"), ("AB-", "AB-"), ("O+", "O+"), ("O-", "O-")
    ])
    units_donated = models.PositiveIntegerField()
    status = models.CharField(max_length=50, choices=[
        ("Pending", "Pending"), ("Approved", "Approved"), ("Rejected", "Rejected")
    ], default="Pending")

    def __str__(self):
        return f"Donation by {self.donor.user.username} on {self.donation_date}"

