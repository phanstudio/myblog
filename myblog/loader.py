import os
from django.conf import settings



# BASE_DIR = Path(__file__).resolve().parent.parent
def imporT_(_file):
    _file = os.path.join(settings.BASE_DIR, _file)
    if os.path.exists(_file):
        with open(_file, "r") as f:
            return f.read()
    else: return ""


# print(imporT_("PGDATABASE.txt", BASE_DIR))
