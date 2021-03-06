![alt text](https://raw.githubusercontent.com/WADPlaceholdr/Placeholdr/master/static/images/logonobg.png)


## Description
placeholdr is a Django web application with the objective of allowing people to browse through places of interest and create trips based on those places, with a user community that provides ratings, comments, pictures.

## Demo
a live demo is available at https://placeholdr.pythonanywhere.com/

## External sources
* django
* Google Maps API
* Bootstrap
* django-bootstrap4
* animate.css
* wow.js
* Search code snippet by julienphalip.com
* django-csp
* django-mathfilters
* django-referrer-policy
* django-geoposition
* Pillow
* pytz
* selenium

## Requirements
(see [requirements.txt](https://github.com/WADPlaceholdr/Placeholdr/blob/master/requirements.txt))
* Python 3.6.x
* pip3
* Django==1.11.7
* django-bootstrap4==0.0.6
* django-csp==3.3
* django-mathfilters==0.4.0
* django-referrer-policy==1.0
* django-geoposition==0.3.1
* Pillow==5.0.0
* pytz==2018.3
* selenium==3.11.0

## Installation
clone this repository
```
git clone https://github.com/WADPlaceholdr/Placeholdr.git
```

install requirements
```
cd Placeholdr
pip install –r requirements.txt --yes
```

**optional** create deployment_variables.py
(don't use for development/test environment, deployment only)
(default conf file uses HTTPS with HTST and all security headers strictly configured
```
mv placeholdr/deployment_variables.py.conf placeholdr/deployment_variables.py
```


create database
```
python manage.py migrate
```

**optional** populate placeholdr with sample data
```
python population_script.py
```

SUMMARY

```
git clone https://github.com/WADPlaceholdr/Placeholdr.git
cd Placeholdr
pip install –r requirements.txt --yes
$ mv placeholdr/deployment_variables.py.conf placeholdr/deployment_variables.py
python manage.py migrate
python population_script.py
```


## Support
for support please submit an issue on [GitHub](https://github.com/WADPlaceholdr/Placeholdr/issues)

## Contact
wadplaceholdr@gmail.com
