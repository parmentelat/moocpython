# Le code Vigenere

Je vous propose un exercice qui consiste à implémenter [le code de chiffrement de Vigenère](https://fr.wikipedia.org/wiki/Chiffre_de_Vigen%C3%A8re).

Quelques consignes supplémentaires

* on ne considère que des messages qui contiennent des minuscules ou de la ponctuation;
  la ponctuation est préservée telle quelle
* on veut une fonction pour coder et une autre pour décoder

### Exemple

```
$ python3
Python 3.6.3 (default, Oct  4 2017, 06:09:15)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from vigenere import encode, decode
>>> encode("j'adore écouter la radio toute la journee", "musique")
"v'sleli éuwknid di lepcg jiyfy tq naojvuy"
>>> decode("v'sleli éuwknid di lepcg jiyfy tq naojvuy", "musique")
"j'adore écouter la radio toute la journee"
```

### Améliorations possibles

* prendre en compte également les caractères majuscules
* transformer le code en une classe

```
$ python3
Python 3.6.3 (default, Oct  4 2017, 06:09:15)
[GCC 4.2.1 Compatible Apple LLVM 9.0.0 (clang-900.0.37)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from vigenere import Vigenere
>>> codec = Vigenere("musique")
>>> codec.encode("j'adore écouter la radio toute la journee")
"v'sleli éuwknid di lepcg jiyfy tq naojvuy"
>>> codec.decode("v'sleli éuwknid di lepcg jiyfy tq naojvuy")
"j'adore écouter la radio toute la journee"
```
