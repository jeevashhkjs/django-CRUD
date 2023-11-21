from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Users, UserScore
from .serializers import UserScoreSerializer

@receiver(post_save, sender=Users)
def check_signal(sender, instance, **kwargs) :
    get_data = {'number':4}
    serializer_data = UserScoreSerializer(data=get_data)

    if serializer_data.is_valid() :
        serializer_data.save()
        print("added")
    else :
        print("not added")

post_save.connect(check_signal, Users)