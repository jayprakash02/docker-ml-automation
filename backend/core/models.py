from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.
PLATFORM=(
    ("tensorflow", "tensorflow"),
    ("other","other")
)
class Version(models.Model):
    version = models.IntegerField(_("Version"),default=1)
    
    def __str__(self):
        return str(self.version)

class Tfmodel(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    base_path = models.CharField(_("Path"), max_length=50)
    model_platform = models.CharField(_("Platform"),choices=PLATFORM, max_length=20)
    version = models.ManyToManyField("core.Version", verbose_name=_("Version"),related_name="model_version")

    def __str__(self):
        return self.name

    def clean(self):
        if len(self.base_path)!=len(self.name)+9 or self.base_path[:8]!='/models/' or self.base_path[8:len(self.base_path)-1]!=self.name:
            raise ValidationError(_('Path should be in this format only /models/<name>/'))