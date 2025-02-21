# Medical Appointment Scheduler

A simple and efficient web application for managing medical appointments built with Flask and SQLite.

## Features

- Book appointments with doctors
- View all scheduled appointments
- Store patient information securely
- User-friendly interface
- Flash notifications for successful/failed operations

## Technical Stack

- **Backend**: Flask (Python)
- **Database**: SQLite
- **Frontend**: HTML/CSS (Templates)

## Database Schema

### Patients Table
- `patient_id` (Primary Key)
- `patient_name`
- `patient_phone`

### Appointments Table
- `appointment_id` (Primary Key)
- `patient_id` (Foreign Key)
- `appointment_date`
- `appointment_time`
- `doctor_name`

## Setup and Installation

1. Clone the repository
2. Install required dependencies:
   ```
   pip install flask
   ```
3. Run the application:
   ```
   python app.py
   ```
4. Access the application at `http://localhost:5000`

## Usage

1. Navigate to the homepage
2. Click "Book Appointment" to schedule a new appointment
3. Fill in patient details and appointment information
4. View all appointments in the "View Appointments" section

## Contributing

Feel free to submit issues and enhancement requests!
