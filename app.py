from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/availability')
def availability():
    return render_template('availability.html')

@app.route('/bookings')
def bookings():
    return render_template('bookings.html')

@app.route('/appointments')
def appointments():
    return render_template('appointments.html')

if __name__ == '__main__':
    app.run(debug=True)
