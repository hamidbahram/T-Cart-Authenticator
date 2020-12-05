# import requests
from django.db import models
from django.contrib.auth.models import AbstractUser



SEX_TYPES = (
    (False, 'خانم'),
    (True, 'آقا'),
)

class UserProfle(AbstractUser):
    f_name       = models.CharField(max_length=50, null=True)
    l_name       = models.CharField(max_length=50, null=True)
    _sex         = models.BooleanField(choices=SEX_TYPES, null=True, default=True)
    birth_date   = models.DateField(null=True, blank=True)
    email        = models.EmailField(max_length = 254, null=True, default=True) 
    location     = models.TextField(null=True, blank=True)
    active_code  = models.IntegerField(null=True)

    def __str__(self):
        return self.f_name

    # getter
    @property
    def sex(self):
        return dict(SEX_TYPES).get(self._sex)

    @sex.setter
    def sex(self, value):
        self._sex = {v: k for k, v in SEX_TYPES}.get(value)

    def refresh_code(self, code):
        self.active_code = code
        self.save()
        return {"status_code": 201, "status":"ok", "message": f"{code} کد رفرش شد"}

    def create_code(self, code):
       self.active_code = code
       self.is_active = False
       self.save()
       return {"status_code": 201, "status":'ok', "message": f"{code} کد ارسال شد"}
