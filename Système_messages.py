#Création d'un bot discord en python avec Cyril et StevieShow
#--------------------------Fonction messages----------------
#------------------------------------------------------------
import discord
import asyncio 
#------------------------------------------------------------

nexus = discord.Client() #On appelle le bot Nexus ^^

@nexus.event 
async def on_ready():
    print("Connecté en tant que : ", nexus.user.name) 
    print("ID : ", nexus.user.name)
#On définit le message de connexion

#Création de premières commandes
#---------------------------------------------
@nexus.event
        #D'abord un ping
if message.content == ".ping" :
    await nexus.send_message(message.channel, "Pong !")
        #--------------------------------------------------------
        #Puis une autre commande
    elif message.content == "Ô mon dieu" :
        await nexus.send_message(message.channel, "Oui ?")
        #---------------------------------------------------------
        #Encore une nouvelle commande
     elif message.content == "Qui est Cyril ?" :
        #---------------------------------------------------------
        await nexus.send_message(message.channel, "Mon Dieu, le tien, le nôtre")
     elif message.content == ".choose" :
        #---------------------------------------------------------
        await nexus.send_message(message.channel, "https://cdn.discordapp.com/attachments/495842732800212995/521308023176560651/Dtu5qUPWoAAdqRV.png")
    elif message.content == "Comment il s'appelle ?" :
        await nexus.send_message(message.channel, "N'Golo Kanté !")
    elif message.content == "Comment il sappelle ?" :
        await nexus.send_message(message.channel, "N'Golo Kanté !")
    elif message.content == "Comment il s'appelle" :
        await nexus.send_message(message.channel, "N'Golo Kanté !")
    elif message.content == "Comment il sappelle" :
        await nexus.send_message(message.channel, "N'Golo Kanté !")
             
        #------------------------------------------------------------
        elif message.content == ".ah" :
            await nexus.send_message(message.channel, "https://giant.gfycat.com/FailingEnragedAsp.webm")
        elif message.content == "ah" :
            await nexus.send_message(message.channel, "https://giant.gfycat.com/FailingEnragedAsp.webm")   
        #-------------------------------------------------------------  
        elif message.content == "Quel est son nom ?" :
            await nexus.send_message(message.channel, "John Cena !")  
        elif message.content == "Quel est son nom " :
            await nexus.send_message(message.channel, "John Cena !")  
         

nexus.run("NTIwNjc0ODIzODk1MTIxOTIw.Du2FpA.hIX2e-uw0IDWyU7RoMeqqO2w7SQ")


	







