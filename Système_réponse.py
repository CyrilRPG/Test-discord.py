#Création d'un bot discord en python avec Cyril : Salut !
#--------------------------Importation des modules----------------
#------------------------------------------------------------
import discord

nexus = discord.Client()

@nexus.event
async def on_message(message):
    # On va être sûr que le bot ne répond pas à lui même
    if message.author == nexus.user:
        return

    if message.content.startswith('.Salut'): #une conditon de message
        message2 = 'Salut {0.author.mention} !'.format(message) #la réponse du bot
        await nexus.send_message(message.channel, message2) 
        #le message va être affiché dans le même channel que l'user a mit
    elif message.content.startswith('.salut'): #une conditon de message
        message2 = 'Salut {0.author.mention} !'.format(message) #la réponse du bot
        await nexus.send_message(message.channel, message2) 
        #le message va être affiché dans le même channel que l'user a mit

@nexus.event 
async def on_ready():
    print("Connecté en tant que : ", nexus.user.name) 
    print("ID : ", nexus.user.name)
#On définit le message de connexion

nexus.run("token")
