from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()
u = User.objects.get(username='youruser')   # or create one
token, created = Token.objects.get_or_create(user=u)
print(token.key)
