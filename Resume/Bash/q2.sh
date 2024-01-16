#!/bin/bash

heure=`date  +%k`

if [[ $heure -ge 7 && $heure -lt 11 ]]
then
    echo "Il est $heure heure, c'est le matin."

elif [[ $heure -ge 12 && $heure -lt 18 ]]
then
    echo "Il est  $heure heure c'est l'après-midi"

elif [[ $heure -ge 18 && $heure -lt 23 ]]
then
    echo "Il est $heure heure c'est le soir"

elif [[ $heure -ge 23 && $heure -lt 7 ]]
then
    echo "Il est $heure heure c'est la nuit"
fi