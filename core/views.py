
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from .forms import UserRegisterForm, UserLoginForm, DonorProfileForm, BloodBankForm, BloodRequestForm, DonationForm
from .models import User, Donor, BloodBank, BloodRequest, Donation

# Helper functions for role-based access
def is_admin(user):
    return user.is_authenticated and user.is_admin

def is_donor(user):
    return user.is_authenticated and user.is_donor

# Authentication Views
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'registration/login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

# Home and Dashboard Views
@login_required
def home(request):
    if request.user.is_authenticated:
        if request.user.is_admin:
            return redirect('admin_dashboard')
        elif request.user.is_donor:
            return redirect('donor_dashboard')
    return render(request, 'home.html')

@login_required
@user_passes_test(is_admin)
def admin_dashboard(request):
    total_donors = Donor.objects.count()
    pending_donations = Donation.objects.filter(status='Pending').count()
    approved_donations = Donation.objects.filter(status='Approved').count()
    rejected_donations = Donation.objects.filter(status='Rejected').count()
    blood_groups = [bg[0] for bg in Donor.blood_group.field.choices]

    context = {
        'total_donors': total_donors,
        'pending_donations': pending_donations,
        'approved_donations': approved_donations,
        'rejected_donations': rejected_donations,
        'blood_groups': blood_groups,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required
@user_passes_test(is_donor)
def donor_dashboard(request):
    donor = request.user.donor
    donations = donor.donations.all()
    blood_requests = BloodRequest.objects.filter(request_by=request.user)

    context = {
        'donor': donor,
        'donations': donations,
        'blood_requests': blood_requests,
    }
    return render(request, 'donor_dashboard.html', context)

# Admin Features
@login_required
@user_passes_test(is_admin)
def blood_bank_list(request):
    blood_banks = BloodBank.objects.all()
    return render(request, 'admin/blood_bank_list.html', {'blood_banks': blood_banks})

@login_required
@user_passes_test(is_admin)
def blood_bank_detail(request, pk):
    blood_bank = get_object_or_404(BloodBank, pk=pk)
    return render(request, 'admin/blood_bank_detail.html', {'blood_bank': blood_bank})

@login_required
@user_passes_test(is_admin)
def blood_bank_create(request):
    if request.method == 'POST':
        form = BloodBankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blood_bank_list')
    else:
        form = BloodBankForm()
    return render(request, 'admin/blood_bank_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def blood_bank_update(request, pk):
    blood_bank = get_object_or_404(BloodBank, pk=pk)
    if request.method == 'POST':
        form = BloodBankForm(request.POST, instance=blood_bank)
        if form.is_valid():
            form.save()
            return redirect('blood_bank_list')
    else:
        form = BloodBankForm(instance=blood_bank)
    return render(request, 'admin/blood_bank_form.html', {'form': form, 'action': 'Update'})

@login_required
@user_passes_test(is_admin)
def blood_bank_delete(request, pk):
    blood_bank = get_object_or_404(BloodBank, pk=pk)
    if request.method == 'POST':
        blood_bank.delete()
        return redirect('blood_bank_list')
    return render(request, 'admin/blood_bank_confirm_delete.html', {'blood_bank': blood_bank})

@login_required
@user_passes_test(is_admin)
def donor_list(request):
    donors = Donor.objects.all()
    query = request.GET.get('q')
    blood_group_filter = request.GET.get('blood_group')

    if query:
        donors = donors.filter(Q(user__username__icontains=query) | Q(blood_group__icontains=query))
    if blood_group_filter and blood_group_filter != 'All':
        donors = donors.filter(blood_group=blood_group_filter)

    blood_groups = [bg[0] for bg in Donor.blood_group.field.choices]

    context = {
        'donors': donors,
        'blood_groups': blood_groups,
        'selected_blood_group': blood_group_filter,
        'query': query,
    }
    return render(request, 'admin/donor_list.html', context)

@login_required
@user_passes_test(is_admin)
def donor_detail(request, pk):
    donor = get_object_or_404(Donor, pk=pk)
    return render(request, 'admin/donor_detail.html', {'donor': donor})

@login_required
@user_passes_test(is_admin)
def blood_request_list(request):
    blood_requests = BloodRequest.objects.all()
    query = request.GET.get('q')
    blood_group_filter = request.GET.get('blood_group')
    status_filter = request.GET.get('status')

    if query:
        blood_requests = blood_requests.filter(Q(request_by__username__icontains=query) | Q(blood_group__icontains=query))
    if blood_group_filter and blood_group_filter != 'All':
        blood_requests = blood_requests.filter(blood_group=blood_group_filter)
    if status_filter and status_filter != 'All':
        is_approved = True if status_filter == 'Approved' else False
        blood_requests = blood_requests.filter(is_approved=is_approved)

    blood_groups = [bg[0] for bg in BloodRequest.blood_group.field.choices]
    statuses = ['All', 'Approved', 'Pending']

    context = {
        'blood_requests': blood_requests,
        'blood_groups': blood_groups,
        'selected_blood_group': blood_group_filter,
        'statuses': statuses,
        'selected_status': status_filter,
        'query': query,
    }
    return render(request, 'admin/blood_request_list.html', context)

@login_required
@user_passes_test(is_admin)
def approve_blood_request(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)
    blood_request.is_approved = True
    blood_request.save()
    return redirect('blood_request_list')

@login_required
@user_passes_test(is_admin)
def reject_blood_request(request, pk):
    blood_request = get_object_or_404(BloodRequest, pk=pk)
    blood_request.is_approved = False # Or add another status like 'Rejected'
    blood_request.save()
    return redirect('blood_request_list')

@login_required
@user_passes_test(is_admin)
def donation_list(request):
    donations = Donation.objects.all()
    query = request.GET.get('q')
    blood_group_filter = request.GET.get('blood_group')
    status_filter = request.GET.get('status')

    if query:
        donations = donations.filter(Q(donor__user__username__icontains=query) | Q(blood_group__icontains=query))
    if blood_group_filter and blood_group_filter != 'All':
        donations = donations.filter(blood_group=blood_group_filter)
    if status_filter and status_filter != 'All':
        donations = donations.filter(status=status_filter)

    blood_groups = [bg[0] for bg in Donation.blood_group.field.choices]
    statuses = ['All', 'Pending', 'Approved', 'Rejected']

    context = {
        'donations': donations,
        'blood_groups': blood_groups,
        'selected_blood_group': blood_group_filter,
        'statuses': statuses,
        'selected_status': status_filter,
        'query': query,
    }
    return render(request, 'admin/donation_list.html', context)

@login_required
@user_passes_test(is_admin)
def approve_donation(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    donation.status = 'Approved'
    donation.save()
    return redirect('donation_list')

@login_required
@user_passes_test(is_admin)
def reject_donation(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    donation.status = 'Rejected'
    donation.save()
    return redirect('donation_list')

@login_required
@user_passes_test(is_admin)
def donation_create(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm()
    return render(request, 'admin/donation_form.html', {'form': form, 'action': 'Create'})

@login_required
@user_passes_test(is_admin)
def donation_update(request, pk):
    donation = get_object_or_404(Donation, pk=pk)
    if request.method == 'POST':
        form = DonationForm(request.POST, instance=donation)
        if form.is_valid():
            form.save()
            return redirect('donation_list')
    else:
        form = DonationForm(instance=donation)
    return render(request, 'admin/donation_form.html', {'form': form, 'action': 'Update'})

# Donor Features
@login_required
@user_passes_test(is_donor)
def donor_profile(request):
    donor = request.user.donor
    if request.method == 'POST':
        form = DonorProfileForm(request.POST, instance=donor)
        if form.is_valid():
            form.save()
            return redirect('donor_profile')
    else:
        form = DonorProfileForm(instance=donor)
    return render(request, 'donor/donor_profile.html', {'form': form, 'donor': donor})

@login_required
@user_passes_test(is_donor)
def make_blood_request(request):
    if request.method == 'POST':
        form = BloodRequestForm(request.POST)
        if form.is_valid():
            blood_request = form.save(commit=False)
            blood_request.request_by = request.user
            blood_request.save()
            return redirect('donor_dashboard')
    else:
        form = BloodRequestForm()
    return render(request, 'donor/make_blood_request.html', {'form': form})

@login_required
@user_passes_test(is_donor)
def donor_donation_history(request):
    donor = request.user.donor
    donations = donor.donations.all()
    return render(request, 'donor/donor_donation_history.html', {'donations': donations})

@login_required
@user_passes_test(is_donor)
def donor_blood_requests(request):
    blood_requests = BloodRequest.objects.filter(request_by=request.user)
    return render(request, 'donor/donor_blood_requests.html', {'blood_requests': blood_requests})


