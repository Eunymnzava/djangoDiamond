from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import ListView,CreateView, DeleteView,DetailView
from finance.models import Donor
# from finance.forms import DonorForm
from django.urls import reverse_lazy



# Create your views here.
   
# class DonorCreateView(CreateView):
#     model = Donor
#     form_class = DonorForm
#     template_name = 'createdonorForm.html'
#     success_url = reverse_lazy('donorlist')  
   

#     def form_valid(self, form):
#         return super().form_valid(form)


class DonorListView(ListView):
    template_name= 'donorlist.html'
    model= Donor
    context_object_name  = 'donors' 
    

    def get_queryset (self):
        qs = Donor. objects.all()
        return qs

class DonorDeleteView(DeleteView):
     model = Donor
     template_name = 'donordelete.html'
     success_url = reverse_lazy('donorlist')


class DonorDetailView(DetailView):
    model = Donor
    template_name = 'donor-details.html'
    success_url = reverse_lazy('donorlist')       



class DonorCreateView(CreateView):
    model = Donor
    template_name = 'Diamond-create account.html'
    success_url = reverse_lazy('donorlist')

    class Meta:
        fields= ['username', 'email', 'password', 'phonenumber']

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            # Retrieve data from the request
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')

            # Create a new Donor instance
            donor = Donor(name=name, email=email, phone_number=phone_number)
            donor.save()  # Save the donor to the database

            # Redirect to the success URL
            return redirect(self.success_url)
        
        return render(request, self.template_name)
