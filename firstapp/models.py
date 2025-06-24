from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

# Create your models here.

CATEGORY_CHOICES={
    ('CR','Curd'),
    ('ML','Milk'),
    ('LS','Lassi'),
    ('MS','Milkshake'),
    ('PN','Paneer'),
    ('GH','Ghee'),
    ('CZ','Cheese'),
    ('IC','Ice-Creams'),
}

STATE_CHOICES = (
   ("AN","Andaman and Nicobar Islands"),
   ("AP","Andhra Pradesh"),
   ("AR","Arunachal Pradesh"),
   ("AS","Assam"),
   ("BR","Bihar"),
   ("CG","Chhattisgarh"),
   ("CH","Chandigarh"),
   ("DN","Dadra and Nagar Haveli"),
   ("DD","Daman and Diu"),
   ("DL","Delhi"),
   ("GA","Goa"),
   ("GJ","Gujarat"),
   ("HR","Haryana"),
   ("HP","Himachal Pradesh"),
   ("JK","Jammu and Kashmir"),
   ("JH","Jharkhand"),
   ("KA","Karnataka"),
   ("KL","Kerala"),
   ("LA","Ladakh"),
   ("LD","Lakshadweep"),
   ("MP","Madhya Pradesh"),
   ("Maharashtra","Maharashtra"),
   ("MN","Manipur"),
   ("ML","Meghalaya"),
   ("MZ","Mizoram"),
   ("NL","Nagaland"),
   ("OD","Odisha"),
   ("PB","Punjab"),
   ("PY","Pondicherry"),
   ("RJ","Rajasthan"),
   ("SK","Sikkim"),
   ("TN","Tamil Nadu"),
   ("TS","Telangana"),
   ("TR","Tripura"),
   ("UP","Uttar Pradesh"),
   ("UK","Uttarakhand"),
   ("WB","West Bengal")
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    composition = models.TextField(default='')
    prodapp = models.TextField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product')
    def __str__(self):
        return self.title


# class Customer(models.Model):
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     locality = models.CharField(max_length=200)
#     city = models.CharField(max_length=100)
#     mobile = models.IntegerField(default=0)
#     zipcode = models.IntegerField()
#     state =  models.CharField(choices=STATE_CHOICES,max_length=100)
#     def __str__(self):
#         return self.name



# from django.db import models
# from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

# # Regex: starts with +country_code followed by exactly 10 digits
# mobile_validator = RegexValidator(
#     regex=r'^\+?\d{1,3}[- ]?\d{10}$',
#     message='Enter a valid mobile number with country code (e.g. +91-9876543210 or +919876543210)'
# )

# STATE_CHOICES = [
#     ('State1', 'State1'),
#     ('State2', 'State2'),
#     # add more as needed
# ]

# class Customer(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=200)
#     locality = models.CharField(max_length=200)
#     city = models.CharField(max_length=100)
#     mobile = models.CharField(validators=[mobile_validator], max_length=16)
#     zipcode = models.IntegerField()
#     state = models.CharField(choices=STATE_CHOICES, max_length=100)

#     def __str__(self):
#         return self.name




# Regex: starts with +country_code followed by exactly 10 digits
mobile_validator = RegexValidator(
    regex=r'^\+?\d{1,3}[- ]?\d{10}$',
    message='Enter a valid mobile number with country code (e.g. +91-9876543210 or +919876543210)'
)

COUNTRY_CHOICES = [
    ('+1', 'United States'),
    ('+44', 'United Kingdom'),
    ('+1', 'Canada'),
    ('+61', 'Australia'),
    ('+91', 'India'),
    ('+49', 'Germany'),
    ('+33', 'France'),
    ('+86', 'China'),
    ('+81', 'Japan'),
    ('+82', 'South Korea'),
    ('+55', 'Brazil'),
    ('+27', 'South Africa'),
    ('+7', 'Russia'),
    ('+52', 'Mexico'),
    ('+39', 'Italy'),
    ('+34', 'Spain'),
    ('+31', 'Netherlands'),
    ('+65', 'Singapore'),
    ('+971', 'UAE'),
    ('+966', 'Saudi Arabia'),
]

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    mobile = models.CharField(validators=[mobile_validator], max_length=16)
    zipcode = models.IntegerField()
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=6)

    def __str__(self):
        return self.name



class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

STATUS_CHOICES = (
    ('Accepted','Accepted'),
    ('Packed', 'Packed'),
    ('On The Way', 'On The Way'),
    ('Delivered', 'Delivered'),
    ('Cancel', 'Cancel'),
    ('Pending', 'Pending'),
)

class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField()
    razorpay_order_id = models.CharField(max_length=100,blank=True,null=True)
    razorpay_payment_status = models.CharField(max_length=100, blank=True, null=True)
    razorpay_payment_id = models.CharField(max_length=100, blank=True, null=True)
    paid = models.BooleanField(default=False)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE,default="")
    @property
    def total_cost(self):
        return self.quantity * self.product.discounted_price

