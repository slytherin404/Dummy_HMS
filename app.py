from flask import Flask, render_template, redirect, request, url_for, session, flash
from models import db, Admin, Customer, Seller, Storage
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config['SECRET_KEY'] = 'Aditi123@#'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///aditi.db'

db.init_app(app)

# Custom Jinja2 filter for JSON parsing
@app.template_filter('from_json')
def from_json_filter(value):
    if value:
        import json
        try:
            return json.loads(value)
        except (json.JSONDecodeError, TypeError):
            return []
    return []

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
    customers = Customer.query.all()
    return render_template('admin_dashboard.html', sellers=sellers, customers=customers)

@app.route('/admin_search', methods=['GET', 'POST'])
def admin_search():
    if request.method == 'POST':
        search_query = request.form['search_query'].strip()
        search_type = request.form['search_type']
        
        results = {'sellers': [], 'customers': []}
        
        if search_query:
            if search_type in ['all', 'sellers']:
                # Search sellers by username
                sellers = Seller.query.filter(
                    Seller.username.contains(search_query)
                ).all()
                results['sellers'] = sellers
            
            if search_type in ['all', 'customers']:
                # Search customers by username
                customers = Customer.query.filter(
                    Customer.username.contains(search_query)
                ).all()
                results['customers'] = customers
        
        return render_template('admin_dashboard.html', 
                             sellers=Seller.query.all() if search_type == 'all' else results['sellers'],
                             customers=Customer.query.all() if search_type == 'all' else results['customers'],
                             search_performed=True,
                             search_query=search_query,
                             search_type=search_type,
                             search_results=results)
    
    # If GET request, redirect to admin dashboard
    return redirect(url_for('admin_dashboard'))

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
    if 'user_id' not in session or session.get('role') != 'seller':
        flash("Please login as seller to access this page.", "danger")
        return redirect(url_for('login'))
    
    seller = Seller.query.get(session['user_id'])
    if not seller:
        flash("Seller not found.", "danger")
        return redirect(url_for('login'))
    
    return render_template('seller_dashboard.html', seller=seller)

@app.route('/update_availability', methods=['GET', 'POST'])
def update_availability():
    if 'user_id' not in session or session.get('role') != 'seller':
        flash("Please login as seller to access this page.", "danger")
        return redirect(url_for('login'))
    
    seller = Seller.query.get(session['user_id'])
    if not seller:
        flash("Seller not found.", "danger")
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        import json
        from datetime import datetime, timedelta
        
        # Get selected dates from form
        selected_dates = request.form.getlist('available_dates')
        
        # Validate that all selected dates are within the next 7 days
        today = datetime.now().date()
        valid_dates = []
        
        for date_str in selected_dates:
            try:
                date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
                # Check if date is within next 7 days
                if today <= date_obj <= today + timedelta(days=6):
                    valid_dates.append(date_str)
            except ValueError:
                continue
        
        # Store the valid dates as JSON in the database
        seller.open_dates = json.dumps(valid_dates) if valid_dates else None
        db.session.commit()
        
        flash(f"Availability updated successfully! You are available on {len(valid_dates)} days.", "success")
        return redirect(url_for('seller_dashboard'))
    
    # For GET request, render the availability form
    return render_template('update_availability.html', seller=seller)

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

