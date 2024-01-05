# 1. Importeer de weaviate module
import weaviate

# 2. Maak een Weaviate client die verbindt met poort 8080
client = weaviate.Client(
    url="http://localhost:8080"
)

# 3. Maak data entries van het type 'Comment'
client.data_object.create(
    data_object={
        'text': 'Ik vond deze film helemaal niet leuk',
    },
    class_name='Comment'
)
 
client.data_object.create(
    data_object={
        'text': 'Wat een geweldige film!',
    },
    class_name='Comment'
)
 
client.data_object.create(
    data_object={
        'text': 'Het acteerwerk was niet erg overtuigend',
    },
    class_name='Comment'
)
 
client.data_object.create(
    data_object={
        'text': 'onverwacht einde zeg',
    },
    class_name='Comment'
)