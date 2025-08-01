import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string

# Descargar recursos de NLTK (solo una vez)
nltk.download('punkt')
nltk.download('stopwords')

# Simulación de mensajes de alerta de servidores
alertas = [
    "Error: Connection timeout on server 01.",
    "Warning: High CPU usage on server 02.",
    "Critical: Disk space full on server 03.",
    "Error: Database connection failed.",
    "Alert: Memory leak detected in process.",
    "Warning: Unusual traffic detected.",
    "Error: Authentication failed.",
    "Critical: Service not responding.",
    "Notice: Scheduled maintenance completed."
]

# Unir todos los textos en un solo corpus
texto = " ".join(alertas).lower()

# Tokenización y limpieza
tokens = word_tokenize(texto)
tokens_limpios = [word for word in tokens if word.isalpha()]  # solo palabras (sin puntuación)

# Eliminar stopwords en inglés
stop_words = set(stopwords.words('english'))
tokens_filtrados = [word for word in tokens_limpios if word not in stop_words]

# Contar palabras frecuentes
frecuencias = Counter(tokens_filtrados)

# Mostrar las 10 palabras más comunes
print("Palabras más frecuentes:")
for palabra, freq in frecuencias.most_common(10):
    print(f"{palabra}: {freq}")

# Visualización
plt.figure(figsize=(10,5))
plt.bar(*zip(*frecuencias.most_common(10)), color='skyblue')
plt.title('Palabras más frecuentes en mensajes de alerta')
plt.xlabel('Palabras')
plt.ylabel('Frecuencia')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
