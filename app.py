from flask import Flask, render_template, redirect, url_for, session, flash, request

app = Flask(__name__)
app.secret_key = "your_secret_key"

VALID_USER = "admin"
VALID_PASS = "password"
bookings = []

@app.route('/', methods=['GET', 'POST'])
def login():
    if session.get('logged_in'):
        return redirect(url_for('dashboard'))

    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == VALID_USER and password == VALID_PASS:
            session['logged_in'] = True
            flash("Logged in successfully!", "success")
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid credentials. Please try again."
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully.", "info")
    return redirect(url_for('login'))

@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/availability')
def availability():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    slots = [
        {'day': 'Monday', 'available': True},
        {'day': 'Tuesday', 'available': False},
        {'day': 'Wednesday', 'available': True},
    ]
    return render_template('availability.html', slots=slots)

@app.route('/calendar')
def calendar():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    dates = ['2025-08-21', '2025-08-22', '2025-08-23']
    return render_template('calendar.html', dates=dates)

@app.route('/book', methods=['GET', 'POST'])
def book():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    if request.method == 'POST':
        sport = request.form.get('sport')
        date = request.form.get('date')
        time = request.form.get('time')
        name = request.form.get('name')
        contact = request.form.get('contact')
        if all([sport, date, time, name, contact]):
            bookings.append({
                'sport': sport, 'date': date, 'time': time,
                'name': name, 'contact': contact
            })
            flash("Booked successfully!", "success")
            return redirect(url_for('view_bookings'))
        else:
            flash("Please fill in all fields.", "error")
    return render_template('book.html')

@app.route('/bookings')
def view_bookings():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('bookings.html', bookings=bookings)

if __name__ == "__main__":
    app.run(debug=True)
