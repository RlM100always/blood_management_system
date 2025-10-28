# Blood Management System

This is a full-stack Blood Management System built using the Django framework and SQLite database. It features user authentication, role-based access for Admin and Donor, and a web interface built with Django templates and Bootstrap for a responsive design.

## Features

### User Authentication
*   **Register:** Users can register as either a Donor or an Admin.
*   **Login/Logout:** Secure login and logout functionality.

### Roles
*   **Admin:**
    *   Manage Blood Banks (Create, View, Update, Delete)
    *   View and manage Donors
    *   View, approve, and reject Blood Requests
    *   View, approve, and reject Blood Donations
    *   Dashboard with overall statistics (total donors, pending/approved/rejected donations).
*   **Donor:**
    *   Update profile information (blood group, contact details, last donation date).
    *   Make new blood donation requests.
    *   View personal donation history.
    *   View personal blood request history.
    *   Dashboard showing personal info, available blood groups, and donation history.

### Core Functionalities
*   **Blood Bank Management:** Admins can manage information about various blood banks.
*   **Donor Management:** Admins can view details of registered donors.
*   **Blood Request Management:** Admins can approve or reject blood requests made by donors. Donors can make requests and view their status.
*   **Blood Donation Management:** Admins can approve or reject donation records. Donors can view their donation history.
*   **Search and Filter:** Admin dashboards include search and filter options for donors, blood requests, and donations based on various criteria (e.g., blood group, status, username).

## Setup Instructions

Follow these steps to get the Blood Management System up and running on your local machine.

### Prerequisites
*   Python 3.8+
*   pip (Python package installer)

### Installation

1.  **Clone the repository (or extract the ZIP file):**
    ```bash
    git clone <repository_url> # If using git
    # or unzip the provided project.zip file
    ```

2.  **Navigate into the project directory:**
    ```bash
    cd blood_management_system
    ```

3.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Note: The `requirements.txt` file will be generated in the next step.)*

5.  **Apply database migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser (for admin access):**
    ```bash
    python manage.py createsuperuser
    ```
    Follow the prompts to create an admin username, email, and password.

7.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

8.  **Access the application:**
    Open your web browser and go to `http://127.0.0.1:8000/`

## Usage

*   **Register:** Click on "Register" to create a new user. You can choose to register as a Donor. If you don't select "Register as a Donor", you will be registered as an Admin by default.
*   **Login:** Use your registered credentials to log in.
*   **Dashboard:** After logging in, you will be redirected to either the Admin Dashboard or Donor Dashboard based on your role.

### Admin Dashboard
From the admin dashboard, you can navigate to:
*   **Manage Blood Banks:** Add, view, edit, and delete blood bank records.
*   **Manage Donors:** View registered donors, search, and filter them.
*   **Manage Blood Requests:** View all blood requests, approve or reject them.
*   **Manage Donations:** View all donation records, approve or reject pending donations.

### Donor Dashboard
From the donor dashboard, you can:
*   **Edit Profile:** Update your personal and donation-related information.
*   **Make Blood Request:** Submit a request for blood.
*   **View Donation History:** See a list of your past donations.
*   **View Your Blood Requests:** Check the status of your blood requests.

## Project Structure

```
blood_management_system/
├── blood_management_system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── core/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   ├── admin/
│   │   │   ├── blood_bank_confirm_delete.html
│   │   │   ├── blood_bank_detail.html
│   │   │   ├── blood_bank_form.html
│   │   │   ├── blood_bank_list.html
│   │   │   ├── blood_request_list.html
│   │   │   ├── donation_form.html
│   │   │   ├── donation_list.html
│   │   │   ├── donor_detail.html
│   │   │   └── donor_list.html
│   │   ├── donor/
│   │   │   ├── donor_blood_requests.html
│   │   │   ├── donor_dashboard.html
│   │   │   ├── donor_donation_history.html
│   │   │   ├── donor_profile.html
│   │   │   └── make_blood_request.html
│   │   ├── registration/
│   │   │   ├── login.html
│   │   │   └── register.html
│   │   ├── admin_dashboard.html
│   │   ├── base.html
│   │   ├── donor_dashboard.html
│   │   └── home.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── urls.py
├── manage.py
├── README.md
└── db.sqlite3 # This file will be created after migrations
```

## Project Screenshot 
<p align="center">
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085525.png?raw=true" />
    <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085554.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085620.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085702.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085821.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085845.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085913.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20085936.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20090001.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20090025.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20090050.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20090143.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20090205.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20091130.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20091206.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20091234.png?raw=true" />
  <img width="600" src="https://github.com/RlM100always/Hisab/blob/main/bms/Screenshot%202025-10-28%20091258.png?raw=true" />
  
  </p>



