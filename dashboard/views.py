from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import UploadFileForm
from .models import EmploymentData
from django.db.models import Avg, Max
import csv
import json

def home(request):
    form = UploadFileForm()

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            file = request.FILES.get('file')

            if file:
                data = file.read().decode('utf-8').splitlines()
                reader = csv.DictReader(data)

               
                EmploymentData.objects.all().delete()

                for row in reader:
                    try:
                        EmploymentData.objects.create(
                            year=int(row['Year']),
                            month=row['Month'].strip(),
                            province=row['Province'].strip(),
                            employment=float(row['Employment (Millions)']),
                            unemployment_rate=float(row['Unemployment rate (%)']),
                            employment_rate=float(row['Employment rate (%)']),
                            participation_rate=float(row['Participation rate (%)']),
                        )
                    except:
                        continue

                return redirect('dashboard')

    return render(request, 'home.html', {'form': form})



def get_province_stats(data):
    provinces = []
    employment = []
    unemployment = []

    for d in data:
        if d.province not in provinces:
            provinces.append(d.province)

    for p in provinces:
        avg_emp = data.filter(province=p).aggregate(Avg('employment'))['employment__avg']
        avg_unemp = data.filter(province=p).aggregate(Avg('unemployment_rate'))['unemployment_rate__avg']

        employment.append(round(avg_emp or 0, 2))
        unemployment.append(round(avg_unemp or 0, 2))

    return provinces, employment, unemployment


# DASHBOARD
def dashboard(request):
    data = EmploymentData.objects.all()

    # KPI data
    total_records = data.count()
    avg_employment = round(data.aggregate(Avg('employment'))['employment__avg'] or 0, 2)
    avg_unemployment = round(data.aggregate(Avg('unemployment_rate'))['unemployment_rate__avg'] or 0, 2)
    latest_year = data.aggregate(Max('year'))['year__max']

    # Best province
    provinces_data = data.values('province').annotate(avg_emp=Avg('employment')).order_by('-avg_emp')
    best_province = provinces_data.first()['province'] if provinces_data else "N/A"

    # Chart data
    provinces, employment, unemployment = get_province_stats(data)

    context = {
        'total_records': total_records,
        'avg_employment': avg_employment,
        'avg_unemployment': avg_unemployment,
        'latest_year': latest_year,
        'best_province': best_province,

        # chart support
        'provinces': json.dumps(provinces),
        'employment': json.dumps(employment),
    }

    return render(request, 'dashboard.html', context)


#PROVINCE PAGE
def province_page(request):
    data = EmploymentData.objects.all()

    provinces, employment, unemployment = get_province_stats(data)

    return render(request, 'province.html', {
        'provinces': json.dumps(provinces),
        'employment': json.dumps(employment),
        'unemployment': json.dumps(unemployment),
        'provinces_list': provinces
    })


# DISTRIBUTION PAGE 
def distribution_page(request):
    data = EmploymentData.objects.all()

    provinces, employment, _ = get_province_stats(data)

    return render(request, 'distribution.html', {
        'provinces': json.dumps(provinces),
        'employment': json.dumps(employment),
    })


#  TREND PAGE 
def trend_page(request):
    data = EmploymentData.objects.all()

    years = sorted(set(d.year for d in data))
    year_employment = []

    for y in years:
        avg = data.filter(year=y).aggregate(Avg('employment'))['employment__avg']
        year_employment.append(round(avg or 0, 2))

    return render(request, 'trend.html', {
        'years': json.dumps(years),
        'year_employment': json.dumps(year_employment),
        'provinces_list': sorted(set(d.province for d in data))
    })


#  AJAX FILTER
def filter_data(request):
    province = request.GET.get('province')
    data = EmploymentData.objects.all()

    if province:
        data = data.filter(province=province)

    provinces, employment, unemployment = get_province_stats(data)

    years = sorted(set(d.year for d in data))
    year_employment = []

    for y in years:
        avg = data.filter(year=y).aggregate(Avg('employment'))['employment__avg']
        year_employment.append(round(avg or 0, 2))

    return JsonResponse({
        'provinces': provinces,
        'employment': employment,
        'unemployment': unemployment,
        'years': years,
        'year_employment': year_employment
    })
