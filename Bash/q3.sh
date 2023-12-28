#!/bin/bash

read -p "Texte : " txt

case $txt in
    [[:lower:]])
    echo "la lettre est minuscule"
    ;;
    [[:upper:]])
    echo "la lettre est majuscule"
    ;;
    [[:digit:]])
    echo "C'est un chiffre"
    ;;
    *)
    echo "autre"

esac

