from flask import Flask, render_template, request, redirect, url_for, flash #importing necessary libraries 
import sqlite3
from datetime import datetime

app = Flask(__name__) #starts the flask web application
app.secret_key = 'secret_key123'  # Required for flash messages

# Create database and tables
def init_db():
    conn = sqlite3.connect('clinic.db') # connects to the database
    c = conn.cursor() # creates a cursor object to interact with the database
    
    # # Drop existing tables if they exist
    # c.execute('DROP TABLE IF EXISTS appointments')
    # c.execute('DROP TABLE IF EXISTS patients')
    
    # # creates a table for patients with columns id, name, and phone in SQLite
    c.execute('''CREATE TABLE IF NOT EXISTS patients 
                 (patient_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  patient_name TEXT NOT NULL,
                  patient_phone TEXT NOT NULL)''') 
    
    # creates a table for appointments with id, patient_id, date, time, doctor, and foreign key patient_id references the id column in the patients table
    c.execute('''CREATE TABLE IF NOT EXISTS appointments
                 (appointment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                  patient_id INTEGER NOT NULL,
                  appointment_date TEXT NOT NULL,
                  appointment_time TEXT NOT NULL,
                  doctor_name TEXT NOT NULL,
                  FOREIGN KEY (patient_id) REFERENCES patients (patient_id))''') # foreign key links the patient_id column in the appointments table to the patient_id column in the patients table
    conn.commit() # saves the changes to the database
    conn.close() # closes the connection to the database

# Initialize database
init_db()

@app.route('/') #defines the homepage url
def home():
    return render_template('home.html') # shows the home page

@app.route('/book_appointment', methods=['GET', 'POST'])
def book_appointment():
    if request.method == 'POST':
        try:
            name = request.form['name']
            phone = request.form['phone']
            date = request.form['date']
            time = request.form['time']
            doctor = request.form['doctor']

            conn = sqlite3.connect('clinic.db')
            c = conn.cursor()
            
            # Add patient with new column names
            c.execute("INSERT INTO patients (patient_name, patient_phone) VALUES (?, ?)", 
                     (name, phone))
            patient_id = c.lastrowid
            
            # Add appointment with new column names
            c.execute("""INSERT INTO appointments 
                        (patient_id, appointment_date, appointment_time, doctor_name) 
                        VALUES (?, ?, ?, ?)""",
                     (patient_id, date, time, doctor))
            
            conn.commit()
            conn.close()
            
            flash('Appointment booked successfully!')
            return redirect(url_for('home'))
        except Exception as e:
            print(f"Error: {e}")
            flash('Error booking appointment!')
            return redirect(url_for('book_appointment'))
    
    return render_template('book_appointment.html')

@app.route('/view_appointments')
def view_appointments():
    # Connect to database
    conn = sqlite3.connect('clinic.db')
    c = conn.cursor()
    
    # Updated query with new column names
    c.execute('''
        SELECT 
            patients.patient_name,
            patients.patient_phone,
            appointments.appointment_date,
            appointments.appointment_time,
            appointments.doctor_name
        FROM appointments
        JOIN patients ON appointments.patient_id = patients.patient_id
        ORDER BY appointments.appointment_date, appointments.appointment_time
    ''')
    
    # Fetch all appointments
    appointments = c.fetchall()
    conn.close()
    
    # Pass appointments to the template
    return render_template('view_appointments.html', appointments=appointments)

if __name__ == '__main__':
    app.run(debug=True) 