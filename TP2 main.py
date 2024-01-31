# -*- coding: utf-8 -*-
"""
Ce module contient des fonctions pour le calcul d'intégrales numériques.

Ce fichier fournit des fonctions pour le calcul d'intégrales à l'aide de différentes méthodes, telles que la méthode des rectangles, la méthode des trapèzes et la méthode de Simpson.

Exemple
-------
Cet exemple illustre l'utilisation de ces fonctions pour le calcul d'intégrales :
    integrale_rectangle(0, 10, 4, 0)
    integrale_trapeze(0, 1, 0.1)
    integrale_simpson(0, 1, 0.1, 2)

Notes
-----
    Assurez-vous d'importer le module numpy avant d'utiliser ce fichier.

    Les fonctions de ce module supposent que la fonction à intégrer est définie dans la fonction 'fonction' du module.

    Les paramètres 'type' pour la méthode des rectangles doivent être 0, 1 ou 2.

    La fonction 'fonction_erreur' ajuste itérativement le pas jusqu'à ce que l'erreur soit inférieure à l'erreur spécifiée.

"""

################################################################################
#####                       Zone d'import des modules                      #####
################################################################################

import numpy as np

################################################################################
#####                   Zone de déclaration des fonctions                  #####
################################################################################

def cordes(fct, b_inf, b_sup, precision):
    """Cette fonction calcule la racine d'une équation à l'aide de la méthode de la corde.

    Paramètres
    ----------
    fct : function
        La fonction pour laquelle on souhaite trouver la racine.
    b_inf : float
        La borne inférieure de l'intervalle initial.
    b_sup : float
        La borne supérieure de l'intervalle initial.
    precision : float
        Erreur maximale entre la racine théorique et la racine réelle.        

    Retour
    ------
    float
        La valeur de la racine calculée.

    Exemple
    -------
    cordes(b_sup=1, b_inf=2, fct=lambda x: 0.51 * x - np.sin(x))
    """
    print("\n\nCalcul de la racine avec la méthode de la corde")
    precision = 10**(-4)
    n = 0
    m = 1  
    
    while abs(fct(m)) > precision:
        
        n = n + 1
        m = (b_inf*fct(b_sup)-b_sup*fct(b_inf))/(fct(b_sup)-fct(b_inf))
        b_inf = b_sup
        b_sup = m
        
    print(f"Valeur de la racine : {m}")
    print(f"Nombre de calcul nécessaire afin d'obtenir la précision voulue : {n}")
    return m

def dicotomie(fct, b_inf, b_sup, precision):
    """
    Calcule la racine d'une fonction à l'aide de la méthode de la dicotomie.

    Paramètres
    ----------
    fct : function
        La fonction pour laquelle la racine est calculée.
    b_inf : float
        La borne inférieure de l'intervalle initial.
    b_sup : float
        La borne supérieure de l'intervalle initial.
    precision : float
        Erreur maximale entre la racine théorique et la racine réelle.        

    Retour
    ------
    float
        La valeur de la racine calculée.

    Exemple
    -------
    dicotomie(b_sup=1, b_inf=2, fct=lambda x: 0.51 * x - np.sin(x))
    """    
    print("\n\nCalcul de la racine avec la méthode de la dicotomie")    
    precision = 10**(-4)
    n = 0
    m = 1
    
    while abs(fct(m)) > precision:       
        m = (b_inf+b_sup)/2
        g = fct(b_inf)
        d = fct(m)    
        n = n + 1
        if g*d <= 0:
            b_sup = m   
        else:
            b_inf = m
    
    print(f"Valeur de la racine : {m}")
    print(f"Nombre de calcul nécessaire afin d'obtenir la précision voulue : {n}")
    return m
    
def newton(fct, dfct, val, precision):
    """Cette fonction calcule la racine d'une équation à l'aide de la méthode de Newton.

    Paramètres
    ----------
    fct : function
        La fonction pour laquelle la racine est recherchée.
    dfct : function
        La dérivée de la fonction fct.
    val : float
        La valeur initiale pour l'itération.
    precision : float
        Erreur maximale entre la racine théorique et la racine réelle.        

    Retour
    ------
    float
        La valeur de la racine calculée.

    Exemple
    -------
    newton(val=1, fct=lambda x: (1 - 0.61 * x) / x, dfct=lambda x: -(1-0.61*x)/x**2-0.61/x)
    """    
    print("\n\nCalcul de la racine avec la méthode de Newton") 
    precision = 10**(-4)
    n = 0
    m = 1

    while abs(fct(m)) > precision:
        n = n + 1
        m = val-fct(val)/dfct(val)
        val = m
                
    
    print(f"Valeur de la racine : {m}")
    print(f"Nombre de calcul nécessaire afin d'obtenir la précision voulue : {n}")
    return m
    
def secante(fct, b_inf, b_sup, precision):
    """Cette fonction calcule la racine d'une équation à l'aide de la méthode de la sécante.

    Paramètres
    ----------
    fct : function
        La fonction pour laquelle on cherche la racine.
    b_inf : float
        La borne inférieure de l'intervalle initial.
    b_sup : float
        La borne supérieure de l'intervalle initial.
    precision : float
        Erreur maximale entre la racine théorique et la racine réelle.        

    Retours
    -------
    float
        La valeur de la racine trouvée.

    Exemple
    -------
    secante(b_sup=1, b_inf=2, fct=lambda x: 0.51 * x - np.sin(x))
    """
    print("\n\nCalcul de la racine avec la méthode de la sécante") 
    precision = 10**(-4)
    n = 0
    m = 1
    while abs(fct(m)) > precision:
        n = n + 1
        m = b_sup-(b_sup-b_inf)*fct(b_sup)/(fct(b_sup)-fct(b_inf))
        b_inf  = b_sup 
        b_sup = m
    print(f"Valeur de la racine : {m}")
    print(f"Nombre de calcul nécessaire afin d'obtenir la précision voulue : {n}")
    return m
    
def fausse_position(fct, b_inf, b_sup, precision):
    """
    Calcule la racine d'une fonction à l'aide de la méthode de la fausse position.

    Paramètres
    ----------
    fct : function
        La fonction pour laquelle on souhaite trouver la racine.
    b_inf : float
        La borne inférieure de l'intervalle de recherche.
    b_sup : float
        La borne supérieure de l'intervalle de recherche.
    precision : float
        Erreur maximale entre la racine théorique et la racine réelle.

    Retours
    -------
    float
        La valeur de la racine calculée.

    Exemple
    -------
    fausse_position(b_sup=1, b_inf=2, fct=lambda x: 0.51 * x - np.sin(x))
    """
        # Print the value of the fct parameter
    # print(f'The value of fct is: {fct.}')
    print("\n\nCalcul de la racine avec la méthode de la fausse position") 
    precision = 10**(-4)
    n = 0
    m = 1
    
    while abs(fct(m)) > precision:
        
        m = b_inf - ((b_sup-b_inf)/(fct(b_sup)-fct(b_inf)))*fct(b_inf)  
        n = n + 1
        if fct(b_inf)*fct(m) <= 0:
            b_sup = m  
        else:
            b_inf = m
        
    print(f"Valeur de la racine : {m}")
    print(f"Nombre de calcul nécessaire afin d'obtenir la précision voulue : {n}")
    return m

################################################################################
#####                  Zone d'éxécution du programme/test                  #####
################################################################################
if __name__ == "__main__" :
    print("\n\nÉxécution du fichier main.py \n\n")   
    
     
    ######### Rappel #########
    # il est important de définir la dérivée (dfct pour newton) 
    
    ######### Fonction / Dérivés #########
    # fct=lambda x: x**2-2, dfct=lambda x:2*x
    # fct=lambda x: 0.51 * x - np.sin(x)), dfct=lambda x:
    # fct=lambda x: (1 - 0.61 * x) / x, dfct=lambda x: -(1-0.61*x)/x**2-0.61/x)
    # fct=lambda x: np.exp(x ** 2) - 56 * np.exp(-2 * x ** 2), dfct=lambda x:
    
    
    ######### Partie 1 #########
    print("Question 1")
    print("Une fonction qui a pour racine : racine de 2 peut etre :")
    print("f(x)=x**2-2")

    cordes(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: x**2-2)
    print("----------------")
    dicotomie(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: x**2-2)
    print("----------------")
    newton(val=2, precision = 10**(-4), fct=lambda x: x**2-2, dfct=lambda x:2*x)
    print("----------------")
    secante(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: x**2-2)
    print("----------------")
    fausse_position(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: x**2-2)

    # fausse_position(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: 0.51 * x - np.sin(x))
    # print("----------------")
    # secante(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: 0.51 * x - np.sin(x))
    # print("----------------")
    # newton(val=1, precision = 10**(-4), fct=lambda x: (1 - 0.61 * x) / x, dfct=lambda x: -(1-0.61*x)/x**2-0.61/x)
    
    # fausse_position(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: x**2-2)
    
    # secante(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: np.exp(x ** 2) - 56 * np.exp(-2 * x ** 2))