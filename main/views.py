from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect , HttpResponse , render
from .models import SportProgram , NutrientProgram , Coach
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import ProgramRequestForm
from django.contrib.auth import get_user_model
from django.db import connection

#python manage.py sqlmigrate
#python manage.py showmigrations
#psql -U postgres

class Landing(View):
    
    
    def get(self, request, *args, **kwargs):
        
        programs = SportProgram.objects.all()
        nutrients = NutrientProgram.objects.all()
        
        print(connection.queries)
        
        context = {
            'programs': programs,
            'nutrients':nutrients
        }
        
        return render(request,'main/index.html', context)
    
    def post(self , request):
        pass


class ProgramDetail(View):
    
    def get(self,request, program_id):
        
        program = get_object_or_404(SportProgram, program_id=program_id)

        print(connection.queries)
        # Pass the program to the template
        context = {
            'program': program
        }
        
        return render(request, 'main/program_detail.html', context)
    
    def post(self , request):
        pass


class NutrientDetail(View):
    
    def get(self,request, program_id):
        
        nutrient = get_object_or_404(NutrientProgram, program_id=program_id)

        print(connection.queries)
        # Pass the program to the template
        context = {
            'nutrient': nutrient
        }
        
        return render(request, 'main/nutrient_detail.html', context)
    
    def post(self , request):
        pass
    

class CoachExplore(View):
    
    
    def get(self, request, *args, **kwargs):
        
        Coachs = Coach.objects.all()
        
        print(connection.queries)
        context = {
            'Coachs': Coachs,
        }
        
        return render(request,'main/Coaches.html', context)
    
    def post(self , request):
        pass

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(connection.queries)
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('main:login')  # Redirect to login page after signup
        else:
            # Print form errors to the console for debugging
            print("Form errors:", form.errors)
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()
    return render(request, 'main/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(connection.queries)
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('main:index') 
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})



def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('main:index') 


class ProgramRequestView(LoginRequiredMixin, FormView):
    template_name = "main/program_request_form.html" 
    form_class = ProgramRequestForm
    success_url = reverse_lazy('main:index')  

    print(connection.queries)
    def form_valid(self, form):

        program_request = form.save(commit=False)
        program_request.save()
        return super().form_valid(form)