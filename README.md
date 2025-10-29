# ShopEase: E-Commerce Web Application

A full-stack **E-Commerce Web Application** built using **Django**, **Python**, **SQLite**, **HTML**, **CSS**, and **Bootstrap**.  
The platform enables users to browse products, manage their cart, place orders, and track their purchases with secure user authentication and order management features.

---

## 🚀 Features

- 🔐 **User Authentication** – Secure login, signup, and session management.
- 🛒 **Shopping Cart** – Add, remove, and update product quantities.
- 📦 **Order Management** – Place orders, view order history, and cancel pending orders.
- 💳 **Checkout System** – Capture customer details (address, phone, name) with **Cash on Delivery** payment option.
- 🧾 **Admin Dashboard** – Manage products, orders, and order status from Django Admin.
- 💻 **Responsive UI** – Built with **Bootstrap**, ensuring seamless experience across all devices.

---

## 🧠 Skills & Technologies Used

| Category | Skills |
|-----------|---------|
| **Programming Languages** | Python, HTML5, CSS3 |
| **Frameworks & Libraries** | Django, Bootstrap |
| **Database** | SQLite (Django ORM) |
| **Backend Development** | RESTful architecture, Django Views, Class-Based Views (CBVs), URL Routing |
| **Frontend Development** | Responsive UI using HTML, CSS, Bootstrap, and Django Templates |
| **Authentication** | Django’s built-in authentication system (login, logout, register) |
| **E-Commerce Logic** | Product catalog, Cart management, Checkout, Order tracking |
| **Version Control** | Git, GitHub |
| **Tools & Environment** | Visual Studio Code, Django Development Server |


---


## 📁 Project Structure

| Folder / File | Description |
|----------------|-------------|
| **ecommerce_project/** | Root Django project directory |
| ├── `manage.py` | Django management script |
| ├── `db.sqlite3` | SQLite database file |
| ├── **ecommerce_project/** | Main Django configuration folder |
| │ ├── `settings.py` | Project settings (includes global templates/static config) |
| │ ├── `urls.py` | Root URL configuration |
| │ ├── `wsgi.py` | WSGI entry point |
| │ └── `asgi.py` | ASGI entry point |
| **accounts/** | Handles user authentication and profile management |
| ├── `models.py` | User profile and related models |
| ├── `views.py` | Signup, login, logout, and profile logic |
| ├── `urls.py` | URL routes for accounts |
| └── `forms.py` | Forms for registration and profile updates |
| **products/** | Manages product catalog and details |
| ├── `models.py` | Product model (name, price, image, etc.) |
| ├── `views.py` | Product listing and details logic |
| ├── `urls.py` | Product-related routes |
| **cart/** | Handles user shopping cart |
| ├── `models.py` | CartItem model |
| ├── `views.py` | Add/update/remove cart items |
| ├── `urls.py` | Cart routes |
| **orders/** | Handles orders and order history |
| ├── `models.py` | Order and OrderItem models |
| ├── `views.py` | Order listing, details, and cancellation |
| ├── `urls.py` | Order routes |
| **checkout/** | Manages checkout and address/payment info |
| ├── `models.py` | Address and payment models |
| ├── `views.py` | Checkout form and order confirmation |
| ├── `urls.py` | Checkout routes |
| **templates/** | Global templates shared across all apps |
| ├── `base.html` | Main base layout |
| ├── `home.html` | Homepage template |
| ├── `products/` | Product-related templates |
| ├── `cart/` | Cart templates |
| ├── `orders/` | Order templates |
| ├── `checkout/` | Checkout templates |
| └── `accounts/` | Authentication templates |
| **static/** | Global static assets (CSS, JS, images) |
| ├── `css/` | Stylesheets and Bootstrap overrides |
| ├── `js/` | JavaScript files |
| └── `images/` | Product and UI images |


