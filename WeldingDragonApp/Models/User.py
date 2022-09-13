from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self,username,password=None):
        """Crea y guarda un usuario con el nombre de usuario y la contraseña proporcionados."""
        if not username:
            raise ValueError('los usuarios deben tener nombre de usuario')
        user = self.model(username=username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser (self,username, password):
        """crea un super usuario con el nombre de usuario y la contraseña proporcionados"""
        user = self.create_user(username=username, password=password)
        user.is_admin = True
        user.save (using =self._db)
        return user
    
class User (AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    tipo_de_usuario = models.CharField('Tipo de Usuario', max_length=30)
    username = models.CharField('Nombre de Usuario', max_length=30,unique=True)
    password = models.CharField('Password', max_length = 256)
    nombre = models.CharField('Nombre',max_length=30)
    apellido = models.CharField('Apellido',max_length=30)
    cedula =  models.CharField ('Cedula',max_length=12)
    correo = models.EmailField('Email', max_length = 100)
    tipo_de_Cliente =models.CharField('Tipo de cliente',max_length=20)
    
    def save (self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        self.password = make_password(self.password,some_salt)
        super().save(**kwargs)
        
    objects = UserManager()
    USERNAME_FIELD = 'username'