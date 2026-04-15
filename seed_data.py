from Shop.models import Category, Package
from decimal import Decimal


Package.objects.all().delete()
Category.objects.all().delete()


basic = Category.objects.create(name="Standard Packages", description="Essential web solutions for individuals and small businesses.")
business = Category.objects.create(name="Business Suite", description="High-performance websites with professional features.")
ecommerce = Category.objects.create(name="Ecommerce", description="Complete online stores with inventory and payment systems.")


Package.objects.create(
    category=basic,
    name="Personal Portfolio",
    description="A sleek, single-page portfolio designed to showcase your skills and projects. Perfect for freelancers and students.",
    price=Decimal('299.00'),
    features="Responsive Design,Contact Form,3 Custom Sections,SEO Basics,Social Media Links"
)

Package.objects.create(
    category=basic,
    name="Landing Page Pro",
    description="High-converting landing page for your product or service. Optimized for speed and performance.",
    price=Decimal('499.00'),
    features="Lead Generation Form,Performance Optimized,Brand Integration,Analytics Setup,Mobile First Design"
)

Package.objects.create(
    category=business,
    name="Professional Business Site",
    description="A complete 5-page website for your business. Includes blog capability and professional layout.",
    price=Decimal('1200.00'),
    features="5 Custom Pages,Blog Integration,GDPR Compliance,Advanced SEO,Domain Consultation"
)

Package.objects.create(
    category=business,
    name="Corporate Portal",
    description="Advanced corporate website with employee dashboards and internal communication tools.",
    price=Decimal('2500.00'),
    features="User Dashboards,Internal CMS,Advanced Security,Priority Support,Custom API Integration"
)

Package.objects.create(
    category=ecommerce,
    name="Online Store Starter",
    description="Start selling online with a beautiful product catalog and secure cart system.",
    price=Decimal('1800.00'),
    features="Product Catalog (up to 50 items),Secure Checkout,Order Management,Coupon System,Inventory Tracking"
)

Package.objects.create(
    category=ecommerce,
    name="Enterprise Marketplace",
    description="Multi-vendor marketplace solution for large scale ecommerce operations.",
    price=Decimal('4500.00'),
    features="Multi-vendor Support,Advanced Analytics,Automated Invoicing,Wholesale Management,24/7 Premium Support"
)

print("Data seeded successfully!")
