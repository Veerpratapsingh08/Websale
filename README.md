# Websale: Premium Ecommerce Prototype

Websale is a high-end ecommerce platform built with Django for selling professional website development packages. It features a modern dark aesthetic, fully dynamic product management, and a complete user purchase flow.

## Key Features

- **Premium UI/UX**: Dark mode theme with card-based layouts, fluid typography, and micro-animations.
- **Dynamic Catalog**: Management of website packages and categories through the Django Admin.
- **User Authentication**: Secure Signup, Login, and personalized Dashboards for order tracking.
- **Session-based Cart**: Seamless shopping experience.
- **Order Management**: End-to-end checkout flow resulting in persistent order history.
- **Responsive Design**: Optimized for mobile and desktop.
- **Search & Filtering**: Search for finding packages.

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML5, CSS3, Django Template Language (DTL)
- **Database**: SQLite3 (Local) / PostgreSQL (Production)

## Installation & Setup

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
   pip install -r requirements.txt
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

## Project Structure

- `Websale/`: Core project settings and URL routing.
- `Shop/`: Main application containing models, views, and commerce logic.
- `Templates/`: Organized HTML templates with a reusable `base.html`.
- `Static/`: Premium CSS stylesheets and image assets.
- `seed_data.py`: Utility script for populating the marketplace.
