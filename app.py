from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="veeresh",  # <== your mysql password
    database="movie_booking_db"  # <== your database name
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    usernames = request.form['usernames']  # names separated by commas
    phone_number = request.form['phone_number']
    movie_name = request.form['movie_name']
    available_seats = int(request.form['available_seats'])
    booked_seats = int(request.form['booked_seats'])
    theater_name = request.form['theater_name']

    # Split multiple names
    name_list = [name.strip() for name in usernames.split(',')]

    for name in name_list:
        cursor.execute("""
            INSERT INTO users (name, phone_number, movie_name, available_seats, booked_seats, theater_name)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (name, phone_number, movie_name, available_seats, booked_seats, theater_name))

    db.commit()

    return redirect(url_for('home'))  # Very Important: redirect to home after submission

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)

