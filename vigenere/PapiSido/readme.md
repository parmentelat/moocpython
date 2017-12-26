Mes propositions pour Vigenere

**version 0** , brut de décoffrage à partir de ce que j'avais fait à l'époque - adaptation minimale à partir de la ligne 57, je n'ai pas touché au reste surabondant pour l'instant, mais je suis prêt à "attaquer" un code  
Prochaine étape: rendre plus pythonique ( vous avez deviné, je viens de java ... ) et suivre les consignes du cours

**version 1** , ma proposition raisonnablement pythonisé. Je n'ai toutefois pas pu ( ou su ? ) me passer des indices pour suivre la progression dans la clé. Par contre j'ai laissé la possibilité par la variable "mode" de travailler en majuscule ou en minuscule, et préparé leterrain pour d'autres modes ( majuscule et minuscule mélangé, ma prochaine étape, voire plus tard caractère accentués, ponctuation etc... ).

**version 2**, version objet Vigenere( mode,cle) faire help(Vigenere) pour plus de détails( mode majuscule et minuscule mélangé et mode cyrillique mis en place - merci UTF-8). Prochaine étape lever une exception si la cle ne correspond paa au mode et pouvoir coder et décoder un message dooné dans un fichier texte 
