from django.shortcuts import render
from fake_app.models import UserModel


# Create your views here.
def home(req):
    user_list = UserModel.objects.order_by('user_name')
    user_dict = {'users': user_list}
    return render(req, 'fake_app/home.html', context=user_dict)
