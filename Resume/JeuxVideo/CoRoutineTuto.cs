using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CoRoutineTuto : MonoBehaviour
{
    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine(TestDisplayDEbug());
    }

    // Update is called once per frame
    void Update()
    {
        if (Input.GetKeyUp(KeyCode.Escape))
        {
            StopCoroutine(TestDisplayDEbug());
        }
    }

    IEnumerator TestDisplayDEbug()
    {
        // nous avons le droit lors de multitraid de mettre un while true
        while (true)
        {
            Debug.Log("je vais attendre un peu");
            yield return new WaitForSeconds(1.0f);
            Debug.Log("cetais long ");
        }

       

        //autant que nous voulons
        Debug.Log("woy");
        yield return new WaitForSeconds(1.0f);
        Debug.Log("czi");
    }
}
