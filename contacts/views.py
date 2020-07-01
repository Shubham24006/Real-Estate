from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


# # Create your views here.
def contact(request):
    if request.method == 'POST':
        property_id = request.POST['prop_id']
        property_name = request.POST['property_name']
        name = request.POST['user']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        seller_id = request.POST['seller_id']
        buyer_id = request.POST['buyer_id']
        seller_email = request.POST['seller_email']
    #
        #  Check if user has made inquiry already
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(property_id=property_id, buyer_id=buyer_id)

            if has_contacted:
                messages.error(request, 'You have already made an inquiry for this listing')
                return redirect('/listing/'+str(property_id))

        contact = Contact(property_name=property_name, property_id=property_id, name=name, email=email, phone=phone,
                          message=message, seller_id=seller_id, buyer_id=buyer_id)
        contact.save()

        subject, from_email, to = 'ENQUIRY LISTED', settings.EMAIL_HOST_USER, seller_email
        text_content = 'There has been an inquiry for your posted property.'
        url = "http://127.0.0.1:8000/listing/{}/".format(property_id)
        html_content = '<p>This is an <strong>important</strong> message.</p><br><p>There has been an inquiry for ' \
                       'your posted property.</p> <br> <strong>{}</strong> having email id <strong>{}</strong> and ' \
                       'phone number <strong>{}</strong> is interseted in your property name<a href={}> {} </a>.' \
                       ' <br> please login and check for more details. <br>Thanks. <br> Team <strong>TOTHENEW.<strong>'\
        .format(name, email, phone, url, property_name)

        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        messages.success(request, 'Your request has been submitted, a realtor will get back to you soon')

    return redirect('/')


def enquiries(request):
    enquiries = Contact.objects.order_by('-contact_date').filter(seller_id=request.user.id)

    return render(request, 'enquries.html', {'enquries': enquiries})








