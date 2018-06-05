from django.shortcuts import render, redirect
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def main(request):
    user_str = request.session.get('login_user')
    if user_str is None:
        return redirect('index:index')
    user = json.loads(user_str, encoding='utf-8')
    return render(request, 'main.html', user)