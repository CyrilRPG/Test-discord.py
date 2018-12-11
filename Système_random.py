#-------Création d'un bot discord en python avec Cyril : Jeu aléatoire !
#--------------------------Importation des modules----------------
#------------------------------------------------------------
import discord
import random
#------------------------------------------------------------

nexus = discord.Client() #On appelle le bot Nexus ^^

#Système de jeu 
#-------------------------------------------------------------
@nexus.event
async def on_message(message): #On lit un message que l'on va indiquer

    if message.author == nexus.user:
        return
    if message.content.startswith('.play'):
        await nexus.send_message(message.channel, 'Choisis un nombre entre 1 et 10')

        def guess_check(m):
            return m.content.isdigit()

        guess = await nexus.wait_for_message(timeout=5.0, author=message.author, check=guess_check)
        answer = random.randint(1, 10)
        if guess is None:
            fmt = "Désolé, vous avez pris trop de temps. C'était {}."
            await nexus.send_message(message.channel, fmt.format(answer))
            return
        if int(guess.content) == answer:
            await nexus.send_message(message.channel, 'Tu as raison !')
        else:
            await nexus.send_message(message.channel, "Désolé. C'est en fait {}.".format(answer))

@nexus.event 
async def on_ready():
    print("Connecté en tant que : ", nexus.user.name) 
    print("ID : ", nexus.user.name)
#On définit le message de connexion


nexus.run("Token")
