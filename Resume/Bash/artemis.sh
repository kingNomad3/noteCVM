#!/bin/bash

# Colors :
# Black: \033[30m
# Red: \033[31m
# Green: \033[32m
# Yellow: \033[33m
# Blue: \033[34m
# Magenta: \033[35m
# Cyan: \033[36m
# White: \033[0m

sauvegarderPartie () {
	date=`date +'[%Y-%m-%d %H:%M:%S]'`

    if [[ $1 = "d" ]]
    then
        echo "$date - Défaite" >> score.txt
    else
        echo "$date - Victoire" >> score.txt
    fi
}

menuFinPartie () {
    clear

    if [[ $1 = "d" ]]
    then
        echo -e "\033[31m"
        echo "             __"
        echo "           _|  |_"
        echo "         _|      |_"
        echo "        |  _    _  |"
        echo "        | |_|  |_| |"
        echo "     _  |  _    _  |  _"
        echo "    |_|_|_| |__| |_|_|_|"
        echo "      |_|_        _|_|"
        echo "        |_|      |_|"
        echo ""
        echo "      Vous avez perdu..."
        echo ""
    else
        echo -e "\033[32m"
        echo ">>>>>>>_____________________|-._"
        echo ">>>>>>>                     |.-"
        echo ""
        echo "       Vous avez gagné !"
        echo ""
    fi

    echo -e "\033[0m"
    read -p "Appuyez sur entrée pour continuer..."
}

afficherEtatJeu() {
    echo -n "D"

    i=0
    while [[ $i -le 18 ]]
    do
        i=$(($i+1))

        if [[ $i -eq $1 ]]
        then
            if [[ $i -eq $2 ]]
            then
                echo -ne "\033[31mX\033[0m"
            else
                echo -ne "\033[34m→\033[0m"
            fi
        elif [[ $i -eq $2 ]]
        then
            echo -n "👾"
        else
            echo -n " "
        fi
    done

    echo ""
    echo ""
}

jouer () {
    clear
    echo ""

    posMonstre=$(( $RANDOM % 3 + 15 ))
    afficherEtatJeu 1 $posMonstre
    read -p "Indiquez la force à appliquer sur l'arc pour que la flèche touche la cible (entre 15 et 18) : " force

    posFleche=1

    while [[ $posFleche -lt $force ]]
    do
        clear
        posFleche=$(($posFleche+1))
        afficherEtatJeu $posFleche $posMonstre
        sleep 0.05
    done

    sleep 2
    etat=d

    if [[ $force -eq $posMonstre ]]
    then
        etat=v
    fi

    sauvegarderPartie $etat
    menuFinPartie $etat
}

menu () {
    clear
    echo -e "\033[32;1m  >>> ------- Artemis ----------->\033[0m"
    echo "          [a] Jouer"
    echo "          [s] Score"
    echo "          [q] Quitter"
    echo ""
}

afficherScore () {
    clear

    cat score.txt

    echo ""
    read -p "Appuyez sur une touche pour continuer..."
}

choix=

while [[ $choix != "q" ]]
do
    menu
    read -p "Choix : " choix

    if [[ $choix = "a" ]]
    then
        jouer
    elif [[ $choix = "s" ]]
    then
        afficherScore
    fi

done