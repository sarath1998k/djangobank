from .models import District, Branches


def menu_objects(request):
    district_objects = District.objects.all()
    branch_objects = Branches.objects.all()

    return dict(district_objects=district_objects, center_objects=branch_objects)