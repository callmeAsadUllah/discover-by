from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import (
    authenticate,
    login
)
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):
    title = 'discover'
    
    context = {
        'title': title
    }
    
    return render(
        request,
        'account/dashboard.html',
        context
    )