from datetime import date
import os
import django

# Configurar el entorno de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portafolio.settings')
django.setup()

from blog.models import Blog

# Crear publicaciones para el blog
def create_blog_posts():
    posts = [
        {
            "titulo": "Introducción a Python para Principiantes",
            "contenido": "Python es un lenguaje de programación popular debido a su sintaxis simple y su versatilidad. En este artículo, exploraremos los conceptos básicos de Python, como variables, tipos de datos y estructuras de control. Aprenderás cómo escribir tu primer script en Python y comprenderás por qué es una de las mejores opciones para principiantes. Además, veremos algunos ejemplos prácticos que te ayudarán a afianzar tus conocimientos.",
            "fecha_de_publicacion": date(2025, 1, 15),
            "autor": "Diego Gonzalez",
        },
        {
            "titulo": "Análisis de Datos con Pandas",
            "contenido": "Pandas es una biblioteca esencial para el análisis de datos en Python. Proporciona estructuras de datos flexibles como DataFrames y Series, que permiten manipular grandes volúmenes de datos de manera eficiente. En este artículo, veremos cómo cargar conjuntos de datos desde archivos CSV y Excel, aplicar filtros, transformar información y generar estadísticas clave. También exploraremos cómo Pandas se integra con otras herramientas como NumPy y Matplotlib.",
            "fecha_de_publicacion": date(2025, 1, 16),
            "autor": "Diego Gonzalez",
        },
        {
            "titulo": "JavaScript: Funciones Asíncronas Explicadas",
            "contenido": "JavaScript es un lenguaje ampliamente utilizado en el desarrollo web, y su capacidad para manejar operaciones asíncronas es fundamental para mejorar el rendimiento de las aplicaciones. En este artículo, exploraremos cómo funcionan las promesas, async/await y el event loop. A través de ejemplos prácticos, aprenderás cómo manejar peticiones a APIs, trabajar con temporizadores y evitar bloqueos en la ejecución del código.",
            "fecha_de_publicacion": date(2025, 1, 17),
            "autor": "Diego Gonzalez",
        },
        {
            "titulo": "Diseño de Bases de Datos Relacionales",
            "contenido": "Un buen diseño de base de datos es clave para el éxito de cualquier aplicación. En este artículo, exploraremos los principios fundamentales del diseño de bases de datos relacionales, incluyendo la normalización, las claves primarias y foráneas, y las relaciones entre tablas. También discutiremos las mejores prácticas para modelar datos de manera eficiente y cómo evitar problemas comunes, como la redundancia y la inconsistencia de datos.",
            "fecha_de_publicacion": date(2025, 1, 18),
            "autor": "Diego Gonzalez",
        },
        {
            "titulo": "Tendencias Tecnológicas en 2025",
            "contenido": "El mundo de la tecnología evoluciona rápidamente, y 2025 no será la excepción. En este artículo, analizaremos algunas de las tendencias más prometedoras, como la inteligencia artificial, la computación cuántica, el desarrollo de software sin servidor (serverless) y el avance de la realidad aumentada. Exploraremos cómo estas tecnologías están cambiando la forma en que trabajamos y vivimos, y qué impacto tendrán en la industria del software en los próximos años.",
            "fecha_de_publicacion": date(2025, 1, 19),
            "autor": "Diego Gonzalez",
        },
    ]

    for post in posts:
        Blog.objects.create(
            titulo=post["titulo"],
            contenido=post["contenido"],
            fecha_de_publicacion=post["fecha_de_publicacion"],
            autor=post["autor"],
        )

    print("¡Publicaciones creadas exitosamente!")

if __name__ == "__main__":
    create_blog_posts()