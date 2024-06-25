class Config(object):
    LOGGER = True
    API_ID = 29920508
    API_HASH = "10676e77085a5214bcea5ca17cda5778"
    TOKEN = ""  
    OWNER_ID=None
    
    SUPPORT_CHAT = "INCREDIBLExGENOCIDE" 
    START_IMG = "https://telegra.ph/file/3759a248d0f805fa9f0ef.jpg"
    EVENT_LOGS = ()
    MONGO_DB_URI= ""
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
