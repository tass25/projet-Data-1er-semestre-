# 🫀 Heart Attack Analysis & Prediction 🫀

Bienvenue dans le projet **Heart Attack Analysis & Prediction** ! Ce projet vise à développer un modèle de classification capable de prédire la probabilité d'une crise cardiaque chez un patient en se basant sur des paramètres cliniques. 

## Contexte 📚

La maladie cardiaque représente une préoccupation majeure de santé publique à l'échelle mondiale. La détection précoce et la prévention sont essentielles pour améliorer les résultats pour les patients. Ce projet utilise l'apprentissage automatique pour identifier les individus à risque.

## 🎯 Objectif du Projet

Développer un modèle fiable capable de prédire le risque de crise cardiaque, permettant ainsi aux professionnels de la santé d'intervenir précocement et de réduire les risques.

## 🛠️ Description du Modèle

Le modèle est basé sur des techniques d'apprentissage automatique et sera déployé sur le cloud via **Streamlit**. Nous allons utiliser **trois modèles différents** pour les comparer et déterminer le meilleur en fonction de leurs performances.

## 🖼️ Aperçu de l’Application

Voici un aperçu de l’interface Streamlit :

![Aperçu interface 1](SH1.png)
*Figure 1 – Interface de l’application*

![Aperçu interface 2](SH2.png)
*Figure 2 – Interface de l’application *

## 🔍 Spécifications Fonctionnelles

### **Entrées**

Pour évaluer le risque d'accident cardiaque, le modèle nécessite les informations suivantes :

- **Âge** : Âge du patient
- **Sexe** : 1 = masculin, 0 = féminin
- **Type de douleur thoracique (cp)** :
  - 0 : asymptomatique
  - 1 : angine atypique
  - 2 : douleur non-anginale
  - 3 : angine typique
- **Pression artérielle au repos (trestbps)** : Pression (mm Hg)
- **Cholestérol (chol)** : En mg/dl
- **Sucre sanguin à jeun (fbs)** : 1 = vrai, 0 = faux
- **Électrocardiogramme au repos (restecg)** :
  - 0 : hypertrophie ventriculaire gauche
  - 1 : normal
  - 2 : anomalie ST-T
- **Fréquence cardiaque maximale (thalach)** : Fréquence maximale
- **Angine induite par l'exercice (exang)** : 1 = oui, 0 = non
- **Ancienneté de la dépression ST (oldpeak)** : Dépression ST induite par l'exercice
- **Pente (slope)** : 0 = vers le bas, 1 = plat, 2 = vers le haut
- **Vaisseaux majeurs (ca)** : Nombre de vaisseaux (0-3)
- **Thalassémie (thal)** :
  - 0 : NULL
  - 1 : défaut fixe
  - 2 : flux sanguin normal
  - 3 : défaut réversible
- **Cible (target)** : 1 = non, 0 = oui

### **Sorties**

Le modèle fournira une prédiction indiquant si le patient est à risque de crise cardiaque.

## 💻 Spécifications Techniques

### **Outils et Technologies**

- **Langage de programmation** : Python
- **Framework** : Streamlit
- **Environnement** : VSCODE
- **Bibliothèques** : 
  - Pandas
  - Matplotlib
  - Seaborn
  - Scikit-learn
  - XGBoost

### **Flux de Travail**

1. **Traitement des Données**
2. **Analyse Exploratoire des Données (EDA)**
3. **Ingénierie des Caractéristiques**
4. **Normalisation et Mise à l'échelle**
5. **Sélection et Évaluation du Modèle** (quatre modèles pour comparaison)
6. **Test du Modèle**
7. **Déploiement du Modèle**

## 📊 Suivi et Évaluation

Le succès sera mesuré par :

- **Précision**
- **AUC (Area Under Curve)**
- **Temps de réponse**

## 🔮 Plan de Développement Futur

- Utilisation de pipelines
- Exploration de méthodes de sélection de caractéristiques
- Traitement des valeurs aberrantes

## 🔗 Liens Utiles

- Dataset : https://archive.ics.uci.edu/dataset/45/heart+disease
