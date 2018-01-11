
def get_urls():

    from .urls import urlpatterns

    return urlpatterns

def get_js():

    return ["djinn_events.js"]

def get_css():

    return ["djinn_events.css"]
