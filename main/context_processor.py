from main.models import Category

def get_cats(request):
   
   return {'cats':Category.objects.all()}