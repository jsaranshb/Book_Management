from django.db import models
from django.contrib.auth.models import AbstractUser

# from sqlalchemy import create_engine
  
# # # DEFINE THE DATABASE CREDENTIALS
# user = 'postgres'
# password = 'Saransh#999'
# host = 'saranshdb1.cm0pvbcyghvn.ap-south-1.rds.amazonaws.com'
# port = 5432
# database = 'postgres'
  
# # PYTHON FUNCTION TO CONNECT TO THE POSTGRESQL DATABASE AND
# # RETURN THE SQLACHEMY ENGINE OBJECT
# def get_connection():
#     return create_engine(
#         url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
#             user, password, host, port, database
#         )
#     )
  
  
# if __name__ == '__main__':
  
#     try:
#         # GET THE CONNECTION OBJECT (ENGINE) FOR THE DATABASE
#         engine = get_connection()
#         print(
#             f"Connection to the {host} for user {user} created successfully.")
#     except Exception as ex:
#         print("Connection could not be made due to the following error: \n", ex)

# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=200, null = False, unique = True)
    fullname = models.CharField(max_length=200)
    email = models.EmailField(null = False)
    public_visibility = models.BooleanField(default="True", null=False)
    birthday_year = models.DateField(null=True, blank=True)    
    address = models.CharField(max_length=200, null = True)
    password = models.CharField(max_length=200)
    confirm_password = models.CharField(max_length=200, null = False, default = 0 )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email',]

    def __str__(self):
        return self.username
    
class uploaded_files(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, default=1)
    book_title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    visibility = models.BooleanField(default="True", null=True)
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    published_year = models.CharField(max_length=200, null=True, blank=True)
    book_file = models.FileField(upload_to = 'book_files/', null=True)

    def __str__(self):
        return self.book_title
    