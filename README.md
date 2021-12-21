# The Bunyols Library

# Tabla de contenidos

- [The Bunyols Library](#the-bunyols-library)
- [Tabla de contenidos](#tabla-de-contenidos)
- [Introducción](#introducción)
- [Historia](#historia)
- [Manual](#manual)
  - [Pre-requisitos](#pre-requisitos)
  - [Instalación](#instalación)
  - [Uso](#uso)
- [Metodología](#metodología)
- [Descripción Técnica](#descripción-técnica)
  - [Partes Interesadas y Requisitos Funcionales/No Funcionales](#partes-interesadas-y-requisitos-funcionalesno-funcionales)
  - [Diagrama de Casos de Uso](#diagrama-de-casos-de-uso)
  - [Arquitectura de la aplicación](#arquitectura-de-la-aplicación)
  - [Posibles Tecnologías](#posibles-tecnologías)
  - [Tecnologías y Herramientas Elegidas](#tecnologías-y-herramientas-elegidas)
- [Diseño](#diseño)
  - [Componentes](#componentes)
  - [Esquema BBDD](#esquema-bbdd)
  - [Ejemplo Real](#ejemplo-real)
  - [Pruebas](#pruebas)
  - [Coverage](#coverage)
  - [Pruebas Esquema BBDD](#pruebas-esquema-bbdd)
    - [Create](#create)
    - [Read](#read)
    - [Update](#update)
    - [Delete](#delete)
- [Comparación Temporal](#comparación-temporal)
  - [Clockify](#clockify)
  - [Justificación temporal](#justificación-temporal)
- [Conclusiones](#conclusiones)
  - [Posibles mejoras](#posibles-mejoras)
- [Dificultades](#dificultades)


# Introducción

**Bunyols Library** nace con la idea de presentar la información básica que cualquier libro debe de tener. Únicamente información representativa sobre el libro en sí de una forma muy fácil para el usuario.

En este proyecto usaremos [*MongoDB*](https://www.mongodb.com) como base de datos a través del servicio Mongo Atlas.
Para la lógica de la aplicación utilizaremos el lenguaje de programación [*Python*](https://www.python.org) (versión 3.9).

Para la conversión y creación del sitio web estático utilizaremos el SSG [*Hugo*](https://gohugo.io).
Y por último, emplearemos el servidor web [*Nginx*](https://www.nginx.com) para servir nuestro sitio web.

![simplediagram](images/technologies.png)

# Historia


Nuestro tan llamativo nombre surgió de un día ir caminando por Palma de Mallorca y una mujer en un puesto de estos aceitosos y sabrosas frutas fritas regalarme una bolsa de 1kg totalmente gratis. No era capaz de comerme tal semejante cantidad de [*fruta de sartén*](https://es.wikipedia.org/wiki/Bu%C3%B1uelo) y así fue como Samuele comió bunyols de camino al tren, dentro del tren y de desayuno al siguiente día. 

- *Con cariño, Eze*


# Manual

## Pre-requisitos
  - `Git` 
  - `Python3`
  - `pip3`
  - `fake-headers`
  - `bs4`
  - `lxml`
  - `pymongo`
  - `matplotlib` 

## Instalación

Se recomienda utilizar en 'virtualenv' para instalar todas las dependencias utilizadas por el programa. En [Windows](https://docs.python.org/es/3.8/library/venv.html) lo puedes instalar siguiendo su guía. En **Linux** ejecuta la siguiente instrucción.

```
$ sudo apt-get install python3-venv
```

Crea un directorio y sitúate dentro de él. Aquí dentro residirá todo el código de la aplicación.

```
$ mkdir ./bunyols-library
$ cd bunyols-library
```

Ya dentro del directorio clona el repositorio.

```
$ git clone git@github.com:stonarini/Bunyols.git
```
Se preparó un archivo 'setup' que activara el entorno virtual y descargara las dependencias necesarias por ti, ejecútalo.
```
$ ./setup.sh
```
Cuando se quiera entrar en el entorno virtual sin pasar por './setup.sh', ejecuta:
```
$ source venv/bin/activate
```
## Uso

**1. Formatea los elementos de la lista de la siguiente manera**.
```
("URL", ("Familia", ["Temática"]))
```
- 'URL' referencia a la página del libro en Amazon.
- 'Familia' referencia al conjunto de libros que pertenece el actual.
- 'Temática' referencia al tema del libro.

**Un ejemplo**
```
("https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882", ("Robert C Martin Series", ["IT"])
```
**2. Ejecuta 'bunyols.py' encima del archivo donde estén todos tus libros a scrapear definiendo la carpeta de 'Hugo' donde se creara el contenido**.

```
python3 bunyols.py [CARPETA]/
```
- 'CARPETA' hace referencia al directorio de 'Hugo'.

# Metodología

Para la parte lógica de la aplicación se ha usado una **metodología incremental** utilizando la filosofía de construir funcionalidades del programa, analizándolo y construyendo incrementos donde uno unido al otro tiene el fin de construir un uso funcional de la aplicación.

Para la parte de diseño web se ha empleado una **metodología prototipada** donde hemos diseñado diferentes prototipos de la página en diferentes formatos *(papel y [software gráfico](https://www.figma.com/)).* Una vez elegido el diseño, se recreó en HTML y CSS pasándolo por último a **hugo**.

Por último, hemos usado **Scrum** como marco de trabajo durante todo el proyecto.

# Descripción Técnica

## Partes Interesadas y Requisitos Funcionales/No Funcionales
Como parte interesada solo tenemos a lo que vienen siendo los empleados de la empresa que necesitan visualizar y gestionar los elementos de
la base de datos con nuestra aplicación. Podemos denominar esta parte interesada como *Empleado*.

**Requisitos Funcionales**
- RF_Empleado_01: Visualizar Elementos (R)

- RF_Empleado_02: Crear Elementos (C)

- RF_Empleado_03: Modificar Elementos (U)

- RF_Empleado_04: Borrar Elementos (D)

**Requisitos No Funcionales**
- RnF_01: Recolección Automática de Datos
- Al crear un nuevo elemento se usará un web scraper para recolectar automáticamente datos sobre ese elemento.
- RnF_02: Catalogación de Elementos
- A cada elemento se asignaran categorías que servirán para agruparlos
- RnF_03: Creación de Gráficos
- Se generaran automáticamente gráficos al renderizar la página

 ## Diagrama de Casos de Uso

 ![Use Cases](images/usecases.png)
 ## Arquitectura de la aplicación

 ![architecture](images/architecture.png)

- **Presentation layer**
  - **nginx/hugo** el primero es un software de servidor web open source utilizado para servir archivos HTML que construirá la segunda tecnología.

- **Service layer**
  - **bunyols.py** programa principal.

- **Business layer**
  - **get_page_source** encargado de hacer peticiones y general el contenido parseado de la página web solicitada.
  - **book_scraper** encargado de obtener los datos estáticos y dinámicos de la página web en la que se solicite la acción.
  - **markdownify** encargado de crear el *frontmatter* empleado por Hugo así de generar la estructura de los items devueltos al hacer peticiones a la base de datos.
  - **generate_graphs** encargado usando los datos dinámicos precios y reviews solicitados a la base de datos de realizar gráficos.

- **Data layer**
  - **database** todo lo relacionado a acciones hechas sobre y con la base de datos **MongoDB** con instrucciones de la librería 'pymongo.'

## Posibles Tecnologías

web-scraper | testing | generación de gráficos  
--- | --- | ---
[BS4](https://www.crummy.com/software/BeautifulSoup/) y [requests](https://docs.python-requests.org/en/master/index.html) | [pytest](https://docs.pytest.org/en/6.2.x/) | [ggplot](https://github.com/yhat/ggpy)  
[Selenium](https://www.selenium.dev/) | [Robot](https://robotframework.org/) | [matplotlib](https://matplotlib.org/)  

## Tecnologías y Herramientas Elegidas

- **[Python](https://docs.python.org/3/)**
  - **Beautiful Soup 4** es una biblioteca de Python para extraer datos de archivos HTML y XML dejando a elegir el parser para proporcional formas de navegación, búsqueda y modificación. [Referencia](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - **requests** es una librería HTTP para Python usada para efectuar peticiones HTTP y hacerlas más amigables.
  [Referencia](https://docs.python-requests.org/en/latest/)
  - **fake-headers** utilizada para generar una cabecera aleatoria para enmascarar diferentes peticiones y que no vengan bloqueadas.
  [Referencia](https://pypi.org/project/fake-headers/)
  - **matplotlib** es una librería para crear animaciones estáticas y visualizaciones interactivas en Python. [Referencia](https://matplotlib.org/stable/)
  - **pytest** es un framework utilizado para escribir casos test y poner aprueba aplicaciones y librerías. [Referencia](https://docs.pytest.org/en/6.2.x/)
  - **coverage** junto a *pytest* es una herramienta para medir el código cubierto de un programa. Monitoriza el programa informando de que cantidad de código ha sido ejecutada. [Referencia](https://coverage.readthedocs.io/en/6.2/)
- **[MongoDB](https://docs.mongodb.com/)**
  - **pymongo** es una librería que contiene herramientas para trabajar con [MongoDB](http://www.mongodb.org/). [Referencia](https://pymongo.readthedocs.io/en/stable/)
- **[Hugo](https://gohugo.io/documentation/)**
- *Framework* empleado para la creación de sitios webs estáticos.
- **HTML5 y CSS**
- Estilización de la parte web junto a hugo.
- **[Git](https://git-scm.com/docs)**
- Realización de cambios y subida de versiones modificadas independientes, no sobrescribiendo en el archivo original.
- **Markdown**
- Lenguaje de marcado ligero utilizado en **gohugo**

# Diseño

![components](/images/components.png)

## Componentes

- **`utilities`** package que alberga *herramientas* que devuelven una información utilizada por otros módulos o realizan una tarea en específico.

- **`book_scraper`** package que alberga todo lo relacionado con el web scraper en sí, dentro de este existen 2 packages más 'get_book_dynamic_data' y 'get_book_static_data' que scrapean la información establecida dentro de sus módulos.

- **`get_page_source`** package que alberga aquellos métodos usados para ejecutar peticiones a una página y devolver el contenido que después será scrapeado por 'book_scraper'.

- **`markdownify`** package que alberga todo lo empleado para generar estructuras markdown así como lo necesario para 'Hugo'.

- **`generate_graphs`** package que alberga aquellos métodos empleados para generar gráficos mediante los datos 'precios' y 'reyes' contenidos en la base de datos.

- **`database`** package donde se sitúa todo lo relacionado con el manejo de la base de datos, en resumen, sus métodos CRUD.

## Esquema BBDD

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
## Ejemplo Real
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

## Pruebas

Organizamos nuestras pruebas de manera que cada unidad hubiese mínimo 2 test:

- Un test que simulase una ejecución correcta.
- Un test que simulase el peor caso posible.

Con estos test ya se podía iniciar a codificar. Después, si había más casos a tener en cuenta se iba añadiendo durante el desarrollo,

Para más concretización sobre los test, véase el file [pytest.ini](https://github.com/stonarini/Bunyols/blob/develop/pytest.ini) o la carpeta de test en la rama [develop](https://github.com/stonarini/Bunyols/tree/develop/test).

Lo que si merece la pena mencionar son los test del módulo *database*, que están diseñados de manera que un elemento se cree, actualice y luego se borre, sin dejar elementos no queridos en la base de datos.

## Coverage

![coverage](images/coverage.png)

Podemos observar como nuestros test tienen una cobertura del 91% de las lineas de código.
Con unos pocos test deberíamos llegar al 100% sin problemas.

## Pruebas Esquema BBDD


```
En pytest, cuando ejecutas los test, un . verde significa que el test ha pasado y una F roja
significa que ha fallado. Todo el output del programa generado por un test vendrá antes del .
o F que represente ese test.

i.e:
test/test_prueba.py ..
Este test ha fallado
F Este test NO ha fallado
.

En este ejemplo podemos ver que hay 4 test.
Los dos primeros han pasado sin ningún output, mientras que el tercero ha fallado y ha tenido
output.
El cuarto no ha fallado y ha tenido también un output descriptivo.
```

### Create
Como podemos observar en los [test de create](https://github.com/stonarini/Bunyols/blob/develop/test/database/test_1_create.py),
seguimos nuestro diseño de un test que pase y otro que no, así que en estos test intentamos meter un documento que no sigue nuestro esquema y otro que si:
![create](images/create.png)

### Read
En los [test de find](https://github.com/stonarini/Bunyols/blob/develop/test/database/test_2_find.py) test intentamos leer dos
elementos, uno que no existe y otro que si. Los dos test pasan sin problema:
![find](images/find.png)

### Update
En el caso de los [test de update](https://github.com/stonarini/Bunyols/blob/develop/test/database/test_3_update.py) tenemos tres test, uno que intenta añadir un parámetro *test* que no está presente en el esquema, otro que intenta añadir el parámetro opcional *family* que sí que está presente en el esquema, pero no es obligatorio, y por último este test simula una actualización de las reviews y un cambio de precio.
Como podemos observar el primer test da error y nos dice si estamos seguros de que nuestro documento sigue el esquema, mientras que los otros dos test pasan sin problemas.
![update](images/update.png)

### Delete
Como último, están los [tests de delete](https://github.com/stonarini/Bunyols/blob/develop/test/database/test_4_delete.py). El primer test borra el elemento creado en los *tests de create*, mientras que el segundo test intenta borrar un elemento que no existe.
Aquí podemos observar como el primer test pasa sin problema, mientras que el segundo nos avisa de que el elemento no existe:
![delete](images/delete.png)

# Comparación Temporal

## Clockify
Para tener bajo control el tiempo utilizado y para poder comparar nuestras estimaciones hemos usado la herramienta Clockify con las siguientes etiquetas:

- **Scraper:** Para los módulos 'book_scraper' y 'get_page_source'.
- **Database:** Para el módulo 'database' y la creación del esquema y validación de la base de datos
- **Web Design:** Para el prototipado de la página web (tanto diseño como implementación HTML y CSS)
- **Hugo:** Para la configuración de 'Hugo' y para la implementación del prototipo realizado en 'Web Design'
- **Markdown:** Para los módulos 'markdownify' y 'generate_graphs'
- **Docs:** Para el tiempo usado para escribir esta documentación
- **Configuración:** Para configuración de git y para la configuración de herramientas y scripts (git-hooks, tox, pytest, etc...)
  
![clockify](images/clockify.png)

Nuestra predicción temporal fue 34 horas, aunque no contamos con cosas como la configuración, documentación y refactorización:

![time](images/time.png)

```yaml
Predicción de Tiempo: 34h

Tiempo Real: 56h y 40min
```

## Justificación temporal

Teniendo el gráfico presente la tarea en la que más hemos invertido tiempo ha sido en la creación de nuestro propio scraper, teníamos la opción de usar el scraper ya hecho por nuestros tutores de segundo, pero prescindimos de este al no ser posible adaptarlo del todo a los requisitos que queríamos.

Invertimos así el tiempo teniendo en mente que la lógica detrás de 'markdownify' no nos iba a ocupar el tiempo que sabíamos la creación del scraper desde cero sí.

# Conclusiones

## Posibles mejoras

- Estamos trabajando en la implementación de [Typer](https://typer.tiangolo.com/) para poder realizar una inserción nueva de libros desde la linea de comandos.
- Estamos trabajando en la implementación de [Typer](https://typer.tiangolo.com/) para poder manejar funciones relacionadas al modulo de base de datos desde la linea de comandos.

# Dificultades

No hemos experimentado dificultades notorias mas haya que desarrollar el modulo `book-scraper` desde cero, pues el proyecto no consistía directamente en esta funcionalidad pero se necesitaba si queríamos crear el proyecto a nuestros gustos personales.

