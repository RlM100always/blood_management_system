from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="login"),
    path("logout/", views.user_logout, name="logout"),
    path("home/", views.home, name="home"),
    path("admin_dashboard/", views.admin_dashboard, name="admin_dashboard"),
    path("donor_dashboard/", views.donor_dashboard, name="donor_dashboard"),

    # Custom admin panel URLs
    path("manage/blood_banks/", views.blood_bank_list, name="blood_bank_list"),
    path("manage/blood_banks/create/", views.blood_bank_create, name="blood_bank_create"),
    path("manage/blood_banks/<int:pk>/", views.blood_bank_detail, name="blood_bank_detail"),
    path("manage/blood_banks/<int:pk>/update/", views.blood_bank_update, name="blood_bank_update"),
    path("manage/blood_banks/<int:pk>/delete/", views.blood_bank_delete, name="blood_bank_delete"),

    path("manage/donors/", views.donor_list, name="donor_list"),
    path("manage/donors/<int:pk>/", views.donor_detail, name="donor_detail"),

    path("manage/blood_requests/", views.blood_request_list, name="blood_request_list"),
    path("manage/blood_requests/<int:pk>/approve/", views.approve_blood_request, name="approve_blood_request"),
    path("manage/blood_requests/<int:pk>/reject/", views.reject_blood_request, name="reject_blood_request"),

    path("manage/donations/", views.donation_list, name="donation_list"),
    path("manage/donations/create/", views.donation_create, name="donation_create"),
    path("manage/donations/<int:pk>/approve/", views.approve_donation, name="approve_donation"),
    path("manage/donations/<int:pk>/reject/", views.reject_donation, name="reject_donation"),
    path("manage/donations/<int:pk>/update/", views.donation_update, name="donation_update"),

    # Donor URLs
    path("donor/profile/", views.donor_profile, name="donor_profile"),
    path("donor/make_request/", views.make_blood_request, name="make_blood_request"),
    path("donor/donation_history/", views.donor_donation_history, name="donor_donation_history"),
    path("donor/blood_requests/", views.donor_blood_requests, name="donor_blood_requests"),

    path("", views.home, name="root"),
]
