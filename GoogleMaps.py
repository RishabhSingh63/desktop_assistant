import webbrowser

def get_directions(source, destination):
    url = f"https://www.google.com/maps/dir/{source}/{destination}"
    webbrowser.open(url)

def find_nearby_places(place):
    url = f"https://www.google.com/maps/search/{place}/"
    webbrowser.open(url)

def search_location(location):
    url = f"https://www.google.com/maps/search/?api=1&query={location}"
    webbrowser.open(url)

def get_current_location():
    url = "https://www.google.com/maps"
    webbrowser.open(url)

def get_distance(source, destination):
    url = f"https://www.google.com/maps/dir/{source}/{destination}"
    webbrowser.open(url)

def get_travel_duration(source, destination):
    url = f"https://www.google.com/maps/dir/{source}/{destination}"
    webbrowser.open(url)