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