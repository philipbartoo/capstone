from django.core.management.base import BaseCommand, CommandError
from ProjectManagementApp.models import Disasters
#import requests
import csv
from csv import DictReader
#import pyperclip

class Command(BaseCommand):
    help = 'Imports Projects csv'

    def handle(self, *args, **kwargs):

        inputfile=csv.reader(open('testprojects.csv','r'))
        outputfile=open('cleanprojects.csv','w')

        for row in inputfile:
            row[7].replace('; \n','')
            outputfile.write()
        
        ''' with open('testprojects.csv', encoding='utf-8') as csv_file:
            csv_reader=csv.DictReader(csv_file, delimiter=",")
            for row in csv_reader:
                disasters=Disasters()
                disasters.disaster_number=row["Disaster Number"]
                disasters.state=row["State"]
                print(row)'''
                
            
            #disaster = Disasters.objects.create(
            #    disaster_number=disaster_number,
            #    state=state
            #)
        
        
        '''for row in DictReader(open('test.csv',delimiter=',')):
            disasters = Disasters()
            disasters.disaster_number = row['disaster_number']
            disasters.state = row['state']
            disasters.save()'''
           


        
        '''file = open("R9 Disaster Summary x3A 29151127.csv")
        disaster = csv.load(file)
        data=disaster['pokemon']
        
        for row in data:
            number=int(row['number'])
            name=row['name']
            height=int(row['height'])
            weight=int(row['weight'])
            image_front=row['image_front']
            image_back=row['image_back']
            type=row['types']
       
            #print(types)

            

            pokemon = Pokemon.objects.create(
                number=number,
                name=str.title(name),
                height=height,
                weight=weight,
                image_front=image_front,
                image_back=image_back
            )
            for type in type:
                type, created = PokemonType.objects.get_or_create(name=type)
                pokemon.types.add(type)'''
            #print('success??')
        
        
        #for row in pokemon:
            #pokemon = pokemon['pokemon']
            #name = row["Name"]
            #pokemon.name = row['Name']
            #pokemon.height = int(row['height'])
            #pokemon.weight = int(row['weight'])
            #pokemon.image_front = row['image_front']
            #pokemon.image_back = row['image_back']
            #pokemon.type = [type['type']['name'] for type in pokemon['types']]

        #file.close()
