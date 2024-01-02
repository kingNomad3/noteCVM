#!/bin/bash


# afficher un menu
# mettre le menu dans une fonction
#offire 2 choix :quitter (choixq)
# ou appelez ./execice2.sh (choix d)
# a chaqe debut de boucle afficber le menu

afficherMenu(){
    clear
    echo "---------"
    echo " Menu"
    echo "-------------"
    echo "Appeler exercice 2(d)"
    echo "Quitter(q)"
    
}

choix=

while [[ $choix != q ]]
do 
    afficherMenu
    read -p "Entrez votre choix: " choix
    if [[ $choix = d ]]
    then
        ./exercice1.sh
    fi
done

