from msilib.schema import File
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','blueland.settings')
import django
django.setup()
from main.models import *
from django.conf import settings
brands = ['MHK MEDIKAL TEKSTIL','AUROLAB', 'VARITEKS',]
cats = {
    'Orthopedic Supports': ['Cervical Collars', 'Waist Corsets',   ],
    'Varicose Stocking' : ['1stv', '2ndv'    ],
}

cats = {
    'Orthopedic Supports': ['Cervical Collars', 'Waist Corsets', 'Abdominal Corsets', 'Knee Braces', 'Arm Slings',
                            'Hand-Wrist and Finger Splints', 'Shoulder and Elbow Supports', 'Ankle Braces and Foot Supports',
                            'Silicone Products', 'Nexus','Softsport', 'Orthopedic Pillows and Cushions', 'Silicone Products', 
                            'Kid Size Products'],
                            
    'Varicose Stocking' : ['Ccl I', 'Ccl II', 'Ccl III', 'Anti Embolism Stockings', 'Elastic Supports'],
}

if __name__ == '__main__':
    p = Partners.objects.first()
    for i in range (3):
        n = p 
        n.id = None 
        n.save()
    
    # for b in brands:
    #     n = Brand(name = b)
    #     n.save()
    # print("saved brands!")

    # for c in cats:
    #     n = Category(name = c)
    #     n.save() 
    #     print(f"saved category {n}")
    #     for s in cats[c]:
    #         m = Subcategory(name = s, category= n)
    #         m.save()
    #         print(f"saved subcategory {m}")
    


