
# L'espace du probleme et l'espace de la solution

nous voulons sanner un biscuit dans un convoilleur
nous devons calculer la qu'elle sorte de biscuit est la 
Si la camera bouge, le biscuit n'est pas centrer etc 

![](note.m\ef3dd3bf-0453-2cfd-fa5e-32f7e58deb8f.svg)

Il faut un espace de solution 

![](note.m\0dfdd531-93e0-6ef6-a42d-845773d0f14a.svg)

Il faut des etoiles et des cercles de differentes taille, une distribution des tailles. AU lien de comparer l'image a un celle biscuit on peut le comparer avec pleins de cercles et d'étoiles

Si nous rajoutant un triangle 
Commen je fais pour savoir si c'est un triange ou un cercle?

![](note.m\08b818fa-4a25-9105-0aa7-3ea30c3489ab.svg)

Nous pouvons rajouter le permiettre

![](note.m\57f77dc8-672a-e9cc-1765-9821368c1ab0.svg)


Maintenant nous avons une meileur idee de ce que pourrait etre l'incconu
c'est l'augmentation de dimmension

si maintenant nous avons un carre, alors nous pouvons rajouter une nouvelle dimmension (en 3d) etc. 

![](note.m\54943e75-cfb4-1861-5f08-5dc79b3e3cdd.svg)
ceci est une boucle for en mathematique 
## L'algo : le K-NN (important al l'exam )
va nous permettre de trouver le plus frequent des cas le plus proches 


![](note.m\89a1ff9b-9dc0-2534-dd4b-28768fcb397e.svg)

## Les cas limite
 si une forme est trop loin de tout les valeurs 
![](note.m\dee0647e-b389-b54a-0032-883402b2cd76.svg)
 

On prend le centroide (moyenne de tout les points) et on regarde le plus proche 




r(img, p = 0.5)
random npy rng = np.random.default_rng()
im_rand = rng.uniform(0.0,1.0,im.shape)