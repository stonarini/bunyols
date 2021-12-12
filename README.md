# Bunyols

# Introduccion
Este prouesasdjflkjsldkjfldsj

# Metodologia
Para la mayor parte del proyecto hemos utilizado una metodologia incremental, donde decidiamos el incremento y una vez acabado, analizavamos resultados y creavamos un nuevo incremento.

Decidimos utilizar otra metodologia para el desarrollo del estilo de la pagina. Aqui hemos seguido un modelo de prototipado, donde hemos disenado diferentes prototipos de la pagina en diferentes formas (papel, software grafico, etc...). Una vez que nos gustaba el diseno, lo hemos recreado con HTML y CSS planos, y como ultimo paso lo hemos implementado en HUGO.

# Analisis


## Tecnologias Eligidas

Book_Scraper:
- **Beautiful Soup 4**: utilizada para procesar paginas html y sacar contenido de ellas

Get_Page_Source:
- **requests**: utilizada para hacer peticiones a determinadas paginas
- **fake-headers**: usada para generar una cabecera aleatoria para masquerar las diferentes peticiones y que no vengan bloqueadas

Database:
- **pymongo**: usada para establecer la coneccion con la base de datos
  
Generate_Graphs:
- **matplotlib**: utilizada para generar graficos de diferentes valores de los libros 

Testing:
- **pytest**: usada para ejecutar los casos tests de todos los componentes
- **coverage**: usada en conjunto con pytest para verificar el porcentaje de lineas ejecutadas


# Diseno
## Mapa Conceptual

## Esquema de la Base de Datos
### Esquema MongoDB
```json
{
    "title": {
        "type": "string",
        "description": "Book's Title"
    },
    "author": {
        "type": "array",
        "description": "List of authors of the book"
    },
    "publisher": {
        "type": "string",
        "description": "Entity that published the book"
    },
    "ISBN_13": {
        "type": "string",
        "description": "Unique book's identifier"
    },
    "publish_date": {
        "type": "string",
        "description": "Day when the book was published"
    },
    "price": {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "value": {
                    "type": "string",
                    "description": "Current price of the book"
                },
                "date": {
                    "type": "string",
                    "description": "The date of when the price was retrived"
                }
            }
        },
        "description": "Array of object contaning the book price and the day the price was retrived"
    },
    "reviews": {
        "type": "object",
        "properties": {
            "total_reviews": {
                "type": "number",
                "description": "Total number of reviews of the book"
            },
            "5": {
                "type": "number",
                "description": "Total number of 5 star reviews"
            },
            "4": {
                "type": "number",
                "description": "Total number of 4 star reviews"
            },
            "3": {
                "type": "number",
                "description": "Total number of 3 star reviews"
            },
            "2": {
                "type": "number",
                "description": "Total number of 2 star reviews"
            },
            "1": {
                "type": "number",
                "description": "Total number of 1 star reviews"
            }
        }
    },
    "categories": {
        "type": "array",
        "items": {
            "type": "string",
            "description": "Category name"
        },
        "description": "Array of categories of the book"
    },
    "family": {
        "type": "string",
        "description": "Saga/Collection of which the book is part of"
    }
}
```

### Ejemplo Real
```json
{
    "title": "Code Complete",
    "author": [
        "Steve McConnell"
    ],
    "publisher": "Microsoft Press",
    "ISBN_13": "9780735619678",
    "publish_date": "June 2004",
    "price": [
        {"date": "2021-12-06 18:13:33", "value": "$16.43"},
        {"date": "2021-12-10 00:24:26", "value": "$29.99"},
    ],
    "reviews": {
        "total_reviews": 896, 
        "5": 699, 
        "4": 117, 
        "3": 45, 
        "2": 17, 
        "1": 18
    },
    "categories": ["IT"],
}
```

## Pruebas a Realizar

# Implementacion

# Pruebas

# Comparacion Temporal

## Clockify
Para tener bajo control el tiempo utilizado y para poder comparar nuestras estimaciones hemos usado la herramienta Clockify con las siguentes etiquetas:
- Scraper: Para los modulos *book_scraper* y *get_page_source*
- Database: Para el modulo *database* y la creacion del esquema y validacion de la base de datos
- Web Design: Para el prototipado de la pagina web (tanto diseno como implementacion HTML)
- Hugo: Para la configuracion de *Hugo* y para la implementacion del prototipo
- Markdown: Para los modulos *markdownify* y *generate_graphs*
- Docs: Para el tiempo usado para escribir esta documentacion
- Cofiguracion: Para la configuracion de git y para la configuracion de herramientas y scripts (git-hooks, tox, pytest, etc...)
### 

# Dificultades