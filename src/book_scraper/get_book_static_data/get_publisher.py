def get_publisher(data):
    try:
        publisher = data["publishers"][0]
    except KeyError:
        publisher = "Na"
    finally:
        return publisher
