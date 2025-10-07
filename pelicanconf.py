AUTHOR = "Kieran Choi-Slattery"
SITENAME = "Kieran Choi-Slattery"
SITEURL = ""

BOOTSTRAP_THEME = "yeti"
# BOOTSTRAP_THEME = "readable"
# BOOTSTRAP_THEME = "paper"

THEME = "./theme"

STATIC_PATHS = ["images", "scripts", "ViewerJS", "documents"]
EXTRA_PATH_METADATA = {"images/favicon.ico": {"path": "favicon.ico"}}

# These next few lines are just to satisfy the theme
JINJA_ENVIRONMENT = {"extensions": ["jinja2.ext.i18n"]}
PLUGIN_PATHS = ["./plugins"]
PLUGINS = ["i18n_subsites", "render_math"]

ARTICLE_EXCLUDES = ["ViewerJS"]

PATH = "content"

ABOUT_ME = "Hi, I'm Kieran! I’m a Ph.D. student in Electrical and Computer Engineering at Georgia Tech. My research is in the Aerospace Engineering department, where I did my undergrad, working on instrumentation for solar system science and astrobiology. Previously, I've worked on radar algorithms for glaciology and rocket avionics for the Georgia Tech Experimental Rocketry team, where I was the Avionics Lead."
AVATAR = "images/square-headshot.jpg"

TIMEZONE = "EST"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Planetary Exploration Lab", "https://pxl.earth/"),
    ("Georgia Tech Experimental Rocketry", "https://www.ramblinrocketclub.org/gtxr"),
    ("Personal PyPI", "https://kchoislattery.github.io/PyPI/"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/KChoiSlattery"),
    ("LinkedIn", "https://www.linkedin.com/in/kchoislattery/"),
)

DEFAULT_PAGINATION = 10

DELETE_OUTPUT_DIRECTORY = True

PYGMENTS_STYLE = "default"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
