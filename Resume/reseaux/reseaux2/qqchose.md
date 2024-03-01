## Panneau de configuration - Centre Réseau et partage
    Méthode 1 – démarrer PowerShell en tant qu'administrateur
        Set-NetConnectionProfile -InterfaceAlias "OnBoard" -NetworkCategory Private
## PowerShell - permettre l'exécution de script à distance
    # Autorise l'ordinateur à recevoir des commandes à distance
    Enable-PSRemoting -SkipNetworkProfileCheck -Force

    # Cette commande ajoute les ordinateurs auxquels on a confiance
    # * correspond à tous les ordinateurs
    Set-Item WSMan:\localhost\Client\TrustedHosts -Value * -Force

    # Redémarre le service "Gestion à distance de Windows (Gestion WSM)"
    Restart-Service WinRM

    # Cette commande affiche les ordinateurs auxquels on a confiance
    Get-Item WSMan:\localhost\Client\TrustedHosts

## Démonter les partitions sauf le disque C:\
    a)	mountvol.exe e: /d
    b)	mountvol.exe f: /d
    c)	mountvol.exe g: /d
    d)	mountvol.exe h: /d
    e)	mountvol.exe i: /d
    f)	mountvol.exe j: /d
    g)	mountvol.exe k: /d
