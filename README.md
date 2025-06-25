# 🎯 Real-Time Attendance Monitoring System

This is a real-time attendance system built using **Django**, **OpenCV**, and **ARUCO markers**. It captures webcam input, detects ARUCO markers, and marks attendance automatically, storing all data securely in a database.

---

## 🛠️ Features

- 🎥 Real-time ARUCO marker detection via webcam
- 📌 Marks attendance with timestamp and user info
- 🔐 Secure user login and registration system
- 🗃️ Django-based backend with SQLite3 database
- 💡 Ready for future integration with face recognition and motion detection
- 📸 Webcam capture and attendance snapshot (planned)

---

## 🧰 Tech Stack

- **Backend**: Django 5.x
- **Frontend**: Django Templates (HTML/CSS)
- **Database**: SQLite3
- **Computer Vision**: OpenCV (with ARUCO)

---
## 📁 Project Structure

| Path                          | Description                                                  |
|-------------------------------|--------------------------------------------------------------|
| `attendance_system/`          | Django project directory (settings, URLs)                    |
| ├── `attendance/`             | Main Django app (models, views, forms, templates)            |
| ├── `attendance_system/`      | Project configuration files (settings.py, urls.py, wsgi.py)  |
| ├── `detector.py`             | ARUCO marker detection script using OpenCV                   |
| ├── `manage.py`               | Django CLI tool for runserver, migrations, etc.              |
| `.venv/`                      | Virtual environment (excluded from Git)                      |
| `db.sqlite3`                  | SQLite3 database (stores users and attendance)               |
| `README.md`                   | Project documentation                                        |


## 🔧 Installation

```bash
# 1. Clone the repository
git clone https://github.com/Akky7684/Real-Time-Attendance-Monitoring-System.git
cd Real-Time-Attendance-Monitoring-System

# 2. Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py makemigrations
python manage.py migrate

# 5. Run the development server
python manage.py runserver
