# 1. Importeer de weaviate module
import weaviate

# 2. Maak een Weaviate client die verbindt met poort 8080
client = weaviate.Client(
    url="http://localhost:8080"
)

# 3. We willen op twee keywords analyseren: positief en negatief. Maak een lijst met deze twee keywords
keywords = ['positief', 'negatief']

# 4. Maak een dictionary aan waarin we de afstanden tussen de keywords en de comments gaan opslaan en
#    een dictionary waarin we de categorie van de comment gaan opslaan
distances_all = {}
categories = {}

# 5. Voor elk keyword in de lijst met keywords
for keyword in keywords:  
    #6. vraag van alle comments op hoever deze bij het keyword liggen
    distances_keyword = (
        client.query
        .get("Comment", ["text"])
        .with_additional("distance")
        .with_near_text({
            "concepts": [keyword],
            "distance": 1.0,
        })
        .do()
    )
    
    # 7. Voor elke comment in de resultaten: sla de afstand op in de dictionary
    for distance in distances_keyword['data']['Get']['Comment']:
        if not distance['text'] in distances_all:
            distances_all[distance['text']] = {}

        distances_all[distance['text']][keyword] = distance['_additional']['distance']
            

# 8. Voor elk keyword in de lijst met keywords: normaliseer de afstanden
for distances_keyword in distances_all:
    for keyword in distances_all[distances_keyword]:
        distances_all[distances_keyword][keyword] = 1 - distances_all[distances_keyword][keyword]
    total = sum([distances_all[distances_keyword][keyword] for keyword in distances_all[distances_keyword]])
    for keyword in distances_all[distances_keyword]:
        distances_all[distances_keyword][keyword] = distances_all[distances_keyword][keyword] / total

# 9. Voor elk keyword in de lijst met keywords: bepaal de categorie van de comment
for keyword in keywords:
    categories[keyword]= []
    for distances_keyword in distances_all:
        if distances_all[distances_keyword][keyword] == max(list(distances_all[distances_keyword].values())):
            categories[keyword].append(distances_keyword)

# 10. Print de categorieën
print(categories)