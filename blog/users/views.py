from django.shortcuts import render

# Create your views here.

from django.views import View

#注册视图
class RegisterView(View):

    def get(self,request):

        return render(request,'register.html')