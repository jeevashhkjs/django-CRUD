from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Users, UserScore
from .serializers import UserScoreSerializer

@receiver(post_save, sender=Users)
def check_signal(sender, instance, **kwargs) :
    updated_number = instance.number
    db_number = UserScore.objects.get(id=1).number
    UserScore.objects.filter(id=1).update(number= updated_number + db_number)
    print("added")