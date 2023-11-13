# Notes sur `startActivityForResult` et `saveInstanceState`

## A) Exercice :

### Application simple avec deux activités :
1. L'utilisateur est salué dans `AccueilActivity`.
2. On lui demande d'entrer des informations dans une deuxième activité, `IdentificationActivity`, pour personnaliser le message d'accueil.

### Étapes à suivre :
- Gérer les événements de clic.
- Créer la classe `Utilisateur` avec les attributs prénom et nom.
- Utiliser `startActivityForResult` pour passer à `IdentificationActivity`.

#### Nouvelle technique (`startActivityForResult`):
- **Activité de départ (`AccueilActivity`):**
  - Déclarer et créer un objet `ActivityResultLauncher<Intent>`.
  - Lancer un intent avec `launch` lors du clic sur le bouton.

- **Activité de destination (`IdentificationActivity`):**
  - Créer un Intent de retour.
  - Gérer le clic du bouton pour transmettre l'objet `Utilisateur`.
  - Utiliser `putExtra` pour transmettre l'objet (rendre la classe sérialisable).

- **Activité de départ (`AccueilActivity`):**
  - La méthode `onActivityResult` gère le retour du boomerang.
  - Vérifier le code de retour.
  - Récupérer l'intent et l'extra.

```java
 ActivityResultLauncher<Intent> lanceur;

lanceur = registerForActivityResult(new ActivityResultContracts.StartActivityForResult(), new CallBackIdentification());

 private class CallBackIdentification implements ActivityResultCallback<ActivityResult> {
        @Override
        public void onActivityResult(ActivityResult result) {
            //c'est ici que le boomrang  va revenir
            if (result.getResultCode() == RESULT_OK) {
                user = (Utilisateur) result.getData().getSerializableExtra("user");
                salut.setText("Bonjour " + user.getNom() + user.getPrenom());
            }
        }
    }

    private class Ecouteur implements AdapterView.OnClickListener {
        @Override
        public void onClick(View v) {
            lanceur.launch(new Intent(AccueilActivity.this, IdentificationActivity.class));
        }
    }
```
```java
 private class Ecouteur implements AdapterView.OnClickListener {

        @Override
        public void onClick(View v) {
            if (v == confirmer){
                Intent retour = new Intent(IdentificationActivity.this, IdentificationActivity.class);
                //ceci fonctionne car nous avons serialized la class Utilisateur, plus tard on verra du Gson (json)
                retour.putExtra("user",new Utilisateur(champPrenom.getText().toString(),champNom.getText().toString()));
               //result ok veut dire qu'il n'y a pas eu de problem
                //setResultat et non start activity make sure que sa retourne dans l'acitivite et non une nouvelle activity
                setResult(RESULT_OK,retour);
                finish();
            }
        }
    }
```

### Problème avec la rotation de l'écran :
- Lorsque l'écran tourne, le cycle de vie est refait complètement, entraînant la perte de données.
- Utiliser `saveInstanceState` pour conserver des informations importantes pendant ces transitions.

## B) Cycle de vie :
- Références : [Cycle de vie des activités Android](https://developer.android.com/guide/components/activities/activity-lifecycle), [Article Medium](https://medium.com/@theabhishekavi/android-activity-lifecycle-9bc7de812dff)

### A-Solution : `saveInstanceState`
- Utiliser la méthode `onSaveInstanceState` pour sauvegarder des infos avant `onStop`.
- Conserve les infos dans la même session/processus.
- Utilisé pour conserver des informations temporaires.

### Méthodes utiles :
- `putSerializable`: Ajouter un objet sérialisable au Bundle.
- `getSerializable`: Récupérer un objet sérialisable depuis le Bundle.

### Astuce pour éviter des redémarrages inutiles :
- Modifier le fichier manifest pour spécifier que l'activité ne se redémarre pas dans certaines situations. Ceci est à ajouter dans le fichier manifest dans l'activite
  ```xml
 <activity
            android:name=".AccueilActivity"
            android:configChanges="orientation|screenSize|keyboard|keyboardHidden"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
 </activity>
``` 
B-Solution : Sérialisation
Si on veut conserver les infos au-delà de la session ou du processus courant.
Utiliser la sérialisation de l'objet, fichiers texte, ou une base de données.
Problème de fermeture d'application :
Si l'application est fermée, on perd les données.
Sérialiser l'objet Utilisateur pour conserver les informations même après la fermeture.
```java
finish();
```

Points à considérer :

## Où sérialiser ?
- La sérialisation peut être effectuée à l'endroit approprié dans le cycle de vie de l'application, tel que onPause() ou onStop(), pour garantir que les données sont sauvegardées avant la fermeture de l'application.

## Où désérialiser ?
- La désérialisation devrait avoir lieu au démarrage de l'application, par exemple dans la méthode onCreate(). Cela permet de restaurer les données sérialisées et de reconstituer l'objet Utilisateur avec les informations sauvegardées lors de la dernière exécution de l'application.

```java
public class MainActivity extends AppCompatActivity {
    private static Stock stock;
    SimpleAdapter simpleAdapter;
    Vector<HashMap<String, Object>> hmStock;
    Vector<VehiculeHyundai> inventaire;
    VehiculeHyundai pickedCar;
    Commande commande;

    ListView list;
    TextView panier;
    Button button;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        list = findViewById(R.id.listView);
        panier = findViewById(R.id.achatListeTexte);
        button = findViewById(R.id.commanderButton);

        stock = Stock.getInstance();
        stock.resetInventaire();
        inventaire = stock.getInventaire();
        hmStock = new Vector<>();

        for(VehiculeHyundai car:inventaire) {
            hmStock.add(
                    new HashMap(){{
                        put("nom", car.getNom());
                        put("alimentation", car.getAlimentation());
                        put("prix", car.getPrix());
                    }}
            );
        }

        simpleAdapter = new SimpleAdapter(
                this,
                hmStock,
                R.layout.layout_list,
                new String[]{"nom", "alimentation", "prix"},
                new int[]{R.id.carTitle, R.id.carType, R.id.price}
        );

        commande = new Commande(null);

        //SERIALIZE
        try {
            ObjectInputStream ois = null;
            FileInputStream fos = openFileInput("fichier.ser");
            ois = new ObjectInputStream(fos);
            commande.setVoitures((Vector<VehiculeHyundai>) ois.readObject());
            commande.setQteVoitures((int) ois.readObject());
            setPanier();
        } catch (NullPointerException np) {
            commande.setVoitures(new Vector<>());
            commande.setQteVoitures(0);

        } catch (Exception e) {
            throw new RuntimeException(e);
        }

        list.setAdapter(simpleAdapter);
        list.setOnItemClickListener((adapterView, view, pos, l) -> {

            pickedCar = stock.trouverObjet(
                    (String) hmStock.get(pos).get("nom"),
                    (String) hmStock.get(pos).get("alimentation"));

            if((Integer) pickedCar.getQte() > 0 && commande.getQteVoitures() <= 2) {
                commande.ajouterVoiture(pickedCar, pickedCar.getQte());
                panier.append(pickedCar.getNom() + " - " + pickedCar.getAlimentation() + '\n');
           }
        });

        button.setOnClickListener(v -> {
            panier.setText(commande.getPrixTotal().toString());
            resetApp();
        });
    }

    public void setPanier() {
        for (VehiculeHyundai car : commande.getVoitures()) {
            panier.append(car.getNom() + " - " + car.getAlimentation() + '\n');
            //resetApp();
        }
    }

    public void resetApp() {
        panier.setText("");
        stock.resetInventaire();

        ObjectOutputStream oos = null;
        try {
            FileOutputStream fos = this.openFileOutput("fichier.ser", Context.MODE_PRIVATE);
            oos = new ObjectOutputStream(fos);
            oos.flush();
        } catch(Exception e) {
            throw new RuntimeException(e);
        }
        finally {
            if(oos != null) {
                try {
                    oos.close();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }

    }

    @Override
    protected void onStop() {
        super.onStop();
        ObjectOutputStream oos = null;

        try {
            FileOutputStream fos = this.openFileOutput("fichier.ser", Context.MODE_PRIVATE);
            oos = new ObjectOutputStream(fos);
            oos.writeObject(commande.getVoitures());
            oos.writeObject(commande.getQteVoitures());
        } catch(Exception e) {
            throw new RuntimeException(e);
        }
        finally {
            if(oos != null) {
                try {
                    oos.close();
                } catch (IOException e) {
                    throw new RuntimeException(e);
                }
            }
        }
    }
}

```