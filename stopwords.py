# importar la libreria nltk
import nltk

#desde nltk descargar el paquete de stopwords
from nltk.corpus import stopwords
nltk.download('stopwords')

lista_stopwords = stopwords.words('spanish')

# imprimir las stopwords
print(lista_stopwords)
