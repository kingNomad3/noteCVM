# Glisser et déposer « Drag&Drop » in Android Studio

## Objectifs:
- Utiliser des fichiers .xml pour représenter des formes et des tracés.
Gérer des événements OnTouchEvent et OnDragEvent pour glisser et déposer des objets d’un conteneur à un autre.

## Introduction:
- Dans cet exercice, nous créerons une interface simulant le jeu de backgammon. L'objectif principal est de permettre aux utilisateurs de déplacer une pastille d'une colonne à une autre.

Étapes:
1. Création du projet:
Créez un nouveau projet avec une API 24 ou supérieure.
2. Ajout d'une image:
Utilisez le fichier jeton.jpg et placez-le dans le dossier approprié pour les ressources images externes, soit le dossier res/drawable.
3. Création d'un arrière-plan:
Dans le dossier drawable, créez un nouveau fichier .xml appelé background_contenant.xml. Ce fichier définira l'arrière-plan des colonnes.
Les objets <shape> peuvent être utilisés pour dessiner 4 types de formes :
Rectangle
Oval
Line
Ring

Code pour background_contenant.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<shape xmlns:android="http://schemas.android.com/apk/res/android"
    android:shape="rectangle" >
    <stroke
        android:width="2dp"
        android:color="#FFFFFF" />
    <gradient
        android:angle="225"
        android:endColor="#2ECCFA"
        android:startColor="#000000" />
    <corners
        android:bottomLeftRadius="7dp"
        android:bottomRightRadius="7dp"
        android:topLeftRadius="7dp"
        android:topRightRadius="7dp" />
</shape>
```
4. Création d'un arrière-plan pour la sélection:
Dans le dossier drawable, créez un autre fichier .xml appelé background_contenant_selectionne.xml. Modifiez la couleur de contour en rouge par rapport au fichier précédent.
5. Création de la mise en page:
Dans le dossier layout, modifiez le fichier de mise en page pour avoir un LinearLayout avec 4 sous-conteneurs (représentant les colonnes).
Les sous-conteneurs (colonnes) seront des LinearLayout verticaux. Utilisez @drawable/background_contenant.xml comme arrière-plan pour ces conteneurs.
Ajoutez un ImageView à l'intérieur des colonnes pour représenter la pastille.
EXTRA - Si vous souhaitez ajouter des triangles comme arrière-plan:

Utilisez VectorDrawables pour créer un triangle, car <shape> ne supporte pas les triangles.
Utilisez les liens fournis pour remplir les données du chemin (pathData) pour le triangle.
6. Codage de l'activité:
Implémentez les écouteurs OnDragListener pour les conteneurs (LinearLayouts) et View.OnTouchListener pour les éléments à déplacer (ImageViews).
Utilisez une boucle pour associer les sources aux écouteurs appropriés. La méthode getChildAt peut être utile ici.
7. Implémentation de onTouch:
Lorsque l'utilisateur touche la pastille, commencez le processus de glissement en appelant startDragAndDrop (ou startDrag pour API23 et moins).
Rendez la pastille invisible une fois le glissement commencé en utilisant setVisibility.
8. Implémentation de onDrag:
En utilisant l'API Android, identifiez les 4 états du processus de glissement: "started", "continuing", "dropped", "ended".
Gérez chaque état en conséquence, comme mentionné dans les instructions.
Note: Pour charger un Drawable en Java:

```java
getResources().getDrawable(R.drawable.contenant_selectionne);
```
Récapitulatif:
Dans cet exercice, vous avez appris à utiliser des fichiers .xml pour créer des formes et à gérer des événements pour effectuer des opérations de glissement et de dépôt dans Android Studio. En suivant ces étapes, vous pouvez créer une interface simple pour déplacer une pastille entre différentes colonnes, simulant un jeu de backgammon.



Bien sûr! Voici les notes intégrées avec le code Java séparé en étapes détaillées.

---

## **Glisser et déposer « Drag&Drop » dans Android Studio**

### **Introduction:**

Dans cet exercice, nous créerons une interface simulant le jeu de backgammon. L'objectif principal est de permettre aux utilisateurs de déplacer une pastille d'une colonne à une autre.

---

## **Étapes:**

### **Étape 1: Initialisation**
Commencez par définir les variables essentielles à votre activité, y compris les layouts.

```java
public class MainActivity extends AppCompatActivity {
    LinearLayout parent;
    LinearLayout colonne;
}
```

### **Étape 2: Configuration de l'activité**
Dans la méthode `onCreate`, initialisez vos vues, configurez vos écouteurs et liez-les aux éléments appropriés.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    parent = findViewById(R.id.parent);
    Ecouteur ec = new Ecouteur();

    for (int i = 0; i < parent.getChildCount(); i++) {
        colonne = (LinearLayout) parent.getChildAt(i);
        colonne.setOnDragListener(ec);
        colonne.getChildAt(0).setOnTouchListener(ec);
    }
}
```

### **Étape 3: Création de la classe d'écouteur**
Cette classe gérera les événements de toucher et de glisser.

```java
private class Ecouteur implements View.OnDragListener, View.OnTouchListener {
    Drawable normal = getResources().getDrawable(R.drawable.background_contenant, null);
    Drawable select = getResources().getDrawable(R.drawable.background_contenant_selectionne, null);
    Drawable selectTriangle = getResources().getDrawable(R.drawable.triangle_selectionner, null);
    Drawable normalTriangle = getResources().getDrawable(R.drawable.triangle, null);
    View jeton = null;
}
```

### **Étape 4: Gestion du glissement (Drag)**
Implémentez la méthode `onDrag` pour gérer les différentes actions de glissement.

```java
@Override
public boolean onDrag(View source, DragEvent event) {
    switch (event.getAction()) {
        case DragEvent.ACTION_DRAG_ENTERED:
            if (source == colonne.getChildAt(3) && source == colonne.getChildAt(1)) {
                source.setBackground(select);
            } else {
                source.setBackground(selectTriangle);
            }
            break;

        case DragEvent.ACTION_DRAG_EXITED:
        case DragEvent.ACTION_DRAG_ENDED:
            if (source == colonne.getChildAt(3) && source == colonne.getChildAt(1)) {
                source.setBackground(normal);
            } else {
                source.setBackground(normalTriangle);
            }
            break;

        case DragEvent.ACTION_DROP:
            jeton = (View) event.getLocalState();
            LinearLayout parentOriginel = (LinearLayout) jeton.getParent();
            parentOriginel.removeView(jeton);
            LinearLayout parentActuel = (LinearLayout) source;
            parentActuel.addView(jeton);
            jeton.setVisibility(View.VISIBLE);
            break;

        default:
            break;
    }
    return true;
}
```

### **Étape 5: Gestion des événements tactiles (Touch)**
Implémentez la méthode `onTouch` pour initier le processus de glissement.

```java
@Override
public boolean onTouch(View source, MotionEvent event) {
    View.DragShadowBuilder shadowBuilder = new View.DragShadowBuilder(source);
    source.startDragAndDrop(null, shadowBuilder, source, 0);
    source.setVisibility(View.INVISIBLE);
    return true;
}
```

---

