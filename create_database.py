import crypt
import sqlite3

# Connexion à la base SQLite
conn = sqlite3.connect('/root/soc-portal/instance/database.db')

# Cursor va prendre les commandes
cursor = conn.cursor()

prenoms = ["Aghilas", "Maya Sandra", "Abdelaziz", "Amine", "Yacine", "Victor", "Belkacemi", "Nada", "Alaa", "Lina Rania", "Assirem", "Elisa", "Roberto", "Lisa", "Feriel", "Clément", "Lylia", "Menouar", "Aziz", "Ornella", "Bastien", "Abdou aziz", "Mehdi", "Robin", "Moncef", "Jordan", "Amine", "Marcel", "Solène", "Arvin", "Mohammed", "Sid Ali Samy", "Anes", "Alexandre", "Stéphane", "Olivier"]
noms = ["AIT HADJI", "AIT YAHIA", "AMEURLAIN", "ROSTOM HASSEN", "AMRANI", "BARRAULT", "CHEMS EDDINE", "BOUAADI", "BOUAGADA", "BOUYAHIA", "BOUYOUCEF", "CAZERES", "CHEMAMA", "DAOUDI", "DENDANI", "DESBOIS", "DJALI", "DJEMA", "DJERMANI", "FABI", "FALCHERO", "FALL", "GHOUILA", "HOSKING", "KHODRI", "LAIRES", "LAKHEL", "LE", "MICELI", "MOHAMMADY", "MOULOUDI", "MOURI", "NECHAF", "OGANEZOV", "PATEL", "PAUCHONT"]
logins = ["aaithadji", "maityahia", "aameurlain", "arostomhassen", "yamrani", "vbarrault", "bchemseddine", "nbouaadi", "abouagada", "lbouyahia", "abouyoucef", "ecazeres", "rchemama", "ldaoudi", "fdendani", "cdesbois", "ldjali", "mdjema", "adjermani", "ofabi", "bfalchero", "afall", "mghouila", "rhosking", "mkhodri", "jlaires", "alakhel", "mle", "smiceli", "amohammady", "mmouloudi", "smouri", "anechaf", "aoganezov", "spatel", "pauchont"]
passwords = ['BSx7c8kvQxqZb80c', 's4zEMFUbjnkybORw', 'kgl5Jsg4g8Ezh4RY', 'X5dfxqKKAn43kTkk', 'KAPD04ke9uAZUvII', 'sOdRuuI1uNrXmEfi', 'hDxqr5LuJKhRZSGV', 'zx61ERRqAUaI3xXi', 'RfTMupNLJwsx1Q7H', '00hrXglCPkCXl4aw', 'ts5uEOfhmhQylCuh', 'qV9Y2eChMEwx1Vns', '1CuXCmggoxQeCxKG', 'VzKbv5b5mlZAynt5', 'uNnQljfbgLaK14XD', '1s05Mpp1SuFF2sag', 'T5oUZkMmCEq90YEj', 'LBJyVzeq9pfpWtB6', 'OXLYhKSYjC1FFPN2', 'XUChiCJh04t4vK9Y', 'tjYJoP8vskQdb0Ow', 'dfjpinaVPsC8dBaz', 'iFtDAbfmEIJJ9q8V', 'vIkoyjWFns6tWVDq', 'jbxd8MjM3qH9fSrB', 'zSiMuChGYmbABb7B', 'kkXgkk6wdDeu3pMm', 'Qg9I6be5q799iOv7', 'Tgd9ndKLevHbkiUg', '1skDEhoGe5lmwwtH', 'yEdqDa0d2hAMheWH', 'w7AWgbCNfg4YnY96', 'UkwuqxCfEMFLqAYm', 'U5zQvZLo4Sxh7c6Q', 'Wjw9tYsi2zhjwfMU', 'uxGtSyTyzBKnYhIh', '6U5qzU5hQKfJW8yR']

groupe = 1
for i in range(0,39):
    if (i+2 == 10) || (i+2 == 18) || (i+2 == 26) || (i+2 == 33):
        groupe += 1
        
    hashed = crypt.crypt(passwords[i], salt=None)
    cursor.execute("INSERT INTO user (id, prenom, nom, login, password_hash, groupe) VALUES ('"+str(i+1)+"','"+prenoms[i]+"','"+noms[i]+"','"+logins[i]+"','"+hashed+"','"+str(groupe)+"'');")
    
# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
