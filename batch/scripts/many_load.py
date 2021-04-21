import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, States, Region, Iso


def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    States.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    Site.objects.all().delete()



    count = 0
    for row in reader:
        count+=1
        print(count)
        #print(row[7],count)
        #print(row[0])
        #Site.name = row[0]
        #print(Site.name)
        #s, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=y,longitude=row[4], latitude=row[5], area_hectares=a, iso=i)
        #n, created = Site.objects.get_or_create(name=row[0])

        #d, created = Site.objects.get_or_create(description=row[1])
        #j, created = Site.objects.get_or_create(justification=row[2])

        #y, created = Site.objects.get_or_create(my_try('year',3))

        #lo, created = Site.objects.get_or_create(my_try('longitude',4))

        #la, created = Site.objects.get_or_create(my_try('latitude',5))

        #a, created = Site.objects.get_or_create(my_try('area_hectares',6))

        c, created = Category.objects.get_or_create(name=row[7])

        s, created = States.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        #c = Category(name=c)
        c.save()
        #s = States(name=s)
        s.save()
        #r = Region(name=r)
        r.save()
        #i = Iso(name=i)
        i.save()

        try:
            y=int(row[3])
        except:
            y=None
        try:
            a=float(row[6])
        except:
            a=None
        #print(a)

        si, created = Site.objects.get_or_create(name=row[0], description=row[1], justification=row[2], year=y,longitude=row[4], latitude=row[5],
        area_hectares=a, category=c, states=s, region=r, iso=i)
        #si = Site(name=n, description=d, justification=j, year=y, longitude=lo, latitude=la, area_hectares=a)
        #print(created)
        #print(si)

        si.save()


