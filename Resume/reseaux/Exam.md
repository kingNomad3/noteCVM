# SYNTHÈSE C43

## CRÉATION DES ORDINATEURS VIRTUELS
 1. Vous devez vérifier l'intégrité du fichier ISO avec le script PowerShell S2019_SHA256.ps1 (cette vérification peut prendre jusqu’à 1 minute).

2.  Paramétrer les commutateurs virtuels
```word
Démarrer la console "Gestionnaire Hyper-V".
	Dans la section de gauche, vous devez sélectionner votre serveur
Dans le menu contextuel, choisir "Gestionnaire de commutateur virtuel…"
o	Sélectionner le commutateur que vous avez créé et modifier son nom pour "EXTERNE".
o	Vous devez créer un commutateur virtuel de type PRIVÉ dont le nom sera "PRIVE_PROJET".
On désire modifier la plage des adresses MAC pour utiliser la plage suivante
00155Dccpp00 à 00155DccppFF
cc = 37 pour le local A5.37
cc = 38 pour le local A5.38
cc = 47 pour le local C4.07
cc = 48 pour le local C4.08
pp = numéro de votre ordinateur réel en utilisant deux chiffres
```


2. Création des ordinateurs virtuels dans Hyper-V
- 
```word
Voici les propriétés de l'ordinateur virtuel "SERVEUR1"
Nom: PROJET_SERVEUR1 et PROJET_SERVEUR2 
L’emplacement devrait être "C:\_VIRTUEL\ORDI"
o	Génération 2
o	Mémoire de démarrage: 4096 Mo
décocher "Utiliser la mémoire dynamique pour cet ordinateur virtuel."
o	Connexion: PRIVE1
o	Cocher "Créer un disque dur virtuel"
	Nom: serveur1.vhdx
	Emplacement: C:\_VIRTUEL\DISQUE
	Taille 60 GO
o	Cocher "Installer un système d'exploitation à partir d'un fichier image de démarrage"
Fichier image (.iso): C:\_ISO\fr-fr_windows_server_2019_updated_aug_2021_x64_dvd_b863695e.iso
```
```word
Copier le fichier pfSense 2.5.2.vhdx qui est dans le dossier
\\uranusprof.reseau.cvm\intranet\rjean\Hyper-V\GEN1 - pfSense 2.5.2 dans le dossier C:\_VIRTUEL\DISQUE de votre serveur réel. Je vous conseille de garder une copie de ce fichier.

Étape 1 - Création de l'ordinateur virtuel "ROUTEUR1"
Création de l'ordinateur virtuel "ROUTEUR1"
o	Nom: ROUTEUR1
Emplacement: C:\_VIRTUEL\ORDI
o	Génération 1
o	Mémoire de démarrage: 1024 Mo
ne pas cocher "Utiliser la mémoire dynamique pour cet ordinateur virtuel."
o	Connexion: EXTERNE
o	Sélectionner l'option "Utiliser un disque dur virtuel existant"
Emplacement: C:\_VIRTUEL\Disque
Nom du fichier: routeur1.vhdx

il faut creer l'externe en premier et ensuite le prive 1

À la fin de la création de l’ordinateur virtuel, vous devez ajouter une deuxième carte réseau.
	Cette carte réseau doit utiliser le commutateur "PRIVE1"

Pour modifier la configuration du routeur pfSense à partir de votre serveur réel.
https://10.57.x.y
nom d'utilisateur = admin
mot de passe = pfsense

Pour modifier la configuration du routeur pfSense à partir d'un ordinateur virtuel qui est dans le réseau LAN.
https://192.168.1.1
nom d'utilisateur = admin
mot de passe = pfsense

```

# Configuration IP
- Le SERVEUR2 aura deux cartes réseau. Le nom de la première carte réseau sera "NAT1" et utilisera une ou plusieurs adresses statiques. Le nom de la deuxième carte réseau sera "NAT2" et utilisera une configuration IP provenant du serveur DHCP.

- ncpa.cpl 
- rename


config dans le dns et dhcp

Panneau de configuration - Centre Réseau et partage
Dans le menu à gauche: "Modifier les paramètres de la carte"
	Cliquer sur la carte réseau et la renommer EXTERNE

Afficher les propriétés de la carte réseau EXTERNE
	Modifier les propriétés de l’item Protocole Internet version 4 (TCP/IPv4)
o	Sélectionner Utiliser l'adresse IP suivante:
Adresse IP (SERVEUR1): 192.168.1.11
Adresse IP (SERVEUR2): 192.168.1.21
Masque de sous-réseau: 255.255.255.0
Passerelle par défaut: 192.168.1.1
o	Sélectionner Utiliser l'adresse de serveur DNS suivante:
Serveur DNS préféré:   127.0.0.1


Installation du rôle IIS


$nic = "nat1"

for ($i = 101; $i -le 110; $i++)
{
  New-NetIPAddress -InterfaceAlias $nic `
                   -IPAddress 192.168.1.$i `
                   -PrefixLength 24
}

Get-NetIPAddress -InterfaceAlias $nic `
                 -AddressFamily IPv4 | Select-Object IPv4Address,PrefixLength

Gestionnaire de serveur  Gérer  Ajouter des rôles et fonctionnalités

Ajouter le rôle "Serveur Web (IIS)"
 
Sélectionner "Serveur Web (IIS)"

 
Cliquer sur le bouton "Ajouter des fonctionnalités"


Tester l’accès à la page web par défaut du serveur IIS avec http://127.0.0.1

Ouvrir la console "Gestionnaire des services Internet (IIS)".
Sur la rubrique de votre serveur ouvrir le nœud Sites
 

Répondre aux questions suivantes en inspectant les outils et les propriétés reliés au site "Default Web Site"
 

L'installation du rôle "Serveur Web (IIS)" a ajouté un répertoire
Actions / Paramètres de base...
Le chemin d'accès physique est %SystemDrive%\inetpub\wwwroot donc c:\inetpub\wwwroot
Le dossier c:\inetpub\wwwroot contient deux fichiers: iisstart.htm et iisstart.png

L'installation du rôle "Serveur Web (IIS)" a ajouté un groupe local.
Get-LocalGroup -Name iis*
 

Le groupe IIS_IUSRS a des autorisations NTFS de "Lecture et exécution" sur le dossier "c:\inetpub\wwwroot".

Vous devez sélectionner le serveur "SERVEUR1".

Sélectionner "En-têtes de réponse HTTP"
À droite dans "Actions", vous devez sélectionner "Définir les en-têtes communs…"

Voici la configuration à effectuer
 
Immédiatement: Ce paramètre convient aux contenus que vous ne souhaitez pas mettre en cache ou qui sont mis à jour fréquemment.

La configuration du paramètre sera valide pour tous les sites web.


## adresse librer
192.168.1.110           24
192.168.1.109           24
192.168.1.108           24
192.168.1.107           24
192.168.1.106           24
192.168.1.105           24 
192.168.1.104           24 
192.168.1.103           24 
192.168.1.102           24 -
192.168.1.101           24 -
192.168.1.21 



Zones de recherche directes
labo DNS avec reponse
delegation de zone 
look up dns 

Redirecteur
voir mio 


## Le contenu des fichiers HTML
Création de deux sites WEB par adresse

Sur le SERVEUR1
Dans votre Gestionnaire des services Internet (IIS), ajouter un nouveau site Web "par adresse" ayant les caractéristiques suivantes:
o	Nom du site: Web adresse 101
o	Chemin d’accès physique: e:\_web\adresse_101
o	Adresse IP: 192.168.1.101
o	Port: 80

Créer un fichier "index.htm" dans le dossier e:\_web\adresse_101 contenant les informations suivantes:
o	Votre nom
o	Le nom du site: Web adresse 101
o	Type de site: site par adresse
o	L'adresse IP: 192.168.1.101
o	Le numéro de port: 80

Tester l'accès à votre nouveau site web avec http://192.168.1.101


<h1>corpo local </h1>
<body>
•	Benjamin Joinvil 1662413 <br>
•	Par adresse<br>
•	192.168.1.101 port 80<br>
•	www.corpo.local<br>
•	Serveur1<br>
•	Le nom de domaine pleinement qualifié (FQDN) pour le site	<br>
</body>


pour la delegation il faut ajouter un enrigistrement dans les deux


par entete
Dans votre Gestionnaire des services Internet (IIS), ajouter un nouveau site Web en utilisant un nom d'hôte ayant les caractéristiques suivantes:
o	Nom du site: Web ENT1 101
o	Chemin d’accès physique: c:\_web\ent1_101
o	Adresse IP: 192.168.1.101
o	Port: 80
o	Nom de l'hôte: ent1.formation.local

Créer un fichier index.htm dans le dossier "c:\_web\ent1_101" contenant les informations suivantes:
o	Votre nom
o	Le nom du site: ent1.formation.local
o	Type de site: site par en-tête
o	L’adresse IP: 192.168.1.101
o	Le numéro de port: 80


Dans votre Gestionnaire des services Internet (IIS), ajouter un nouveau site Web en utilisant un nom d'hôte ayant les caractéristiques suivantes:
o	Nom du site: Web ENT2 101
o	Chemin d’accès physique: c:\_web\ent2_101
o	Adresse IP: 192.168.1.101
o	Port: 80
o	Nom de l'hôte: ent2.formation.local

Créer un fichier index.htm dans le dossier "c:\_web\ent2_101" contenant les informations suivantes:
o	Votre nom
o	Le nom du site: ent2.formation.local
o	Type de site: site par en-tête
o	L’adresse IP: 192.168.1.101
o	Le numéro de port: 80

Sur le SERVEUR2
Dans la zone formation.local créer deux enregistrements de type "A"
o	Nom = ent1
Adresse IP = 192.168.1.101
o	Nom = ent2
Adresse IP: 192.168.1.101



gestion
document par defaut et ajouter gestion.htm


LE SERVEUR DHCP

Pour acceder a pf sense https://192.168.1.1/

plage 192.168.1.103
192.168.1.202

exlus 192.168.1.103 a 192.168.1.107