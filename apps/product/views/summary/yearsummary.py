# import calendar
# import json
from typing import Tuple

# third-party
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.product.models import Product

# from django.db.models import Count
# from django.conf import settings
# from django.http import JsonResponse

# from django.views.decorators.csrf import csrf_exempt


@api_view(["POST"])
def ProdYearSummaryView(request):
    """
    ...
    """

    # json_data: Dict[str, Any] = json.loads(request.body.decode("utf-8"))
    # print(json_data)

    # COUNT

    total_count: int = Product.objects.count()

    # tag_total_count: Dict[str, int] = {
    #     'enter': 0,
    #     'exit': 0,
    #     'cancel': 0
    # }

    # tag_total_count['enter'] = Product.objects.filter(
    #     tag='ENTER',
    #     updated__year=2020,
    # ).count()
    # tag_total_count['exit'] = Product.objects.filter(
    #     tag='EXIT',
    #     updated__year=2020,
    # ).count()
    # tag_total_count['cancel'] = Product.objects.filter(
    #     tag='CANCEL',
    #     updated__year=2020,
    # ).count()

    # list_name_count = tuple(Product.objects.values('name').annotate(
    #     count=Count('name')
    # ))
    # list_name_count = Product.objects.values('name').annotate(
    #     count=Count('name')
    # ).explain()

    # YEAR

    year_summary = []

    months: Tuple[str] = (
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    )

    for number, name in enumerate(months):
        # print(number + 1, name)
        year_summary.append({"number": number + 1, "name": name, "count": 0})

    return Response(
        {"total": total_count, "year_summary": year_summary}, status=status.HTTP_200_OK
    )
