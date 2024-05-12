
# Python Scripts for Reading and Analyzing Text Files

This document outlines two Python scripts that demonstrate how to read from text files and perform basic text analysis, including counting lines, words, characters, and occurrences of a specific substring.

## Script 1: Basic File Reading

### Function: `lire`

- **Purpose**: Opens and reads a text file, then returns its content.
- **Parameters**:
  - `chemin`: File path.
  - `encodage`: Encoding of the file.

```python
def lire(chemin, encodage):
    f = open(chemin, 'r', encoding=encodage)
    print(f.encoding)
    texte = f.read()
    f.close()
    return texte
```

### Main Execution

- Retrieves the file path and encoding from command line arguments and prints the file's content.

```python
def main():
    chemin = argv[1]
    encodage = argv[2]
    texte = lire(chemin, encodage)
    print(texte)
    return 0

if __name__ == '__main__':
    main()
```

## Script 2: Advanced Text Analysis

### Function: `lire`

- Same as above but converts text to lower case for uniform analysis.

```python
def lire(chemin, encodage):
    f = open(chemin, 'r', encoding=encodage)
    texte = f.read()
    f.close()
    return texte.lower()
```

### Text Analysis Functions

- **Count Lines**: Counts the number of lines in the text.
- **Count Characters**: Counts non-space characters.
- **Count Words**: Counts words based on word boundaries.
- **Count Substrings**: Counts occurrences of a specified substring.

```python
def compter_lignes(texte):
    return len(re.findall('[^\n]+', texte))

def compter_caracteres(texte):
    return len(re.findall('\S', texte))

def compter_mots(texte):
    return len(re.findall('\w+', texte))

def compter_souschaines(texte, souschaine):
    return len(re.findall(souschaine.lower(), texte))
```

### Main Execution

- Extends the first script to include functions that count lines, characters, words, and substrings based on command line input.

```python
def main():
    chemin = argv[1]
    encodage = argv[2]
    souschaine = argv[3]
    texte = lire(chemin, encodage)
    print(f'Il y a {compter_lignes(texte)} lignes dans le texte.')
    print(f'Il y a {compter_caracteres(texte)} caractÃ¨res dans le texte.')
    print(f'Il y a {compter_mots(texte)} mots dans le texte.')
    print(f'Il y a {compter_souschaines(texte, souschaine)} occurrences de "{souschaine}" dans le texte.')
    return 0

if __name__ == '__main__':
    main()
```

These scripts offer a straightforward way to read text data and perform basic analysis, suitable for tasks like data preprocessing, text mining, and more.
