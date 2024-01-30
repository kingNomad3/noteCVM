# robot
    -roue libre 
    - contre poids (la batterie)
    - le truc en arriere de dois pas toucher le sols

    - le plus grand defi de la robotic est l'alimentation, tres gourment en electricite 

    - Le robot a plusieurs capteur 
        - camera V2.1, c'est un flu video de type compresser mpeg
        - le range fider (mesureur de distance) le truc au milieu des yeux
        - capteur d'intenister lumineuse et de couleur RGN en haut des yeux. Il contient aussi un flash 
        -6 capteur en dessous, c;est un detecteur de ligne (comme caoteur lumineux) le truc en avant qui ne doit pas toucher le sol
        - detecteur de rotation des roues 
        - capteur d'inpedence, detect la pulsion des emant avec les roues
        - capteur d'inercie (detecte la reference en 3 dans un espace a partir d'une position de depart )
        - accelerometre, medure la vitesse (varation de la vitesse selon le temps ), il en a 3 donc 3d, la fleche blanche 
        - le truc bleu capteur pour le telecommande

Les actionnaires
    se sont les choses qui nous donnes du feetback, des donnees 
        - les roues
        - des lumieurs
            - les yeux (RGB) ont peut changer la couleur
            - les blinker slm allumer et eteind en rouge

Le speaker 

Le cerveau moteur
    - perment de bouger la camera 
    - c'est un moteur qui bouge en angle, asservie en position

si le controleur de camera tourne trop, les files vont arracher nous allons creer une buter virtuel afin d'eviter ca 

les communication
    plaquette rouge 4 connexto blanche i2c, ad1, ad2, i2c
    nous avons les servo 1 et 2
    serial, tres long mais plus stable electriquement 

    i2c protocole d serial plus moderne, moins grand porter on puet brancher un capteur et sur se capteur en peut en serie plusieurs capteur

    plaquette rouge
        port internet
        4 prise usb, une est un os pour demarer 

       