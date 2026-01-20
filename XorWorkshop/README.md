# Atelier de Cryptographie: Comprendre le XOR et ses faiblesses

Pour cet atelier, il vous suffit de suivre le **README** est de faire les défis qui vous intéresse. L'enjeu de l'atelier se trouve dans les défis 1 et 2 associés au XOR. Pour ces deux challenges, vous pouvez les initialiser avec les fichiers **/_create.py** (normalement ce n'est pas nécessaire) et des solutions sont proposées dans les fichiers **/_in_work.py**. 

Ces solutions sont une simple proposition et il y a évidemment différentes façons de faire.

## 1. Petit historique du chiffrement

### Chiffrement de César

Le chiffrement de César est l’un des plus anciens algorithmes de chiffrement connus.  
Il doit son nom à **Jules César**, qui l’utilisait pour envoyer des messages militaires.  
Le principe : **décaler chaque lettre de l’alphabet d’un nombre fixe**, par exemple +3.

Exemple (décalage de 3) :  
- Message : `PONY`  
- Alphabet décalé : P→S, O→R, N→Q, Y→B  
- Message chiffré : `SRQB`

C’est très simple à comprendre… mais aussi très simple à casser.  

#### Exercice
Voici un message chiffré :  **KHOOR ZRUOG**

Essayez de :
1. Trouver la clé (le décalage).  
2. Retrouver le message en clair.

Une fois que vous avez réussi, demandez-vous :

**Quel est le moyen le plus efficace de casser un chiffrement de César ?**  
*(Indice : raisonnez en “modulo 26” et pensez à l’espace de clé…)*  

Petit défi: Faire un petit programme avec la longueur d'alphabet que vous souhaitez pour brute-forcer une clé.

### Chiffrement de Vigenère

Le chiffrement de **Vigenère** est une amélioration du chiffre de César.  
Plutôt que d'utiliser **un seul décalage**, il utilise une **suite de décalages**, définie par une **clé composée de plusieurs lettres**.  
On parle alors de **substitution poly-alphabétique** : chaque lettre du message est chiffrée avec un alphabet différent.

Ce chiffrement, longtemps considéré comme “incassable”, a résisté pendant **plus de 300 ans** avant que des méthodes d’analyse ne permettent de le casser.

#### Comment ça marche ?

1. On répète la **clé** autant de fois que nécessaire pour qu’elle fasse la même longueur que le message.
2. Chaque lettre du message est décalée selon la **lettre correspondante de la clé**.
   - Exemple :  
     - Clé : **K** → 10 (si A=0, B=1, ..., K=10)  
     - On décale donc la lettre du message de **10 positions** dans l’alphabet.

Tout se fait en **modulo 26** pour “boucler” dans l'alphabet. (ou plus généralement modulo n avec la taille de votre alphabet)

#### Déchiffrer ?  
On fait simplement l’inverse : on **retire** la valeur de la clé au lieu de l’ajouter.

### Casser Vigenère : possible… mais plus subtil

Même si Vigenère est plus solide que César, il devient vulnérable si :
- la **clé est courte**,  
- le **message est long**,  
- et surtout si la **même clé est réutilisée**.

Voici les trois techniques classiques :

#### Kasiski (trouver la longueur de la clé)

On cherche des **séquences répétées** dans le texte chiffré.  
Si elles se répètent à des positions régulières, elles ont probablement été chiffrées avec la **même portion de la clé**.

Les distances entre ces répétitions donnent souvent…  
**un multiple de la longueur de la clé**.

#### Analyse de fréquence (identifier les décalages)

Une fois la longueur de la clé trouvée :
- on découpe le texte en **sous-textes** (un pour chaque position de la clé),
- chaque sous-texte est en réalité… un **César** déguisé !
- on regarde quelle lettre est la plus fréquente → souvent un équivalent du **E** en anglais ou du **E**/**A** en français.

On en déduit la valeur de chaque lettre de la clé.

#### Bruteforce (si la clé est courte)

Si la clé fait 3 lettres ou moins…  
**Il suffit de tester toutes les combinaisons**.  
Très vite cassé aujourd’hui.

#### Petit défi (Falcutatif)
Appliquer les méthodes **1 et 2** sur *VigCipherText.txt* que vous pouvez trouver dans le dossier VigenereDefi.

## 2. Ce qui définit un bon chiffrement moderne
- Résistance même face à de très grands moyens de calcul  
- Pas de fuite d’information  
- Résultat indiscernable du hasard  
- Sûr même avec du clair connu  
- Étudié publiquement  

## 3. Symétrique vs Asymétrique

### Symétrique
- Une seule clé (ex : AES, ChaCha20)
- Très rapide
- Clé à partager secrètement

### Asymétrique
- Clé publique / clé privée (ex : RSA, ECC)
- Pratique mais plus lent

## 4. Le XOR : simple, puissant, dangereux

L’opérateur XOR (⊕) est l’un des outils les plus fondamentaux de la cryptographie moderne.  
Il est simple, rapide, réversible, mais peut devenir **extrêmement dangereux** s’il est mal utilisé… notamment en cas de **réutilisation de clé**.

### Propriétés de l’opérateur XOR

Le XOR est une opération binaire qui renvoie **1 si les deux bits sont différents**, **0 s’ils sont identiques**.

Voici ses propriétés essentielles (et très utiles en crypto) :

**1. Commutatif**  
`A ⊕ B = B ⊕ A`

**2. Associatif**  
`A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C`

**3. Élément neutre : 0**  
`A ⊕ 0 = A`

**4. Auto-inverse**  
`A ⊕ A = 0`

**5. Inversibilité parfaite**  
Si tu connais deux éléments dans l’équation :

```
C = P ⊕ K
```

Tu peux retrouver le troisième :

- retrouver le message : `P = C ⊕ K`  
- retrouver la clé : `K = C ⊕ P`

C’est **cette inversibilité parfaite** qui fait du XOR un outil extrêmement utilisé en cryptographie.

### Utilisation en chiffrement

Un chiffrement par XOR chiffre chaque octet ainsi :

```
cipher[i] = plaintext[i] XOR key[i]
```

Si la clé est **au moins aussi longue que le message** et **jamais réutilisée**, on obtient un chiffrement parfait :

➡ **le One-Time Pad (OTP)** — *mathématiquement incassable*.

### Mais attention : la réutilisation de clé est catastrophique

Si deux messages `P1` et `P2` sont chiffrés avec la **même clé** `K`, alors :

```
C1 = P1 ⊕ K
C2 = P2 ⊕ K
```

On peut faire :

```
C1 ⊕ C2 = (P1 ⊕ K) ⊕ (P2 ⊕ K)
        = P1 ⊕ P2 ⊕ K ⊕ K
        = P1 ⊕ P2
```

➡ **La clé disparaît…**  
➡ **Et on obtient directement le XOR des deux messages en clair !**

Cela permet très souvent de retrouver `P1` et `P2`, surtout si :

- on a des hypothèses sur leur contenu (mots probables, ASCII),
- les messages ont un format prévisible,
- on devine l'emplacement des espaces ou ponctuations.

C’est le cœur du **défi 1**.

### Longueur de clé : courte = failles, longue = sécurité

- Une **clé courte** ⇒ elle se répète ⇒ motifs ⇒ vulnérable.  
- Une **clé plus longue que le message** ⇒ très bonne sécurité.  
- Une **clé vraiment aléatoire, utilisée une seule fois** ⇒ sécurité parfaite (**OTP**).

Les systèmes modernes (AES, TLS, SSH…) évitent la réutilisation d’un même flux XOR grâce à :

- des IV,
- des nonces,
- des compteurs,
- du salage cryptographique.

C'est le cœur du **défi 2**




