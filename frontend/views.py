from django.shortcuts import render

def user_page(request):
   return render(request, 'FE/users.html')  # create this template
