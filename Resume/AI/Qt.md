# Introduction Ã  Qt (1/3)
Cet exemple introductif prÃ©sente comment crÃ©er une application de type sÃ©lection de couleur avec Qt.
#
# Le schÃ©ma suivant prÃ©sente les widgets utilisÃ©.
#   __________________________________________________________________
#  |__________________________________________________________________|
#  |             ________________________           _____     _____   |
#  |  Rouge     |__________________|_|___|   212   |_____|   |     |  |
#  |             ________________________           _____    |     |  |
#  |  Vert      |_|______________________|    0    |_____|   |     |  |
#  |             ________________________           _____    |     |  |
#  |  Bleu      |_____________|_|________|   188   |_____|   |_____|  |
#  |__________________________________________________________________|
# 
#    \____/     \________________________/  \____/ \_____/   \_____/
#      |                     |                |       |         |
#      |                     |                |       |         \_ QLabel : affiche une image de la couleur finale
#      |                     |                |        \_ QLabel : affiche une image pour chaque bande de couleur (intensitÃ© de rouge, vert, bleu)
#      |                     |                 \_ QLabel : affiche un texte pour la valeur de chaque bande de couleur (intensitÃ© de rouge, vert, bleu)
#      |                      \_ QScrollBar : sÃ©lection de la valeur pour chaque bande de couleur (intensitÃ© de rouge, vert, bleu)
#       \_ QLabel : affiche un titre pour chaque bande de couleur
#
#
# Cet exemple est constituÃ© de plusieurs "layout" imbriquÃ©s les uns dans les autres. Les "layouts" permettent une gestion automatisÃ©e de la disposition Ã  l'Ã©cran.
# Le schÃ©ma suivant prÃ©sente quelle est la disposition des 6 "layouts" utilisÃ©s.
# 
#   _________________________________________________________________________________________
#  |_________________________________________________________________________________________|
#  |                                                                                         |
#  |   ___________________________________________________________________________________   |
#  |  6                                                                                   |  |
#  |  |   _____________________________________________________________________________   |  |
#  |  |  5                                                                             |  |  |
#  |  |  |   ______________________________________________________________            |  |  |
#  |  |  |  4                                                              |           |  |  |
#  |  |  |  |   ________________________________________________________   |           |  |  |
#  |  |  |  |  1             ________________________           _____   |  |   _____   |  |  |
#  |  |  |  |  |  Rouge     |__________________|_|___|   212   |_____|  |  |  |     |  |  |  |
#  |  |  |  |  |________________________________________________________|  |  |     |  |  |  |
#  |  |  |  |                                                              |  |     |  |  |  |     
#  |  |  |  |   ________________________________________________________   |  |     |  |  |  |     
#  |  |  |  |  2             ________________________           _____   |  |  |     |  |  |  |
#  |  |  |  |  |  Vert      |_|______________________|    0    |_____|  |  |  |     |  |  |  |
#  |  |  |  |  |________________________________________________________|  |  |     |  |  |  |
#  |  |  |  |                                                              |  |     |  |  |  |     
#  |  |  |  |   ________________________________________________________   |  |     |  |  |  |     
#  |  |  |  |  3             ________________________           _____   |  |  |     |  |  |  |
#  |  |  |  |  |  Bleu      |_____________|_|________|   188   |_____|  |  |  |_____|  |  |  |
#  |  |  |  |  |________________________________________________________|  |           |  |  |
#  |  |  |  |                                                              |           |  |  |
#  |  |  |  |______________________________________________________________|           |  |  |
#  |  |  |                                                                             |  |  |
#  |  |  |_____________________________________________________________________________|  |  |
#  |  |                                                                                   |  |
#  |  |___________________________________________________________________________________|  |
#  |                                          /                                              |
#  |                                         /                                               |
#  |                                         \                                               |
#  |                                          \  (stretch)                                   |
#  |                                           \                                             |
#  |                                           /                                             |
#  |__________________________________________/______________________________________________|
#  Informations sur les layouts :
#   - (1), (2) et (3) : 
#       - QHBoxLayout
#       - gÃ¨re la disposition horizontale de 4 widgets : 
#           - le titre
#           - la barre de dÃ©filement
#           - la valeur de la couleur
#           - l'image de la couleur
#   - (4) :
#       - QVBoxLayout
#       - gÃ¨re la disposition verticale des trois "layouts" (1), (2) et (3)
#   - (5) :
#       - QHBoxLayout
#       - gÃ¨re la disposition horizontale entre le "layout" (4) et l'image de la couleur finale
#   - (6) :
#       - QHBoxLayout
#       - gÃ¨re la disposition verticale du "layout" (5) et de l'application
#
# L'implÃ©mentation suivante est plutÃ´t simple et vise une comprÃ©hension de base. Les exemples suivants pourront approfondir quelques aspects supplÃ©mentaires.



- est souvent utiliser sur le systeme embarquer, par exemple le moniteur de coeur a l'hopital est surment afficher avec utie 
- supporter dans plusieurs language ici pyecutie 

## composition
- une notion de composition, vous avez l'application principale qui est commencer de widjet et les widget peuvent etre composer de plusieurs widget comm eun arbre genialogique.Comme un linear layout. Il y a une notion de parent si on delete ou change de dependence en memoire du parent ( pas de garbage collector), alors les parents vont gerer la memoire des enfants  et une notion de disposition les enfants seront affecter  
- On va utiliser le QmainWindow pour supporter les widget, doit toujorus avoir au milieu un 
- Qwidget central le Qw aura la composition qu'on veut 
- Un Qlabel aura du text non interactif,
- QscrollBar
- QHboxLayout pour la couleur rouge
- QVBoxLayout pour bleu

## observor
- exactement comme un listener en java  
![](Qt.m\5347bbce-0c7a-fcc6-52f0-c49989074c75.svg)

- Lorsque qqchose va bouger met l'autre a jour
    - on peut connecter un signal a n slot 
    - on peut aussi avoir m vers n  

