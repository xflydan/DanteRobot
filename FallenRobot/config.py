class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 27192333
    API_HASH = "f5e17d3232f7e1ac576befaf319665b8"

    CASH_API_KEY = "0XYNIGBARN825UR4"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = "postgres://mtksghre:YX8h6Dk6sduf9lOj4bbvBSskxy-_AKXk@flora.db.elephantsql.com/mtksghre"  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1001919016639)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://idmn1:idmn1@cluster0.vuda5r7.mongodb.net/?retryWrites=true&w=majority"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://telegra.ph/file/0503186cae8a355ef894b.jpg"

    SUPPORT_CHAT = "dansupport"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6675348472:AAHXq5rb_6HOSt75dLdZS8tklRXkdVuKiLE"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "AZ8RZLD3B2TS"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 2025158952  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = [2025158952]  # User id of sudo users
    DEV_USERS = [2025158952]  # User id of dev users
    DEMONS = [2025158952]  # User id of support users
    TIGERS = [2025158952]  # User id of tiger users
    WOLVES = [2025158952]  # User id of whitelist users

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
