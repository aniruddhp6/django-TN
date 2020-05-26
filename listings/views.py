from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User
from listings.models import RegListing
from listings.forms import RegListingForm,UpdateForm
from django.http import HttpResponseRedirect 




def index(request):
    listings=RegListing.objects.order_by('-list_date')
    paginator=Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings=paginator.get_page(page)

    context={
        'listings':paged_listings
    }
    return render(request,'listings/listings.html', context)

def listing(request,listing_id):
    listing=get_object_or_404(RegListing ,pk=listing_id)

    context={
        'listing':listing
    }
    return render(request,'listings/listing.html',context)
  
  
def create(request): 
    if request.method == 'POST':
        title = request.POST['title']
        message = request.POST['message']
        reg=RegListing.objects.create(title=title,message=message,reguser_id=request.user.id)
        reg.save() 
        return redirect('dashboard') 

    else:
        return render(request, 'listings/create.html')

def update(request, id):     
    
    if request.method == 'POST': 
        title = request.POST['title']
        message = request.POST['message']
        t = RegListing.objects.get(id=id)
        t.title = title
        t.message = message
        t.save()
        return redirect('dashboard') 

    else:
        about = RegListing.objects.get(id=id)        
        return render(request, "listings/update.html", {'about':about}) 
    
    

def delete(request,id):
    about = RegListing.objects.get(id=id)
    reg = RegListing.objects.get(pk=id)
    reg.delete()
    return redirect('dashboard')
            
         
