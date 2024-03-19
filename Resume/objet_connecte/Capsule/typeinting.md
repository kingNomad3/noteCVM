# annotation de type

La raison pk on a des types dans les codes comme int ou string, c'est un moyen d'aider les developpeur a deboger nos code
par exemple le code attendait un int mais un string lui a ete donner


from types import NoneType

```python
#<3.9
from typing import List,Tuple,Dict,Set
nl : List[int] = [1,2,3]
n2 : Tuple[int,str,flaot] = [1,"allo",3.14]
n3 : Dict[int,str] = [1:"allo"]
```

```python
vit: float = Allo()
    hint

def(vit:int,v2:str='') -> None:
```

None est comme true or false est un NoneType, n'est pas un type None est une instance de NoneType et NonType est un type

```python
#<=3.9
# from typing import List,Tuple,Dict,Set
nl : list[int] = [1,2,3]
n2 : tuple[int,str,flaot] = [1,"allo",3.14]
n3 : dict[int,str] = [1:"allo"]


def scan_moy(values: list[float]) -> tuple[flaot,float]:
# ...
```


```python
# oernet de defubur un paranettre ayant n'import quel type
from typing import Any
a: Any = 1
a: 3.14
a: Tower()
a: "allo"
```

```python
# < 3.10
from typing import Union

nombre : Union[int,float] = 3

nombre = 3.14


# 3.10
from typing import Union

nombre : int|float = 3

nombre = 3.14
```

```python
from typing import Optional

value : Optional[int] = None 

#3.10
value: int|None = 3
```

```python
from typing import Callable

def f(i:int, r:float)->complex:

task:Callable[[int,float],complex] = f

isinstance(a,(...))
callable(f) # c minuscule, retourne f is elle est callable 
```


```python
from typing import Iterable
def show(values:Iterable[int|float]):
    for v in values
        print(v-3)
```

```python
# 1
#aliace de type
Data qty = list[int|float]

qt1: list[int|float] = [1,2,3]
qt2:     = [3,5]
```

```python
# 3.8
from typing import Literal

var : Literal['red', ]= 'red', 'green', 'blue'
```

```python
# resoud les dependance circulaire 

class Tower:
    def __init__()
        ...

    def compare(other:Tower) -> bool:
        ...

#le compilateur de sait pas que Tower exist le tower dans compare depend de la class tower
#depuis 3.7 

 def compare(other:'Tower') -> bool:

#foward declaration, annonce que cela va exister plus tard 


#autre exemple 

class A:
    def f()->B

#on peut mettre B avant a et le problem est regler 
class B:
    defg()->None

#mais si
class A:
    def f()->B

#on peut mettre B avant a
class B:
    defg()->A

#alors
class A:
    def f()->'B'

#on peut mettre B avant a
class B:
    defg()->A

# nouveaute
# prevoir dans le futur 
from __future__ import Annonation # doit etre la premiere ligne de code 

#plus besoin des  ''
class A:
    def f()->B

#on peut mettre B avant a
class B:
    defg()->A

```

```python
#etat  courrant 
from typing import TYPE_CHECKING

#un fichier
a.py[
from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from b import B
        
    class a:
        def f()->B


]

#u autre fichier
b.py[
from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from a import A
    class b:
        def f(v:B)->a
        return v


]


```


# personnelle
    - NewType
    - TypeVar
    - Annonated
    - Generic






__defaults__
__annotations__ : les informations d'annotations (typeHinting) int, str None