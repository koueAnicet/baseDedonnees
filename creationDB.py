
import sqlite3




conn = sqlite3.connect('database.db')
#designer le cursor "c"
c =conn.cursor()
#executer le cursor
""" puisque les code se sql sont longue il faut add commentaire sur plusieur ligne
la methode IF NOT EXISTS db permet de dire de creer si il existe pas"""
c.execute("""CREATE TABLE IF NOT EXISTS inscriptions (
        nom text,
        prenom text,
        email integer,
        mdp integer,
        confir_mdp integer
    )""")
 


#ajout des valeurs/inserrer
c.execute("INSERT INTO inscriptions VALUES(:nom , :prenom , :email , :mdp ,:confir_mdp)", 
#On creer un dictionnaire d , la meilleur methode
 donnesInscription= {
 "nom": "23",
 "prenom": "343",
 "email": "343",
 "mdp": 433,
 "confir_mdp": 34
 })

"""recuperer les donnees et le mettre dans une variable
# autre methode where champ=:cle dict"""

#c.execute("SELECT * FROM actions")

#mise a jour des donnees avec UPDATE table SET ...
#c.execute("""UPDATE actions SET nom=:nom WHERE prenom=:prenom AND age=:age""", d)

#Suppression des donnes avec la methode 
#c.execute("DELETE FROM employes")
"""parcourir les donnees a partir du cursoeur fetchone le premier element de la base de donnees/ fetchall tout les elements"""
donnees = c.fetchone()

#executer la requette
#1- commit envoyer donnees a la base de donnees
conn.commit()
#2-fermer la base de donnees
conn.close()

