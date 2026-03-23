from environs import Env

# Reading .env
env = Env()
env.read_env()

# Creating variables
BOT_TOKEN = env.str("BOT_TOKEN")
ADMINS = env.list("ADMINS")
IP = env.str("IP")
