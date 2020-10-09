import confuse

configuration = confuse.Configuration('AILOL_BACKEND',__name__)


class Config:
    # Flask settings
    SECRET_KEY = configuration['SECRET_KEY'].get()
    FLASK_APP = configuration['FLASK_APP'].get()
    FLASK_ENV = configuration['FLASK_ENV'].get()
    # ai api connections
    AI_IP = configuration['ai']['ip'].get()
    AI_PORT = configuration['ai']['port'].get()
    # scraper api connections
    SCRAPER_IP = configuration['scraper']['ip'].get()
    SCRAPER_PORT = configuration['scraper']['port'].get()
    # frontend api connections
    FRONTEND_IP = configuration['frontend']['ip'].get()
    FRONTEND_PORT = configuration['frontend']['port'].get()