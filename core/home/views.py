from django.shortcuts import render
from .models import ContactMessage, LensType, StockLens

navLinksData = [
            {
                'name': 'Home',
                'link': '/'
            },
            {
                'name': 'About Us',
                'link': '/aboutus'
            },
            {
                'name': 'Lenses',
                'link': '/lenses'
            },
            {
                'name': 'Contact',
                'link': '/contact'
            }
        ]

# Create your views here.
def home(req):
    return render(req, "index.html", context={ 'navlinks': navLinksData })

def aboutus(req):
    
    lensCollectionData = [
        "Scratch Proof Lenses",
        "Crystal Clear Lenses",
        "Blue Cut Lenses",
        "Photo Grey Lenses",
        "Polycarbonate Lenses",
        "Blue Cut Polycarbonate Lenses",
        "Blue Cut Photo Grey Lenses",
        "Night Vision Lenses",
        "Night Vision Photo Grey Blue Cut Lenses",
    ]
    
    coatingData = [
        'Scratch Proof HC',
        'Crystal ARC',
        'UV Green',
        'UV Blue',
        'Protect Blue',
        'UV Crystal+ Protect',
        'Drive+'
    ]
    
    return render(req, "aboutus.html", context={ 'navlinks': navLinksData, 'lensCollections': lensCollectionData, 'cotingDatas': coatingData })

def contact(req):
    
    isError = False
    
    popupMessage = []
    
    if req.method == "GET":
        return render(req, "contact.html", {'navlinks': navLinksData, "popups": popupMessage})
    
    if req.method == "POST":
        
        print("Got Post Reqest")
        
        name = req.POST.get('name')
        email = req.POST.get('email')
        phone = req.POST.get('phone')
        message = req.POST.get('message')
        
        form_data = {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        }
        
        if len(name) < 2:
            popupMessage.append({
                'type': "warning",
                'message': 'Name should be at least 3 characters long.'
            })
            isError = True
        
        if len(phone) < 10:
            popupMessage.append({
                'type': "warning",
                'message': 'Phone should be at least 10 numbers long.'
            })
            isError = True
        
        if isError:
            return render(req, "contact.html", context={'navlinks': navLinksData, "popups": popupMessage, 'data': form_data})
        else:
            
            if not name or not email or not message or not phone:
                isError = True
                popupMessage.append({
                'type': "warning",
                'message': 'Please Fill all the Fields.'
                })
                # Handle invalid form data, for example, redirect back to the contact page with an error message
                return render(req, "contact.html", {'navlinks': navLinksData, "popups": popupMessage})
            else:
                isError = False
                
                new_message = ContactMessage(name=name, email=email, phone=phone, message=message)
                new_message.save()
                
                popupMessage.append({
                    'type': "success",
                    'message': 'You Message Submitted Successfully.'
                })
                return render(req, "contact.html", {'navlinks': navLinksData, "popups": popupMessage})


def lenses(req):
    lensTypesData = LensType.objects.all()
    
    print(lensTypesData)
    
    context={'navlinks': navLinksData, 'lensTypesData': lensTypesData}
    
    return render(req, "lenses.html", context=context)

def lenses_list(req, lens_type_id):
    
    stockLensesData = StockLens.objects.filter(type__id=lens_type_id).prefetch_related('features')
    
    for lens in stockLensesData:
        print("---------------------")
        print(f"Brand: {lens.brand_name}")
        print(f"Type: {lens.type}")
        print(f"Index: {lens.lens_index}")
        print(f"Material: {lens.lens_material}")
        print(f"Coating: {lens.lens_coating}")
        print(f"Description: {lens.description}")
        print("Features:")
        for feature in lens.features.all():
            print(f"- {feature}")
            print(f"  Image: {feature.image.url}")  # Access the feature image URL
            print(f"  Description: {feature.description}")
        print(f"Image: {lens.image.url}")  # Access the lens image URL
        print("---------------------")
    
    context = {'navlinks': navLinksData, 'id': lens_type_id, 'lensesData' : stockLensesData }
    
    return render(req, "lensList.html", context=context)
