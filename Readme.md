Set environment source to use django specific features locally
> source venv/Scripts/activate

Create a new app. I.e. seperate logical part for project
> python manage.py startapp [[ new_app_name ]]

Create migrations based on models for specific app 
> python manage.py makemigrations [[ app_name ]]



>TODO:

Coordinates:
>CRUD to create a seperate locations
>>Create form to add new locations
>>Create template to display current locations and filter them based on their values
>>Add signal for location just to test out how it works
>>Make proximity calculations, distance calculations based on existing locations. How far is x from y.

>Make migration from 

Rest API

>restAPI should return any coordinate API information available in the DB

>Given two points calculate the distance between them and compare their associated values
