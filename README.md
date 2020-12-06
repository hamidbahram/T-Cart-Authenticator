# authenticator system
# django-3.1.4


installation
--------------------
- requirements:
- python 3.7 install following packages via **pip** or **easy_install**
- `pip install -r requirements.txt`
- create database step 1 `python manage.py migrate`
- create database step 2 `python manage.py makemigrations`
- create database step 3 `python manage.py migrate`
- run your server by typing `python manage.py runserver`
- url `http://localhost:8000/graphql/`

> **Note:**

> - You need to create an admin user to manage your blog site by this command: `python manage.py createsuperuser`

> **PLEASE READE THE BELOW**

```
1 - Detail All User

query{
  allUser{
    fName
    lName
    # sex
    phoneNumber
  }
}


2 - Add User

mutation{
  addUser(phone:"0912*******",firstName:"name",lastName:"name",sex:true,email:"aaaaa@gmail.com"){
    response{
      status
      statusCode
      message
    }
  }
}


3 - check code

mutation{
  checKcode(phone:"0912*******", code: code){
    response{
      status
      message
    }
  }
}
```