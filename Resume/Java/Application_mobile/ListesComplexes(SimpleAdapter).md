# Notes sur les Listes Complexes avec SimpleAdapter


##  Utilisation d'un SimpleAdapter :
Habituellement, on utilise un ArrayAdapter pour remplir un ListView.
Pour un ListView composé d'items plus complexes, on doit utiliser un SimpleAdapter.

Paramètres du SimpleAdapter :
```java
public SimpleAdapter(Context context, List<? extends Map<String, ?>> data, int resource, String[] from, int[] to)
```
- context : Le contexte dans lequel la vue associée à ce SimpleAdapter s'exécute.
- data : Une liste de Map. Chaque entrée correspond à une ligne de la liste.
- resource : Identifiant de ressource d'une disposition de vue qui définit les vues pour cet élément de liste.
- from : Une liste de noms de colonnes ajoutés à la carte associée à chaque élément.
- to : Les vues qui doivent afficher la colonne dans le paramètre from.
## Paramètre "data" de SimpleAdapter :

 - Le 2e paramètre "data" doit contenir les données à afficher dans la liste, sous forme de List de Maps.
Questions :
- Quelle est la collection qui met en œuvre l'interface List ?
    - Réponse : List.
- Quelle est la collection qui met en œuvre l'interface Map ?
    - Réponse : HashMap.
## Organisation des Données :
- Les données doivent être déposées dans une collection de collections, où la collection parent représente les items et la collection enfant représente les informations d'une chanson.


``` java
public class MainActivity extends AppCompatActivity {
    TextView palmares;
    TextView date;
    TextView nomChanson;
    ImageView image;

    ListView liste;

    String [] params = {"palmares","nomChanson","date","image"};
    int [] id = {R.id.palmares,R.id.date,R.id.nomChanson,R.id.image};

    Vector<Hashtable<String,Object>> Map;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        liste =  findViewById(R.id.liste);

        Map = rempl   ir();

        SimpleAdapter Sadapt = new SimpleAdapter(this,Map,R.layout.liste_textview,params,id);
        liste.setAdapter(Sadapt);
    }

    public Vector<Hashtable<String,Object>> remplir(){
        Vector<Hashtable<String,Object>> v = new Vector();

        Hashtable<String,Object>  h = new Hashtable();
        h.put("palmares",3);
        h.put("nomChanson","touch me");
        h.put("date","22/03/86");
        h.put("image", R.drawable.touchme);
        v.add(h);

        h = new Hashtable();
        h.put("palmares",8);
        h.put("nomChanson","nothing is gonna stop me now  ");
        h.put("image", R.drawable.nothing);
        v.add(h);

        h = new Hashtable();
        h.put("palmares",31);
        h.put("nomChanson","Santa Maria");
        h.put("date","28/03/1998");
        h.put("image", R.drawable.santamaria);
        v.add(h);

        h = new Hashtable();
        h.put("palmares",108);
        h.put("nomChanson","Hot boy");
        h.put("date","10/04/2018");
        h.put("image", R.drawable.hotboy);
        v.add(h);

        return v;
    }
}
```

```java
public class MainActivity extends AppCompatActivity {

    ImageView imageView;
    Spinner spinner;

    Groupe[] liste = {new Groupe ("c23", R.drawable.c23),new Groupe("c34", R.drawable.c34),new Groupe("c44", R.drawable.c44)  };
    Groupe groupeSelect;
    Boolean firstEntry;

    int index;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        imageView = findViewById(R.id.imageView);
        spinner = findViewById(R.id.spinner);

        Vector<String> vec = new Vector<>();
        for ( Groupe g : liste)
        {
            vec.add(g.getNomCours());
        }


        ArrayAdapter adapter = new ArrayAdapter(this, android.R.layout.simple_list_item_1,vec );
        spinner.setAdapter(adapter);

        setImage();
        firstEntry = true;

        Ecouteur ec = new Ecouteur();
        spinner.setOnItemSelectedListener(ec);

    }
    private class Ecouteur implements AdapterView.OnItemSelectedListener
    {

        @Override
        public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
            ObjectOutputStream oos;
            index = position;
            if (firstEntry == false){
                try{
                    groupeSelect = liste[position];
                    FileOutputStream fos = openFileOutput("fichier.ser", Context.MODE_PRIVATE);
                    oos = new ObjectOutputStream(fos);
                    oos.writeObject(groupeSelect);
                    oos.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            setImage();
            firstEntry = false;
        }

        @Override
        public void onNothingSelected(AdapterView<?> parent) {

        }
    }

    private void setImage(){
        try{
            FileInputStream fis = openFileInput("fichier.ser");
            ObjectInputStream ois = new ObjectInputStream(fis);
            groupeSelect = (Groupe)(ois.readObject());
            imageView.setImageResource(groupeSelect.getAdresseImage());
            ois.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        } catch (IOException e) {
            e.printStackTrace();
        } catch (ClassNotFoundException e) {
            throw new RuntimeException(e);
        }
    }
}
```