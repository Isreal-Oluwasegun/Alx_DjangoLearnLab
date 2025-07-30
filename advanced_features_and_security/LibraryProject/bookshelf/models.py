from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError("User must have email address")
        user = self.model(self.normalize_email(email))
        user.set_password(password)
        user.save(using = user._db)
        return user
    
    def create_superuser(self, email, password):
        user =self.crete_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)


class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to="profile/")

    objects = UserManager()

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title
