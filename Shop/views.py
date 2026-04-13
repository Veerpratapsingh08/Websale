from django.shortcuts import render


def home(request):
    context = {
        "featured_services": [
            {
                "title": "Business Website Package",
                "description": "A complete website setup for shops, startups, and local businesses.",
            },
            {
                "title": "Portfolio Website Package",
                "description": "A modern portfolio solution for students, freelancers, and creators.",
            },
            {
                "title": "Ecommerce Website Package",
                "description": "An online store starter with product browsing, cart flow, and order management.",
            },
        ]
    }
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    return render(request, "contact.html")
