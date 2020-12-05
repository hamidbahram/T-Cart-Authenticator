import graphene
from graphene_django.types import DjangoObjectType
from t_profile.models import UserProfle
from random import randint


class ProfileType(DjangoObjectType):
    # sex = graphene.Boolean()

    # def resolve_sex(self, info):
    #     return self.sex

    class Meta:
        model = UserProfle
        # only_fields = ("f_name", "l_name", "sex", "phone_number")

class Query(graphene.ObjectType):
    all_user = graphene.List(ProfileType)

    def resolve_all_user(root, info):
        return UserProfle.objects.all()


# add user
class ResponseUser(graphene.ObjectType):
    status = graphene.String()
    status_code = graphene.Int()
    message = graphene.String()


class AddUser(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        phone = graphene.String(required=True)
        sex = graphene.Boolean()
        email = graphene.String()

    response = graphene.Field(ResponseUser)

    def mutate(self, info, first_name, last_name, phone, sex, email, **kwargs):
        code = randint(1000, 9999)
        user, created = UserProfle.objects.get_or_create(
            username=phone, 
            f_name=first_name, 
            l_name=last_name, 
            _sex=sex, 
            email=email,
        )

        if not created:
            response = user.refresh_code(code)
            return AddUser(response=response)

        else:
            response = user.create_code(code)
            return AddUser(response=response)


class ResponseCode(graphene.ObjectType):
    status = graphene.Int()
    message = graphene.String()


class CheckCode(graphene.Mutation):
    class Arguments:
        phone = graphene.String(required=True)
        code = graphene.Int(required=True)

    response = graphene.Field(ResponseCode)


    def mutate(self, info, code, phone, **kwargs):
        user = UserProfle.objects.get(username=phone)
        if user.active_code != code:
            return CheckCode(
                response={"status": 403, "message": "کد نامعتبر است"})
        user.is_active = True
        user.save()
        return CheckCode(response={"status": 200, "message": "خوش امدید"})



class Mutation(object):
    add_user   = AddUser.Field()
    chec_kcode = CheckCode.Field()