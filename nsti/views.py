from django.core.mail import send_mail,EmailMultiAlternatives
from django.shortcuts import render
from .forms import *


def home(request):
   a= 'TestnMail from django '
   b= 'Mailer body , THANK YOU.'
   c= 'hanuman2241@gmail.com'
   d= ['hanumanup45@gmail.com']
   send_mail(a,b,c,d)
   return render(request, 'index.html')




def mailer(request):
   subject= 'Django',
   body= "<h1 style='color:red'>Thank you.</h1><button>Click to verify</button>"  

   from_email= 'hanuman2241@gmail.com'
   recipient_list= ['hanumanup45@gmail.com']
   mail= EmailMultiAlternatives(subject,body,from_email,recipient_list)
   mail.content_subtype='html'
   mail.send()

   return render(request, 'index2.html')



def contact(request):
   a= contactForm()

   if request.method=='POST':
      b= request.POST.get('name')
      c= request.POST.get('email')
      d= request.POST.get('message')
      e= request.POST.get('phone')
      

      f= "Dear {},Thank you for contacting us. Your msg is {}".format(b,d)
      send_mail('Test',d,'hanumanup45@gmail.com',[c])
      return render(request,'index.html', {'form': a})
   else :pass
   return render(request,'index.html',{'form':a})



def sell(request):
   return render(request,'sell.html')
   
   
