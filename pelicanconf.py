AUTHOR = 'Kieran Choi-Slattery'
SITENAME = "Kieran Choi-Slattery"
SITEURL = ""

THEME = './pelican-themes/pelican-bootstrap3'

# These next few lines are just to satisfy the theme
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['i18n_subsites']

PATH = "content"

ABOUT_ME = "Hi, I'm Kieran!"
AVATAR = "images/square-headshot.jpg"

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PADDED_SINGLE_COLUMN_STYLE = True

# Blogroll
LINKS = (
    ("Planetary Exploration Lab", "https://pxl.earth/"),
    ("Georgia Tech Experimental Rocketry", "https://www.ramblinrocketclub.org/gtxr"),
)

# Social widget
SOCIAL = (
    # ("Github", "https://github.com/KChoiSlattery"),
    ("LinkedIn", "https://www.linkedin.com/in/kchoislattery/"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
