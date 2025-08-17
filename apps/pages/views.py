from django.shortcuts import render


def home(request):
    return render(request, 'pages/home.html', {'title': 'Welcome to NeuraNote'})


def contact_us(request):
    return render(request, 'pages/contact_us.html', {'title': 'Contact Us'})


def privacy_policy(request):
    return render(request, 'pages/privacy_policy.html', {'title': 'Privacy Policy'})


def terms_of_service(request):
    return render(request, 'pages/terms_of_service.html', {'title': 'Terms of Service'})
