# 1.Laad de pipeline in vanuit de transformers library
from transformers import pipeline
# 2. Maak een pipeline aan voor sentimentanalyse met een nederlands sentimentanalysemodel
sentiment_pipeline = pipeline("sentiment-analysis", "DTAI-KULeuven/robbert-v2-dutch-sentiment")
# 3. Creëer de data om te analyseren
data = [
    'Ik vond deze film helemaal niet leuk',
    'Wat een geweldige film!',
    'Het acteerwerk was niet erg overtuigend',
    'onverwacht einde zeg'
]
# 4. Voer een analyse uit
resultaat = sentiment_pipeline(data)
# 5. Print het resultaat
print(resultaat)