from django.shortcuts import render, redirect, get_object_or_404
import requests
from .models import *
import json
from django.views import View
from datetime import datetime, timedelta
from farms_database import settings
from django.core.mail import send_mail
from farms.forms import *
# Create your views here.
class HomeView(View):
    def get(self, request):
        form = NewsLetterForm()
        crops = Crop.objects.all()
        newslist = WhatsNew.objects.all()
        crops_rainy = Crop.objects.filter(category=2)
        crops_dry = Crop.objects.filter(category=1)
        url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?q=Zamboanga City&units=metric&cnt=30&appid=1047600834087dd796420df1c5149a42'
        city = 'Zamboanga City'
        total_dry = 0
        total_rain = 0
        city_weather_data = requests.get(url.format(city)).json()
        city_weather = json.dumps(city_weather_data)
        count_sky = city_weather.count('clear sky')
        count_few_clouds = city_weather.count('few clouds')
        count_scattered_clouds = city_weather.count('scattered clouds')
        count_broken_clouds = city_weather.count('broken clouds')
        count_light_rain = city_weather.count('light rain')
        count_moderate_rain = city_weather.count('moderate rain')
        count_shower_rain = city_weather.count('shower rain')
        count_heavy_intensity_rain = city_weather.count('heavy intensity rain')
        count_very_heavy_rain = city_weather.count('very heavy rain')

        total_dry = count_sky + count_few_clouds + count_scattered_clouds + count_broken_clouds
        total_rain = count_light_rain + count_moderate_rain + count_shower_rain + count_heavy_intensity_rain + count_very_heavy_rain
    
        day_1 = datetime.now().date()
        day_30 = datetime.now() + timedelta(days=29)

        format_date_1 = day_1.strftime("%a, %b-%d")
        format_date_30 = day_30.strftime("%a, %b-%d")

        context = {
        'form':form,
        'crops':crops,
        'newslist':newslist,
        'crops_dry':crops_dry,
        'crops_rainy':crops_rainy,
        'total_dry':total_dry,
        'total_rain':total_rain,
        'format_date_1':format_date_1,
        'format_date_30':format_date_30
        }
        return render(request, 'store/index.html', context)

    def post(self, request):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            email_address = form.cleaned_data['email_address']
            reg = NewsLetter(email_address=email_address)
            subject = 'Thank you for Subscribing!'
            message = 'Greetings! ' + form.cleaned_data['email_address'] + '\nYou will be updated to the latest news from our webpage. \nPlease contact us for your concerns.'
            from_email = settings.DEFAULT_FROM_EMAIL
            to_list = [form['email_address'].value()]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            reg.save()
        return redirect('farms:home')


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'store/contact.html', {'form':form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data['fname']
            email_address = form.cleaned_data['email_address']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            reg = Contact(fname=fname, email_address=email_address, subject=subject, message=message)
            reg.save()
        return redirect('farms:home')

def categories(request):
    crops = Crop.objects.all()
    crops_rainy = Crop.objects.filter(category=2)
    crops_dry = Crop.objects.filter(category=1)
    url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?q=Zamboanga City&units=metric&cnt=30&appid=1047600834087dd796420df1c5149a42'
    city = 'Zamboanga City'
    total_dry = 0
    total_rain = 0
    city_weather_data = requests.get(url.format(city)).json()
    city_weather = json.dumps(city_weather_data)
    count_sky = city_weather.count('clear sky')
    count_few_clouds = city_weather.count('few clouds')
    count_scattered_clouds = city_weather.count('scattered clouds')
    count_broken_clouds = city_weather.count('broken clouds')
    count_light_rain = city_weather.count('light rain')
    count_moderate_rain = city_weather.count('moderate rain')
    count_shower_rain = city_weather.count('shower rain')
    count_heavy_intensity_rain = city_weather.count('heavy intensity rain')
    count_very_heavy_rain = city_weather.count('very heavy rain')
 
    total_dry = count_sky + count_few_clouds + count_scattered_clouds + count_broken_clouds
    total_rain = count_light_rain + count_moderate_rain + count_shower_rain + count_heavy_intensity_rain + count_very_heavy_rain
    
    day_1 = datetime.now().date()
    day_30 = datetime.now() + timedelta(days=29)

    format_date_1 = day_1.strftime("%a, %b-%d")
    format_date_30 = day_30.strftime("%a, %b-%d")

    context = {
        'crops':crops,
        'crops_dry':crops_dry,
        'crops_rainy':crops_rainy,
        'total_dry':total_dry,
        'total_rain':total_rain,
        'format_date_1':format_date_1,
        'format_date_30':format_date_30
    }
    return render(request, 'store/category.html', context)

def detail(request,slug):
    crop = get_object_or_404(Crop, slug=slug)
    url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?q=Zamboanga City&units=metric&cnt=30&appid=1047600834087dd796420df1c5149a42'
    city = 'Zamboanga City'
    total_dry = 0
    total_rain = 0
    city_weather_data = requests.get(url.format(city)).json()
    city_weather = json.dumps(city_weather_data)
    
    count_sky = city_weather.count('clear sky')
    count_few_clouds = city_weather.count('few clouds')
    count_scattered_clouds = city_weather.count('scattered clouds')
    count_broken_clouds = city_weather.count('broken clouds')
    count_light_rain = city_weather.count('light rain')
    count_moderate_rain = city_weather.count('moderate rain')
    count_shower_rain = city_weather.count('shower rain')
    count_heavy_intensity_rain = city_weather.count('heavy intensity rain')
    count_very_heavy_rain = city_weather.count('very heavy rain')
 
    total_dry = count_sky + count_few_clouds + count_scattered_clouds + count_broken_clouds
    total_rain = count_light_rain + count_moderate_rain + count_shower_rain + count_heavy_intensity_rain + count_very_heavy_rain
    print(f'{total_dry=}')
    print(f'{total_rain=}')

    context = {
        'crop':crop,
        'total_dry':total_dry,
        'total_rain':total_rain,
        "city":city,
        "temperature":city_weather_data['list'][0]['temp']['day'],
        "description":city_weather_data['list'][0]['weather'][0]['description'],
        "icon":city_weather_data['list'][0]['weather'][0]['icon']
    }
    return render(request, 'store/crop-details.html', context)

def services(request):
    url = 'https://pro.openweathermap.org/data/2.5/forecast/climate?q=Zamboanga City&units=metric&cnt=30&appid=1047600834087dd796420df1c5149a42'
    city = 'Zamboanga City'
    total_dry = 0
    total_rain = 0
    city_weather = requests.get(url.format(city)).json()
    city_weather_data = json.dumps(city_weather)
    count_sky = city_weather_data.count('clear sky')
    count_few_clouds = city_weather_data.count('few clouds')
    count_scattered_clouds = city_weather_data.count('scattered clouds')
    count_broken_clouds = city_weather_data.count('broken clouds')
    count_light_rain = city_weather_data.count('light rain')
    count_moderate_rain = city_weather_data.count('moderate rain')
    count_shower_rain = city_weather_data.count('shower rain')
    count_heavy_intensity_rain = city_weather_data.count('heavy intensity rain')
    count_very_heavy_rain = city_weather_data.count('very heavy rain')
 
    total_dry = count_sky + count_few_clouds + count_scattered_clouds + count_broken_clouds
    total_rain = count_light_rain + count_moderate_rain + count_shower_rain + count_heavy_intensity_rain + count_very_heavy_rain

    day_1 = datetime.now().date()
    day_2 = datetime.now() + timedelta(days=1)
    day_3 = datetime.now() + timedelta(days=2)
    day_4 = datetime.now() + timedelta(days=3)
    day_5 = datetime.now() + timedelta(days=4)
    day_6 = datetime.now() + timedelta(days=5)
    day_7 = datetime.now() + timedelta(days=6)
    day_8 = datetime.now() + timedelta(days=7)
    day_9 = datetime.now() + timedelta(days=8)
    day_10 = datetime.now() + timedelta(days=9)
    day_11 = datetime.now() + timedelta(days=10)
    day_12 = datetime.now() + timedelta(days=11)
    day_13 = datetime.now() + timedelta(days=12)
    day_14 = datetime.now() + timedelta(days=13)
    day_15 = datetime.now() + timedelta(days=14)
    day_16 = datetime.now() + timedelta(days=15)
    day_17 = datetime.now() + timedelta(days=16)
    day_18 = datetime.now() + timedelta(days=17)
    day_19 = datetime.now() + timedelta(days=18)
    day_20 = datetime.now() + timedelta(days=19)
    day_21 = datetime.now() + timedelta(days=20)
    day_22 = datetime.now() + timedelta(days=21)
    day_23 = datetime.now() + timedelta(days=22)
    day_24 = datetime.now() + timedelta(days=23)
    day_25 = datetime.now() + timedelta(days=24)
    day_26 = datetime.now() + timedelta(days=25)
    day_27 = datetime.now() + timedelta(days=26)
    day_28 = datetime.now() + timedelta(days=27)
    day_29 = datetime.now() + timedelta(days=28)
    day_30 = datetime.now() + timedelta(days=29)

    format_date_1 = day_1.strftime("%a, %b-%d")
    format_date_2 = day_2.strftime("%a, %b-%d")
    format_date_3 = day_3.strftime("%a, %b-%d")
    format_date_4 = day_4.strftime("%a, %b-%d")
    format_date_5 = day_5.strftime("%a, %b-%d")
    format_date_6 = day_6.strftime("%a, %b-%d")
    format_date_7 = day_7.strftime("%a, %b-%d")
    format_date_8 = day_8.strftime("%a, %b-%d")
    format_date_9 = day_9.strftime("%a, %b-%d")
    format_date_10 = day_10.strftime("%a, %b-%d")
    format_date_11 = day_11.strftime("%a, %b-%d")
    format_date_12 = day_12.strftime("%a, %b-%d")
    format_date_13 = day_13.strftime("%a, %b-%d")
    format_date_14 = day_14.strftime("%a, %b-%d")
    format_date_15 = day_15.strftime("%a, %b-%d")
    format_date_16 = day_16.strftime("%a, %b-%d")
    format_date_17 = day_17.strftime("%a, %b-%d")
    format_date_18 = day_18.strftime("%a, %b-%d")
    format_date_19 = day_19.strftime("%a, %b-%d")
    format_date_20 = day_20.strftime("%a, %b-%d")
    format_date_21 = day_21.strftime("%a, %b-%d")
    format_date_22 = day_22.strftime("%a, %b-%d")
    format_date_23 = day_23.strftime("%a, %b-%d")
    format_date_24 = day_24.strftime("%a, %b-%d")
    format_date_25 = day_25.strftime("%a, %b-%d")
    format_date_26 = day_26.strftime("%a, %b-%d")
    format_date_27 = day_27.strftime("%a, %b-%d")
    format_date_28 = day_28.strftime("%a, %b-%d")
    format_date_29 = day_29.strftime("%a, %b-%d")
    format_date_30 = day_30.strftime("%a, %b-%d")

    data = {
        "city":city,
        'total_dry':total_dry,
        'total_rain':total_rain,
        "format_date_1":format_date_1,
        "temperature":city_weather['list'][0]['temp']['max'],
        "description":city_weather['list'][0]['weather'][0]['description'],
        "speed":city_weather['list'][0]['speed'],
        "cloud":city_weather['list'][0]['clouds'],

        "format_date_2":format_date_2,
        "temperature_2":city_weather['list'][1]['temp']['max'],
        "description_2":city_weather['list'][1]['weather'][0]['description'],
        "speed_2":city_weather['list'][1]['speed'],
        "cloud_2":city_weather['list'][1]['clouds'],

        "format_date_3":format_date_3,
        "temperature_3":city_weather['list'][2]['temp']['max'],
        "description_3":city_weather['list'][2]['weather'][0]['description'],
        "speed_3":city_weather['list'][2]['speed'],
        "cloud_3":city_weather['list'][2]['clouds'],

        "format_date_4":format_date_4,
        "temperature_4":city_weather['list'][3]['temp']['max'],
        "description_4":city_weather['list'][3]['weather'][0]['description'],
        "speed_4":city_weather['list'][3]['speed'],
        "cloud_4":city_weather['list'][3]['clouds'],

        "format_date_5":format_date_5,
        "temperature_5":city_weather['list'][4]['temp']['max'],
        "description_5":city_weather['list'][4]['weather'][0]['description'],
        "speed_5":city_weather['list'][4]['speed'],
        "cloud_5":city_weather['list'][4]['clouds'],

        "format_date_6":format_date_6,
        "temperature_6":city_weather['list'][5]['temp']['max'],
        "description_6":city_weather['list'][5]['weather'][0]['description'],
        "speed_6":city_weather['list'][5]['speed'],
        "cloud_6":city_weather['list'][5]['clouds'],

        "format_date_7":format_date_7,
        "temperature_7":city_weather['list'][6]['temp']['max'],
        "description_7":city_weather['list'][6]['weather'][0]['description'],
        "speed_7":city_weather['list'][6]['speed'],
        "cloud_7":city_weather['list'][6]['clouds'],

        "format_date_8":format_date_8,
        "temperature_8":city_weather['list'][7]['temp']['max'],
        "description_8":city_weather['list'][7]['weather'][0]['description'],
        "speed_8":city_weather['list'][7]['speed'],
        "cloud_8":city_weather['list'][7]['clouds'],

        "format_date_9":format_date_9,
        "temperature_9":city_weather['list'][8]['temp']['max'],
        "description_9":city_weather['list'][8]['weather'][0]['description'],
        "speed_9":city_weather['list'][8]['speed'],
        "cloud_9":city_weather['list'][8]['clouds'],

        "format_date_10":format_date_10,
        "temperature_10":city_weather['list'][9]['temp']['max'],
        "description_10":city_weather['list'][9]['weather'][0]['description'],
        "speed_10":city_weather['list'][9]['speed'],
        "cloud_10":city_weather['list'][9]['clouds'],

        "format_date_11":format_date_11,
        "temperature_11":city_weather['list'][10]['temp']['max'],
        "description_11":city_weather['list'][10]['weather'][0]['description'],
        "speed_11":city_weather['list'][10]['speed'],
        "cloud_11":city_weather['list'][10]['clouds'],

        "format_date_12":format_date_12,
        "temperature_12":city_weather['list'][11]['temp']['max'],
        "description_12":city_weather['list'][11]['weather'][0]['description'],
        "speed_12":city_weather['list'][11]['speed'],
        "cloud_12":city_weather['list'][11]['clouds'],

        "format_date_13":format_date_13,
        "temperature_13":city_weather['list'][12]['temp']['max'],
        "description_13":city_weather['list'][12]['weather'][0]['description'],
        "speed_13":city_weather['list'][12]['speed'],
        "cloud_13":city_weather['list'][12]['clouds'],

        "format_date_14":format_date_14,
        "temperature_14":city_weather['list'][13]['temp']['max'],
        "description_14":city_weather['list'][13]['weather'][0]['description'],
        "speed_14":city_weather['list'][13]['speed'],
        "cloud_14":city_weather['list'][13]['clouds'],
        
        "format_date_15":format_date_15,
        "temperature_15":city_weather['list'][14]['temp']['max'],
        "description_15":city_weather['list'][14]['weather'][0]['description'],
        "speed_15":city_weather['list'][14]['speed'],
        "cloud_15":city_weather['list'][14]['clouds'],

        "format_date_16":format_date_16,
        "temperature_16":city_weather['list'][15]['temp']['max'],
        "description_16":city_weather['list'][15]['weather'][0]['description'],
        "speed_16":city_weather['list'][15]['speed'],
        "cloud_16":city_weather['list'][15]['clouds'],

        "format_date_17":format_date_17,
        "temperature_17":city_weather['list'][16]['temp']['max'],
        "description_17":city_weather['list'][16]['weather'][0]['description'],
        "speed_17":city_weather['list'][16]['speed'],
        "cloud_17":city_weather['list'][16]['clouds'],

        "format_date_18":format_date_18,
        "temperature_18":city_weather['list'][17]['temp']['max'],
        "description_18":city_weather['list'][17]['weather'][0]['description'],
        "speed_18":city_weather['list'][17]['speed'],
        "cloud_18":city_weather['list'][17]['clouds'],

        "format_date_19":format_date_19,
        "temperature_19":city_weather['list'][18]['temp']['max'],
        "description_19":city_weather['list'][18]['weather'][0]['description'],
        "speed_19":city_weather['list'][18]['speed'],
        "cloud_19":city_weather['list'][18]['clouds'],

        "format_date_20":format_date_20,
        "temperature_20":city_weather['list'][19]['temp']['max'],
        "description_20":city_weather['list'][19]['weather'][0]['description'],
        "speed_20":city_weather['list'][19]['speed'],
        "cloud_20":city_weather['list'][19]['clouds'],

        "format_date_21":format_date_21,
        "temperature_21":city_weather['list'][20]['temp']['max'],
        "description_21":city_weather['list'][20]['weather'][0]['description'],
        "speed_21":city_weather['list'][20]['speed'],
        "cloud_21":city_weather['list'][20]['clouds'],

        "format_date_22":format_date_22,
        "temperature_22":city_weather['list'][21]['temp']['max'],
        "description_22":city_weather['list'][21]['weather'][0]['description'],
        "speed_22":city_weather['list'][21]['speed'],
        "cloud_22":city_weather['list'][21]['clouds'],

        "format_date_23":format_date_23,
        "temperature_23":city_weather['list'][22]['temp']['max'],
        "description_23":city_weather['list'][22]['weather'][0]['description'],
        "speed_23":city_weather['list'][22]['speed'],
        "cloud_23":city_weather['list'][22]['clouds'],

        "format_date_24":format_date_24,
        "temperature_24":city_weather['list'][23]['temp']['max'],
        "description_24":city_weather['list'][23]['weather'][0]['description'],
        "speed_24":city_weather['list'][23]['speed'],
        "cloud_24":city_weather['list'][23]['clouds'],

        "format_date_25":format_date_25,
        "temperature_25":city_weather['list'][24]['temp']['max'],
        "description_25":city_weather['list'][24]['weather'][0]['description'],
        "speed_25":city_weather['list'][24]['speed'],
        "cloud_25":city_weather['list'][24]['clouds'],

        "format_date_26":format_date_26,
        "temperature_26":city_weather['list'][25]['temp']['max'],
        "description_26":city_weather['list'][25]['weather'][0]['description'],
        "speed_26":city_weather['list'][25]['speed'],
        "cloud_26":city_weather['list'][25]['clouds'],

        "format_date_27":format_date_27,
        "temperature_27":city_weather['list'][26]['temp']['max'],
        "description_27":city_weather['list'][26]['weather'][0]['description'],
        "speed_27":city_weather['list'][26]['speed'],
        "cloud_27":city_weather['list'][26]['clouds'],

        "format_date_28":format_date_28,
        "temperature_28":city_weather['list'][27]['temp']['max'],
        "description_28":city_weather['list'][27]['weather'][0]['description'],
        "speed_28":city_weather['list'][27]['speed'],
        "cloud_28":city_weather['list'][27]['clouds'],

        "format_date_29":format_date_29,
        "temperature_29":city_weather['list'][28]['temp']['max'],
        "description_29":city_weather['list'][28]['weather'][0]['description'],
        "speed_29":city_weather['list'][28]['speed'],
        "cloud_29":city_weather['list'][28]['clouds'],

        "format_date_30":format_date_30,
        "temperature_30":city_weather['list'][29]['temp']['max'],
        "description_30":city_weather['list'][29]['weather'][0]['description'],
        "speed_30":city_weather['list'][29]['speed'],
        "cloud_30":city_weather['list'][29]['clouds'],
    }
    return render(request, 'store/services.html', data)

def advisories(request):
    return render(request, 'store/advisories.html')

def about(request):
    return render(request, 'store/about.html')

class CreateNews(View):
    def get(self, request):
        form = CreateNewsForm()
        return render(request, 'store/newsletter.html', {'form':form})

    def post(self, request):
        form = CreateNewsForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            background_image = form.cleaned_data['background_image']
            description = form.cleaned_data['description']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            reg = WhatsNew(title=title,background_image=background_image,description=description,content=content,category=category)
            reg.save()
        emails = NewsLetter.objects.all()
        subject = 'News Report'
        message = 'Greetings new headlines has been uploaded:\n' + form.cleaned_data['title'] + '\nNews Description: ' + form.cleaned_data['description'] + '\nNews Content: ' + form.cleaned_data['content'] + '\nNews Category: ' + form.cleaned_data['category']
        from_email = settings.DEFAULT_FROM_EMAIL
        to_list = emails
        send_mail(subject,message,from_email,to_list,fail_silently=True)
        return redirect('farms:home')
