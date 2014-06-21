import os

from wafer.settings import *

try:
    from localsettings import *
except ImportError:
    pass

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse_lazy

pyconzadir = os.path.dirname(__file__)


STATICFILES_DIRS = (
    os.path.join(pyconzadir, 'static'),
)

TEMPLATE_DIRS = (
    os.path.join(pyconzadir, 'templates'),
) + TEMPLATE_DIRS


WAFER_MENUS += (
    {"menu": "about", "label": _("About"),
     "items": []},
    #{"menu": "venue", "label": _("Venue"),
    # "items": []},
    {"menu": "sponsors", "label": _("Sponsors"),
     "items": [
         {"name": "sponsors", "label": _("Our sponsors"),
          "url": reverse_lazy("wafer_sponsors")},
         {"name": "packages", "label": _("Sponsorship packages"),
          "url": reverse_lazy("wafer_sponsorship_packages")},
     ]},
    {"menu": "talks", "label": _("Talks"),
     "items": [
         {"name": "accepted-talks", "label": _("Accepted Talks"),
          "url": reverse_lazy("wafer_users_talks")},
     ]},
    {"menu": "previous-pycons", "label": _("Past PyConZAs"),
     "items": [
         {"name": "pyconza2012", "label": _("PyConZA 2012"),
          "url": "http://2012.za.pycon.org/"},
         {"name": "pyconza2013", "label": _("PyConZA 2013"),
          "url": "http://2013.za.pycon.org/"},
     ]},
    {"name": "twitter", "label": "Twitter",
     "image": "/static/img/twitter.png",
     "url": "https://twitter.com/pyconza"},
)


CRISPY_TEMPLATE_PACK = 'bootstrap'
MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})
