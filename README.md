# doctor-appointment-system
A web-based appointment booking system for medical clinics. Features include patient registration, time slot scheduling, and appointment management for both patients and doctors.


# 🏥 Django Clinic Project

A simple medical appointment booking system built with **Django**.  

---

## 🚀 Getting Started

Follow the steps below to set up the project locally.

### 1. Clone the repository
```bash
git clone https://github.com/AliSalsali/doctor-appointment-system.git
cd clinic
```
### 2. Create a virtual environment

```bash
python -m venv .venv
```
### 3. Activate the virtual environment
Windows:
```
.venv\Scripts\activate
```
Linux/Mac:
```
source .venv/bin/activate
```
### 4. Install dependencies


```
pip install -r requirements.txt
```
### 5. Apply database migrations

```
python manage.py migrate
```
### 6. Create a superuser (optional, for admin access)
```
python manage.py createsuperuser
```
### 7. Run the development server
```
python manage.py runserver
```
Now the project will be available at:

```
http://127.0.0.1:8000/
```