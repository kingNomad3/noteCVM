# Animator

Window
Package nmanager
Window asset store search oline 

controle a select all for eample images to poin to point
Un petit caree dans unity c'est 1 mettre

Window
aniamtion


clip
create new clip
control a et drag drop animation 
ctrl a sur les cle pour les espaces

![Keyfranes](./image/Screenshot%202024-02-18%20135852.png)


Window 
Animator
cette fenetre devrait apparatre 
![Keyfranes](./image/Screenshot%202024-02-18%20140517.png)
 delete all the squares except any states et entry


Add a new float
![Keyfranes](./image/Screenshot%202024-02-18%20141006.png)


right click dans le vide du animator
create state from new entry
![Keyfranes](./image/Screenshot%202024-02-18%20141751.png)

double click on it 
![Keyfranes](./image/Screenshot%202024-02-18%20143825.png)

a coter de lay clock parameter 
double click on blend par defaut 

![Keyfranes](./image/Screenshot%202024-02-18%20143945.png)

click sur le bland tree and change blend type pour any 2d you will see your parametere
+ add motion feel x4
drag and drop the animation there

linear drag (comme viscosite)

```C#
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

[RequireComponent(typeof(Animator))]
[RequireComponent (typeof(Rigidbody2D))]
public class ControlRobin : MonoBehaviour
{
    private Animator AnimatorRobin;
    private Rigidbody2D Rigidbody;
    private float ControlX;
    private float ControlY;

    [SerializeField]
    private float QteForce;
    [SerializeField]
    private float VitesseMaximum;

    // Start is called before the first frame update
    void Start()
    {
        AnimatorRobin = GetComponent<Animator>();
        Rigidbody = GetComponent<Rigidbody2D>();
    }

    // Update is called once per frame
    void Update()
    {
        ControlX = Input.GetAxis("Horizontal");
        ControlY =  Input.GetAxis("Vertical");
        AnimatorRobin.SetFloat("MovementX", ControlX);
        AnimatorRobin.SetFloat("MouvementY", ControlY);
    }

    private void FixedUpdate()
    {
        float VitesseActuelle = Rigidbody.velocity.magnitude; // longueur de la fleche
        if(VitesseActuelle < VitesseMaximum){
            Rigidbody.AddForce(new Vector2(ControlX, ControlY) * QteForce);
        }
    }
}
```