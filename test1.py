from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

custom_categories = ['entretenimiento', 'moda', 'musica']

custom_texts = [
    "Inception es una película dirigida por Christopher Nolan que explora los límites de la realidad y los sueños. La trama sigue a un ladrón de sueños experto que es contratado para implantar una idea en la mente de una persona.",
    "Parasite es una película surcoreana dirigida por Bong Joon-ho que ganó el Premio de la Academia a la Mejor Película en 2020. La historia gira en torno a una familia pobre que se infiltra en una familia adinerada, desatando una serie de eventos inesperados.",
    "Breaking Bad es una serie de televisión estadounidense creada por Vince Gilligan. Sigue la historia de Walter White, un profesor de química convertido en fabricante de metanfetamina después de ser diagnosticado con cáncer.",
    "Stranger Things es una serie de televisión de ciencia ficción y terror creada por los hermanos Duffer. Ambientada en los años 80 en un pequeño pueblo, la trama sigue a un grupo de niños que se encuentran con fenómenos sobrenaturales y un mundo paralelo."
]

custom_labels = [0, 1, 2, 3] 

model = make_pipeline(TfidfVectorizer(), MultinomialNB())

model.fit(custom_texts, custom_labels)

# Texto para clasificar
texto_para_clasificar = [
    "Ana: ¡Hola Javier! ¿Cómo estás?",
    "Javier: ¡Hola Ana! Estoy muy bien, gracias. ¿Y tú?",
    "Ana: También estoy bien, gracias. ¿Has visto alguna película interesante últimamente?",
    "Javier: Sí, hace poco vi 'Inception' de Christopher Nolan. ¡Fue alucinante! La trama, los efectos visuales, todo fue increíble.",
    "Ana: ¡Oh, sí! 'Inception' es una de mis películas favoritas. La forma en que exploran los sueños y la realidad es fascinante. ¿Qué otra película te ha impresionado últimamente?",
    "Javier: Bueno, también vi 'Parasite' de Bong Joon-ho. Ganó el Oscar a la Mejor Película y realmente mereció el reconocimiento. La historia es tan única y llena de giros inesperados.",
    "Ana: Sí, 'Parasite' fue una obra maestra. La manera en que aborda temas sociales y económicos de una manera tan ingeniosa es brillante. ¿Has estado viendo alguna serie últimamente?",
    "Javier: Sí, estuve enganchado a 'Breaking Bad'. Sí, sé que es antigua, pero finalmente decidí verla y comprendí por qué es tan aclamada. La evolución del personaje de Walter White es increíble.",
    "Ana: ¡Sí! 'Breaking Bad' es una serie icónica. La complejidad de los personajes y la tensión constante mantienen al espectador atrapado desde el principio hasta el final. ¿Tienes alguna recomendación para mí?",
    "Javier: Definitivamente deberías ver 'Stranger Things' si aún no lo has hecho. Es una mezcla perfecta de nostalgia de los años 80 y elementos sobrenaturales. La trama te atrapa desde el primer episodio.",
    "Ana: He oído hablar mucho sobre 'Stranger Things'. ¡Definitivamente la agregaré a mi lista! Bueno, Javier, ha sido genial hablar contigo sobre películas y series. ¡Hagamos planes para ver una película juntos pronto!",
    "Javier: ¡Por supuesto, Ana! Será divertido. ¡Hasta luego!",
    "Ana: ¡Hasta luego, Javier!"
]

prediccion = model.predict(texto_para_clasificar)

print("El texto fue clasificado en la categoría:", custom_categories[prediccion[0]])
