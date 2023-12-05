# Notes sur les Animations en Java - Annexe 8

## Principes derrière les animations « utiles » dans une interface graphique :

1. **Informative :** Les animations doivent être informatives, montrant les liens entre les informations. Par exemple, utiliser le geste de glissement (swipe) pour afficher davantage d'informations.

2. **Attractive :** Les animations peuvent attirer l'attention sur des éléments importants. Par exemple, animer un bouton pour indiquer qu'il est cliquable.

3. **Originale :** Les animations apportent un style unique à une application, contribuant à son attrait s'il y a une récurrence appropriée.

## ObjectAnimator :

- ObjectAnimator permet d'animer certaines propriétés d'un objet graphique.
  
- Des méthodes de la classe permettent de définir les propriétés soumises à l'animation.

- Les animations peuvent être établies en XML ou en Java.

- La méthode `invalidate` est automatiquement appelée pour actualiser l'apparence visuelle.

## Exemples :

```java
ObjectAnimator anim = ObjectAnimator.ofFloat(button, View.X, 500f, 1000f);
anim.start();

ObjectAnimator anim2 = ObjectAnimator.ofFloat(image, View.X, View.Y, path);
```
## Propriétés pouvant être utilisées :
- View.X : en fonction de l'origine.
- View.TRANSLATION_X : en fonction de la position au départ, nonobstant 

d'autres translations.
Unités et Conversion :

Les unités sont en pixels. Conversion en dp :

```java
public static int pxToDp(int px) {
    return (int) (px / Resources.getSystem().getDisplayMetrics().density);
}

public static int dpToPx(int dp) {
    return (int) (dp * Resources.getSystem().getDisplayMetrics().density);
```