# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
from .models import PricePackage
from .serializers import PricePackageSerializer

@api_view(['POST'])
def submit_form(request):
    serializer = PricePackageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # Get data
        data = serializer.data
        name = data.get('name')
        phone = data.get('phone')
        email = data.get('email')
        city = data.get('city')
        date = data.get('date')
        message = data.get('message')

        # Send email
        send_mail(
            subject=f"New Price Package Enquiry from {name}",
            message=f"""
            Name: {name}
            Phone: {phone}
            Email: {email}
            City: {city}
            Date: {date}
            Message: {message}
            """,
            from_email='snehamulamootil@gmail.com',
            recipient_list=['lakshyamakeovers@gmail.com'],
            fail_silently=False,
        )

        return Response({"success": True, "message": "Form submitted and email sent successfully!"})

    return Response({"success": False, "message": "Invalid data!"}, status=400)
