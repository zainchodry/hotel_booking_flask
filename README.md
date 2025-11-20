# Hotel Room Booking System – Flask Project

A complete Flask-based Hotel Room Booking Application with authentication, room listing, booking system, admin features, templates, and SQLite database support.

## Features

### User Features
- User Registration & Login
- Secure Password Hashing
- View All Rooms
- Check Room Availability
- Book a Room
- View Booking History

### Admin Features
- Add Rooms
- Manage Room Types
- View All Bookings
- Mark Rooms as Available/Unavailable

## Project Structure

hotel_booking/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── database.db
│   └── static/
│       └── styles.css
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── rooms.html
│   ├── book_room.html
│   ├── bookings.html
│
├── README.md
└── run.py

## Installation Guide

### 1. Clone the Repository
git clone https://github.com/zainchodrye/hotel_booking_flask.git

### 2. Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate        # Linux/Mac
venv\Scripts\activate           # Windows

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Set Up the Database
flask shell
from app import db
db.create_all()
exit()

### 5. Run the Application
python run.py

Visit in browser:
http://127.0.0.1:5000/

## Database Models

### User Model
- id  
- username  
- email  
- password  

### Room Model
- id  
- room_number  
- room_type  
- price  
- is_available  

### Booking Model
- id  
- user_id (FK)  
- room_id (FK)  
- check_in  
- check_out  

## Screenshots (Descriptions Only)
- Homepage – Shows welcome text and navigation
- Room List – Shows all rooms
- Booking Form – User selects date and books room
- Booking History – User can view previous bookings

## Future Enhancements
- Payment Gateway Integration
- Email Notifications
- Admin Dashboard
- REST API Using Flask-RESTful
- Room Image Gallery

## License
This project is open-source and free to use.

## Author
Zain Choudry  
Built with ❤️ using Flask.
