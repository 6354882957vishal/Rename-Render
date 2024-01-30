# Don't Remove Credit @SUMIT_KING_2
# Subscribe YouTube Channel For Amazing Bot @SUMIT_KING_9
# Ask Doubt on telegram @King1_devil


import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "29943848")

API_HASH = os.environ.get("API_HASH", "43953a2e9967683decfe979f2ede27e0")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6547990933:AAHFMjvW76QPAS_EpaFJFQIYhWe3yMx3E1U") 

FORCE_SUB = os.environ.get("FORCE_SUB", "SUMIT_KING2") 

             # Don't Remove Credit @SUMIT_KING2
             # Subscribe YouTube Channel For Amazing Bot @SUMIT_KING9
             # Ask Doubt on telegram @King1_devil

DB_NAME = os.environ.get("DB_NAME", "Filerename4GBbot")     

DB_URL = os.environ.get("DB_URL", "mongodb+srv://narutoajr3:cONq92hwYg64X4mv@cluster0.peq9vil.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://te.legra.ph/file/119729ea3cdce4fefb6a1.jpg")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2108417544').split()]

PORT = os.environ.get("PORT", "8080")

# Don't Remove Credit @SUMIT_KING_2
# Subscribe YouTube Channel For Amazing Bot @SUMIT_KING_9
# Ask Doubt on telegram @King1_devil
