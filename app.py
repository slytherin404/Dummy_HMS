from flask import Flask, render_template, redirect, request, url_for, session, flash
from models import db, Admin, Customer, Seller, Storage
from werkzeug.security import generate_password_hash, check_password_hash
app = Flask(__name__)

app.config['SECRET_KEY'] = 'Aditi123@#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aditi.db'

db.init_app(app)

#predefing admin credentials
def create_admin():
    with app.app_context():
        db.create_all()  # Create tables if they don't exist
        admin = Admin.query.filter_by(username='aditik123').first()
        if not admin:
            hashed_password = generate_password_hash('admin123', method='pbkdf2:sha256')
            admin = Admin(username='aditik123', email='aditi16@gmail.com', contact='1234567890', password=hashed_password)
            db.session.add(admin)
            db.session.commit()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        contact = request.form.get('contact')  # optional
        password = request.form['password']

        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        # Check if username/email already exists (optional but recommended)
        existing_user = Customer.query.filter(
            (Customer.username == username) | (Customer.email == email)
        ).first()
        if existing_user:
            flash("Username or email already exists!", "danger")
            return redirect(url_for('register'))

        # Create a new Customer instance
        new_customer = Customer(username=username, email=email, contact=contact, password=hashed_password)

        # Add to the database
        db.session.add(new_customer)
        db.session.commit()

        flash("Registration successful! Please login.", "success")
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        role = request.form['role']
        username = request.form['username']
        password = request.form['password']
        user = None

        # Get user based on role
        if role == 'admin':
            user = Admin.query.filter_by(username=username).first()
        elif role == 'seller':
            user = Seller.query.filter_by(username=username).first()
        elif role == 'customer':
            user = Customer.query.filter_by(username=username).first()

        # Check password and login
        if user:
            if check_password_hash(user.password, password):
                # Check if seller is blocked
                if role == 'seller' and user.status == 'blocked':
                    flash("Your account has been blocked by admin. Please contact support.", "danger")
                    return redirect(url_for('login'))
                
                session['user_id'] = user.id
                session['role'] = role
                flash(f"Logged in as {role}", "success")
                return redirect(url_for(f"{role}_dashboard"))  # redirect to respective dashboard
            else:
                flash("Incorrect password", "danger")
        else:
            flash(f"No {role} found with that username", "danger")

    return render_template('login.html')


@app.route('/admin_dashboard')
def admin_dashboard():
    sellers = Seller.query.all()
    return render_template('admin_dashboard.html', sellers=sellers)

@app.route('/create_seller', methods=['GET', 'POST'])
def create_seller():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        contact = request.form['contact']
        password = request.form['password']
        storage_capacity = request.form['storage_capacity']

        # Hash the password
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')

        new_seller = Seller(username=username, email=email, contact=contact, password=hashed_password, storage_capacity=storage_capacity)
        db.session.add(new_seller)
        db.session.commit()

        flash("Seller created successfully!", "success")
        return redirect(url_for('admin_dashboard'))

    return render_template('create_seller.html')

@app.route('/edit_seller/<int:seller_id>', methods=['GET', 'POST'])
def edit_seller(seller_id):
    seller = Seller.query.get_or_404(seller_id)
    if request.method == 'POST':
        seller.username = request.form['username']
        seller.email = request.form['email']
        seller.contact = request.form['contact']
        seller.password = generate_password_hash(request.form['password'], method='pbkdf2:sha256')
        seller.storage_capacity = request.form['storage_capacity']
        db.session.commit()
        flash("Seller updated successfully!", "success")
        return redirect(url_for('admin_dashboard'))
    return render_template('edit_seller.html', seller=seller)

@app.route('/delete_seller/<int:seller_id>', methods=['POST'])
def delete_seller(seller_id):
    seller = Seller.query.get_or_404(seller_id)
    db.session.delete(seller)
    db.session.commit()
    flash("Seller deleted successfully!", "success")
    return redirect(url_for('admin_dashboard'))

@app.route('/toggle_seller_status/<int:seller_id>', methods=['POST'])
def toggle_seller_status(seller_id):
    seller = Seller.query.get_or_404(seller_id)
    if seller.status == 'active':
        seller.status = 'blocked'
        flash(f"Seller {seller.username} has been blocked!", "warning")
    else:
        seller.status = 'active'
        flash(f"Seller {seller.username} has been unblocked!", "success")
    
    db.session.commit()
    return redirect(url_for('admin_dashboard'))

@app.route('/seller_dashboard')
def seller_dashboard():
    return render_template('seller_dashboard.html')

@app.route('/customer_dashboard')
def customer_dashboard():
    return render_template('customer_dashboard.html')

@app.route('/logout')
def logout():
    session.clear()
    flash("Logged out successfully!", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    create_admin()
    app.run(debug=True, port=5001)

