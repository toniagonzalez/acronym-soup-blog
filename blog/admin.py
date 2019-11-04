from django.contrib import admin
from .models import Volume
from .models import Text
from .models import Image
from .models import Spanish
from .models import TextSpanish
from .models import ImageSpanish

# Models registered here.
admin.site.register(Volume)
admin.site.register(Text)
admin.site.register(Image)
admin.site.register(Spanish)
admin.site.register(TextSpanish)
admin.site.register(ImageSpanish)
