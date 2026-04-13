# Websale: Premium Ecommerce Prototype

Websale is a high-end ecommerce platform built with Django for selling professional website development packages. Inspired by premium retail experiences, it features a modern **Glassmorphism** aesthetic, fully dynamic product management, and a complete user purchase flow.

## ✨ Key Features

- **Premium UI/UX**: Dark mode theme with glassmorphic cards, fluid typography, and micro-animations.
- **Dynamic Catalog**: Full management of website packages and categories through the Django Admin.
- **User Authentication**: Secure Signup, Login, and personalized Dashboards for order tracking.
- **Session-based Cart**: Seamless shopping experience without requiring immediate login.
- **Order Management**: End-to-end checkout flow resulting in persistent order history.
- **Responsive Design**: Optimized for everything from mobile devices to ultra-wide displays.
- **Search & Filtering**: Real-time search for finding the perfect package.

## 🚀 Tech Stack

- **Backend**: Django 6.0.3
- **Frontend**: HTML5, CSS3 (Vanilla), Django Template Language (DTL)
- **Database**: SQLite3
- **Image Processing**: Pillow

## 📦 Installation & Setup

1. **Clone the repository**:
   ```bash
   cd Websale
   ```

2. **Set up Virtual Environment**:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   python -m pip install Django Pillow
   ```

4. **Initialize Database**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Seed Initial Data**:
   ```bash
   python manage.py shell < seed_data.py
   ```

6. **Create Superuser (Admin Access)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run Server**:
   ```bash
   python manage.py runserver
   ```

## 🛠 Project Structure

- `Websale/`: Core project settings and URL routing.
- `Shop/`: Main application containing models, views, and commerce logic.
- `Templates/`: Organized HTML templates with a reusable `base.html`.
- `Static/`: Premium CSS stylesheets and image assets.
- `seed_data.py`: Utility script for populating the marketplace.

---

*Built with ❤️ as a professional Django prototyping showcase.*
