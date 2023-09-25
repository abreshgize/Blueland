from django.shortcuts import render
from django.views import View
from main.models import Category, Mission, Partners, Product, Subcategory,Team, ContactUsMessages
from django import forms 

class ContactForm(forms.ModelForm):
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'cols':"30", 'rows':"10", 'placeholder':'Your Message'}))
    class Meta:
        model = ContactUsMessages
        fields = "__all__"
        widgets = {
            'name' :forms.TextInput(attrs={'placeholder':'Your Name'}),
            'email' :forms.EmailInput(attrs={'placeholder':'Your Email'}),
        }

# class EmailAcctivationThread(threading.Thread):
#     def __init__(self, request):
#         self.request= request
#         threading.Thread.__init__(self) 


#     def run(self):
#         try:
#             current_site = get_current_site(self.request)
#             mail_subject = 'You have a new message from your website.'
#             message = render_to_string('email/accounts/account_activation.html', {
#                 'user': self.user,
#                 'domain': current_site.domain,
#                 'uid':urlsafe_base64_encode(force_bytes(self.user.id)),#encode self.user id
#                 'token':account_activation_token.make_token(self.user),
               
#             })
#             to_email = self.user.email
#             email = EmailMultiAlternatives(mail_subject, message, 'mukeraacc@gmail.com', [to_email],)
#             email.attach_alternative(message, 'text/html')
#             email = email.send()
#             print(f"sent email acctivation to {to_email} ", email )
#             return (True, "sent email" ) 
#         except Exception as e:
#             print("Email Exception ", e)
#             return (False, e)



def Index(request):
    hot = Product.objects.filter(hot = True)[:6]
    new = Product.objects.filter(new =True)[:6]
    if not new:
        new = Product.objects.all()[:6]

    return render(request, 'index.html', {'index':True, 'new':new,'prods_count':Product.objects.count(), 'hot':hot,'partners':Partners.objects.all()})

    
class ProductList(View):
    def get(self, *args, **kwargs):
        ps = Product.objects.select_related('subcat').all()
        return render(self.request, 'products.html', {'ps':ps, 'cats':Category.objects.all()} )

class CategoryProducts(View):
    def get(self, *args, **kwargs):
        cat = Category.objects.get(id = self.kwargs['pk'])
        prods = Product.objects.filter(subcat__category = cat)
        return render(self.request, 'products.html', {'cat':cat,  'prods':prods})
    


class SubProducts(View):
    def get(self, *args, **kwargs):
        sub = Subcategory.objects.get(id = self.kwargs['pk'])
        prods = Product.objects.filter(subcat = sub)
        return render(self.request, 'products.html', {'cat':sub.category, 'sub':sub, 'prods':prods})

class ProductDetail(View):
    def get(self, *args, **kwargs):
        p = Product.objects.get(id = self.kwargs['pk'])
        related = Product.objects.filter(subcat = p.subcat).exclude(id = p.id)[:4]
        images  = p.productimages_set.all()
        return render(self.request, "product_detail.html", {'p':p, 'related':related, 'images':images})



class Aboutus(View): 
    def get(self, *args, **kwargs):
        prods_count = Product.objects.count() 
        partners_count = Partners.objects.count()
        return render(self.request, 'about.html', {'team':Team.objects.all(), 'prods_count':prods_count, 'partners_count':partners_count, 'm':Mission.objects.first()})

class Contact(View):
    def get(self, *args, **kwargs):
        return render(self.request, "contact.html", {'form':ContactForm(), 'm':Mission.objects.first()})
    
    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        
        if form.is_valid():
            form.save()
            return render(self.request, "contact.html", {'form':ContactForm})
    
        else:
            print(form.errors )
            return render(self.request, "contact.html", {'form':form})
    
        
        