



## Variable C#


### RequireComponent

- Cet attribut garantit qu'un composant Rigidbody2D est requis et doit être attaché au même GameObject que ce script. Si ce composant n'est pas présent, Unity l'ajoutera automatiquement.

```C# 
[RequireComponent(typeof(Rigidbody2D))]
```

## Variable Serialisee

- La variable Velocity est sérialisée grâce à l'attribut [SerializeField]. Cela signifie que la vitesse initiale de l'objet peut être ajustée dans l'éditeur Unity sans avoir à modifier le code. Cela est utile pour paramétrer des valeurs spécifiques pour chaque instance de cet objet.

```C#
[SerializeField]
Vector2 Velocity;
```

## Méthodes du Script

### Méthode Start()

- La méthode Start est appelée avant la première image du jeu. Dans cette méthode, on obtient le composant Rigidbody2D attaché au même GameObject en utilisant GetComponent. Ensuite, la vitesse initiale du Rigidbody2D est définie avec la valeur de la variable Velocity. Cela assure que l'objet commence à se déplacer avec la vitesse spécifiée dès le début du jeu.

```C#
void Start()
{
    Rigidbody2D MonRigidbody2D = GetComponent<Rigidbody2D>();
    MonRigidbody2D.velocity = Velocity;
}
```

### Méthode Update()
- La méthode Update est appelée une fois par image dans la boucle de jeu Unity. Dans ce script, la méthode Update est vide, ce qui signifie qu'elle n'effectue aucune action. Vous pouvez y ajouter une logique personnalisée pour gérer les entrées utilisateur ou effectuer des mises à jour continues si nécessaire.

```C#
void Update()
{
    // Cette méthode est vide dans ce script et n'effectue aucune action dans la boucle Update.
    // Vous pouvez ajouter une logique supplémentaire ici si nécessaire.
}
```
### Méthode OnCollisionEnter2D(Collision2D collision)

- La méthode OnCollisionEnter2D est appelée lorsque l'objet entre en collision avec un autre objet 2D dans le jeu. Dans ce cas, elle détruit le GameObject actuel (this.gameObject) lorsqu'une collision se produit.
Ces éléments du script "BalleJouer" expliquent comment le script contrôle le comportement de l'objet de jeu, en particulier son mouvement initial, la gestion des collisions et l'utilisation d'attributs comme [SerializeField] pour faciliter la personnalisation des propriétés dans l'éditeur Unity.

```C#
private void OnCollisionEnter2D(Collision2D collision)
{
    Destroy(this.gameObject);
}
```

### Composant Transform

- Le composant Transform est un composant fondamental de Unity qui représente la transformation d'un GameObject dans l'espace 3D ou 2D. Il stocke les informations sur la position, la rotation et l'échelle de l'objet.

    - La position (position) détermine la position spatiale de l'objet dans le monde. Elle est généralement exprimée en coordonnées XYZ (3D) ou XY (2D).

    - La rotation (rotation) indique l'orientation de l'objet dans l'espace. Elle est généralement exprimée en termes d'angles d'Euler ou d'un quaternion.

    - L'échelle (localScale) détermine la taille de l'objet par rapport à sa taille d'origine.

- Le composant Transform est couramment utilisé pour déplacer, faire pivoter et redimensionner les objets dans Unity, ainsi que pour définir des positions de spawn, des points de vue de caméra et bien d'autres aspects de la scène du jeu.

```C#
[SerializeField]
Transform ExemplaireBalleJoueur;
```

### console Print

- affiche dans la console le temps écoulé depuis le début du niveau.

```C#
Debug.Log("Temps depuis le début du niveau " + Time.time); 
````

### Input Axis

- récupère l'input de l'axe "BougerJoueur" qui représente le mouvement vertical du joueur.
```C#
Input.GetAxis("BougerJoueur") 
Input.GetButtonDown("TirerBalle")
```

### Dans unity

1. Edit > Project Settings, then select Input Manage
    - Change le nom et doit etre le meme nom dans le sript
    - Changer les nom des cmd pour script 
2. input manager

**important, le nom BougerJoeur doit etre le meme nom dans l'axis 

- Dans Negative Button down
- Dans Positive button up 
- Dans Alt Negative Button s
- Dans ALt Positive button w 
    - type : key or mouse button
- Sinon, exemple TirerBalle 
    -Positive Button space


## Utilisation de `Time.time`

- En Unity, `Time.time` est une propriété qui représente le temps en secondes depuis le début du jeu ou depuis l'initialisation du moteur de jeu. Il s'agit d'une valeur de type float qui augmente continuellement à mesure que le jeu s'exécute.

- `Time` : Il s'agit d'une classe intégrée à Unity qui offre des fonctionnalités liées au temps pour la gestion du temps dans un jeu.

- `time` : Cette propriété à l'intérieur de la classe `Time` représente le temps écoulé en secondes. Elle commence à compter à partir de 0 lorsque le jeu démarre et augmente en temps réel à mesure que le jeu progresse.

## Exemple d'utilisation

```csharp
// Exemple de code en C#
Debug.Log("Temps depuis le début : " + Time.time);
```

### Destroy(this.gameObject);

- La fonction `Destroy(this.gameObject)` est une fonction intégrée dans Unity qui permet de détruire l'objet auquel le script est attaché. Cela signifie que l'objet lui-même, et tout ce qui lui est attaché, sera supprimé de la scène.

## Utilisation de `Destroy(this.gameObject)`

- `Destroy(this.gameObject)` est généralement utilisé pour supprimer des objets de la scène en réponse à certaines conditions ou actions. Par exemple, vous pouvez l'utiliser pour détruire un projectile après qu'il ait touché une cible, ou pour supprimer un ennemi lorsqu'il est vaincu.

   Exemple d'utilisation dans un script Unity :
   ```csharp
   private void OnCollisionEnter(Collision collision)
   {
       if (collision.gameObject.tag == "Projectile")
       {
           // Détruire cet objet (par exemple, un ennemi) lorsqu'il est touché par un projectile
           Destroy(this.gameObject);
       }
   }
    ```

- L'appel à Destroy(this.gameObject) détruit immédiatement l'objet courant, le retirant de la hiérarchie de la scène et libérant ses ressources associées.

- Il est important de noter que cette fonction doit être utilisée avec précaution, car elle peut avoir un impact sur la performance de votre jeu si elle est utilisée de manière excessive. Il est recommandé de détruire les objets de manière appropriée lorsqu'ils ne sont plus nécessaires pour éviter les fuites de mémoire.

- La fonction Destroy(this.gameObject) est essentielle pour la gestion des objets et des ressources dans Unity, permettant de créer des mécaniques de jeu dynamiques en ajoutant et en supprimant des éléments de la scène en temps réel.

# Extras

# Fonctions d'Entrée Joueur en Unity

Unity offre plusieurs fonctions pour gérer les entrées joueur, que ce soit depuis un clavier, une souris, un contrôleur ou un écran tactile. Voici quelques-unes des fonctions d'entrée les plus couramment utilisées :

## `Input.GetButtonDown()`

### `Input.GetButtonDown(nomDuBouton)` 
- permet de détecter si un bouton spécifique a été enfoncé. Cette fonction renvoie `true` pendant un seul frame lorsque le bouton est enfoncé.

   Exemple :
   ```csharp
   if (Input.GetButtonDown("Sauter"))
   {
       // Faire quelque chose lorsque le bouton "Sauter" est enfoncé
   }
    ```
### Input.GetAxis()
- permet de récupérer l'entrée liée à un axe spécifique. Elle renvoie une valeur continue qui dépend de la façon dont le joueur déplace un joystick ou appuie sur des touches associées à cet axe.

```C#
float mouvementHorizontal = Input.GetAxis("Horizontal");
```

### Input.GetKey()
- permet de vérifier si une touche du clavier est actuellement enfoncée. Elle est utilisée pour des contrôles basés sur des touches du clavier.

Exemple :

```C#
if (Input.GetKey(KeyCode.E))
{
    // Faire quelque chose lorsque la touche E est enfoncée
}
```

### Input.GetMouseButtonDown()
- Détecte si un bouton de la souris (clic gauche, clic droit, etc.) a été enfoncé. Elle est utilisée pour détecter les clics de souris.
```C#
if (Input.GetMouseButtonDown(0))
{
    // Faire quelque chose lorsque le bouton gauche de la souris est enfoncé
}
```

### Input.GetAxisRaw()
- permet de détecter si une touche a été enfoncée pendant le frame actuel uniquement. Elle est utile pour gérer des événements qui ne doivent se produire qu'une seule fois lorsqu'une touche est enfoncée.

```C#
if (Input.GetKeyDown(KeyCode.E))
{
    // Faire quelque chose lorsque la touche E est enfoncée dans ce frame
}
```

### Input.GetButton()
- permet de vérifier si un bouton virtuel configuré dans les paramètres d'entrée d'Unity est actuellement enfoncé. Elle est couramment utilisée pour créer des contrôles personnalisés et des boutons configurables.

```C#
if (Input.GetButton("Sauter"))
{
    // Faire quelque chose lorsque le bouton "Sauter" est enfoncé
}
```

### Input.touches (pour les appareils mobiles)
- Pour les appareils mobiles, Unity fournit un tableau d'objets Touch qui représente les entrées tactiles, y compris les appuis et les mouvements de doigts sur l'écran.
- Ces fonctions et méthodes vous permettent de gérer divers types d'entrées joueur en fonction des besoins de votre jeu.



```C#
if (Input.touches.Length > 0)
{
    Touch premierAppui = Input.touches[0];
    // Traitement des entrées tactiles
}
```