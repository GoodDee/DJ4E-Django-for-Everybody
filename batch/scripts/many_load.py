import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Category, Region, State, Iso, Site


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    # Clear all tables
    Category.objects.all().delete()
    Region.objects.all().delete()
    State.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()


    for row in reader:
        print(row)
        c, created = Category.objects.get_or_create(name=row[7])
        r, created = Region.objects.get_or_create(region=row[9])
        s, created = State.objects.get_or_create(state=row[8])
        i, created = Iso.objects.get_or_create(iso=row[-1])

        try:
            y = int(row[3])
        except:
            y = None

        try:
            longitude, latitude = int(row[4]), int(row[5])
        except:
            longitude, latitude = None, None

        try:
            area = int(row[6])
        except:
            area = None


        site = Site(name=row[0], description=row[1], justification = row[2], year=y,
                    longitude = longitude, latitude = latitude, area_hectares = area,
                    category = c, state = s, region = r, iso = i)
        site.save()
