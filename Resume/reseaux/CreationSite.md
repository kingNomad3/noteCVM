# Creation site web

## Étape 1 Création des 3 sites Web sur le serveur 1

## Étape 1.1  Création des dossiers et des fichiers nécessaires pour les sites Web

- New-Item -Path C:\_Web\Lab5C_PSH_Entreprise -ItemType directory
- New-Item -Path C:\_Web\Lab5C_PSH_Entreprise\index.htm  -ItemType file -Value "Site de l'entreprise PowerShell"

- New-Item -Path C:\_Web\Lab5C_PSH_Dept1 -ItemType directory
- New-Item -Path C:\_Web\Lab5C_PSH_Dept1\index.htm  -ItemType file -Value "Site du dept1 PowerShell"

- New-Item -Path C:\_Web\Lab5C_PSH_Dept2 -ItemType directory
- New-Item -Path C:\_Web\Lab5C_PSH_Dept2\index.htm  -ItemType file -Value "Site de dept2 PowerShell"


## Étape 1.2  Création des 3 sites Web

 ### Ici, vous avez plusieurs choix : 

 - --> arrêter quelques sites existants pour pouvoir utiliser leur adresse IP

 - --> ajouter d'autres adresses IP sur la carte réseau (pour cela, il faut s'assurer qu'on en a d'autres de disponibles)
     Commande PowerShell pour ajouter une adresse IP sur une carte réseau :
New-NetIPAddress  -InterfaceAlias   -IPAddress    -PrefixLength  

 - --> faire des sites par port.


### J'ai choisi d'arrêter 3 sites existants: 

- Stop-WebSite -Name “Default Web Site”
- Stop-WebSite -Name “Web Adresse 1”
- Stop-WebSite -Name “Web Adresse 3”

- New-Website -Name "Web Site Entreprise PSH" -PhysicalPath - C:\_Web\Lab5C_PSH_Entreprise `
            -IPAddress 10.57.4.1
- New-Website -Name "Web Site Dept1 PSH" -PhysicalPath C:\_Web\Lab5C_PSH_Dept1 `
            -IPAddress 10.57.4.3
- New-Website -Name "Web Site Dept2 PSH" -PhysicalPath C:\_Web\Lab5C_PSH_Dept2 `
            -IPAddress 10.57.4.4


## Étape 1.3 Tester vos 3 sites Web dans un navigateur  (les tests se font par adresse, on n’a pas encore de nom (DNS) pour ces sites)


- http://10.57.4.1
- http://10.57.4.3
- http://10.57.4.4


## Étape 2 Création des zones DNS

### Étape 2.1 Création de la zone DNS pour l'entreprise SUR LE SERVEUR1

- Add-DnsServerPrimaryZone -Name CieAM4PSH.com  -ZoneFile CieAM4PSH.com.dns
- Add-DnsServerResourceRecordA -Name www -IPv4Address 10.57.4.1 -ZoneName CieAM4PSH.com

### Étape 2.2 Création de la zone DNS pour le département 1 SUR LE SERVEUR1

- Add-DnsServerResourceRecordA -Name www.dept1 -IPv4Address 10.57.4.3 -ZoneName CieAM4PSH.com
 

### Étape 2.3 Création de la délégation de zone pour le département 2 SUR LE SERVEUR 1

- Add-DnsServerZoneDelegation -name CieAM4PSH.com  -ChildZoneName dept2 `
                            -nameserver sv2.CieAM4PSH.com   -IPAddress 10.57.4.2 


### Étape 2.4 SUR LE SERVEUR 2 : Création de la zone enfant dept2.CieAM4PSH.com et ajout de l’enregistrement A pour le site Web du département 2


### Add-DnsServerPrimaryZone -name dept2.cieAM4PSH.com  -ZoneFile dept2.cieAM4PSH.com.dns

### Add-DnsServerResourceRecordA -Name www  -IPv4Address 10.57.4.4  -zonename dept2.cieAM4PSH.com


## Étape 2.5 Tests des zones DNS avec la commande NSLOOKUP SUR LE SERVEUR 1 (PowerShell accepte la commande NSLOOKUP)

- NSLOOKUP  www.cieAM4PSH.com
- NSLOOKUP  www.dept1.cieAM4PSH.com
- NSLOOKUP  www.dept2.cieAM4PSH.com

### Étape 3   Tests d'accès par nom dans un navigateur à partir du serveur 1

- www.cieAM4PSH.com 
- www.dept1.cieAM4PSH.com
- www.dept2.cieAM4PSH.com

