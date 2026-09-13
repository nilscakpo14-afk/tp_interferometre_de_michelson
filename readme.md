# TP d'interférences à deux ondes

## Objectif

Etude de l'interféromètre de Michelson et détermination de la longueur d'onde d'un laser d'heliun-néon, de la raie verte et du doublet jaune d'une lampe Hg.

## Mesure de la longueur d'onde

Le déplacement du miroir mobile (M2) est noté `d` et le nombre de franges observées est noté `q`.

La longueur d'onde est déterminée à partir de la relation :

**λ = 2d / q**

## Mesure d'incertitudes et écart relatif (voir code python pour les formules)

-Incertitude liée a la répétition de l'expérience (*u_A, de la fonction uncertainty_A(), de fichier functions.py*)

-Ecart relatif de la valeur expérimentale a la théorie (*fonction relative_difference() du fichier functions.py*)

- Incertitude résultant du calcul de la longueur de cohérence :

$$
\Delta \lambda = \frac{\lambda_0^2}{c}\Delta \nu
$$

avec :

$$
L_c = \frac{c}{\Delta \nu}
$$

## Traitement des données

Les données expérimentales sont traitées avec Python.

Bibliothèques utilisées :

- NumPy
- Matplotlib
- SciPy

Le programme permet notamment de :

- calculer les différentes valeurs de la longueur d'onde;
- représenter graphiquement les résultats;
- exploiter les mesures expérimentales.

## Fichiers

- `TP_6_interference_a_deux_ondes.py` : traitement principal des données expérimentales.
- `functions.py` : fonctions utilisées pour l'exploitation des mesures.

## Auteur

Nils CAKPO  
Licence 3 Physique