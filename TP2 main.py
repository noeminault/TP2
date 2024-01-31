# -*- coding: utf-8 -*-
"""
Ce module contient des fonctions pour le calcul de racine dans un intervalle donnée avec une précision donnée.

Ce fichier fournit des fonctions pour le calcul de racines à l'aide de différentes méthodes, telles que la méthode des cordes, de la dicotomie, de Newton, de la secante et de la fausse position.

Exemple
-------
Cet exemple illustre l'utilisation de ces fonctions pour le calcul de racines :
    newton(val=1, fct=lambda x: (1 - 0.61 * x) / x, dfct=lambda x: -(1-0.61*x)/x**2-0.61/x)
    fausse_position(b_sup=1, b_inf=2, fct=lambda x: 0.51 * x - np.sin(x))
    racine_all_method(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: x**2-2, dfct=lambda x:2*x)

Notes
-----
    Assurez-vous d'importer le module numpy avant d'utiliser ce fichier.

    L'utilisation de la dérivée de la fonction est nécessaire seulement pour la méthode de Newton.

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
    n = 0
    m = 1  
    
    while abs(fct(m)) > precision:
        
        n = n + 1
        m = (b_inf*fct(b_sup)-b_sup*fct(b_inf))/(fct(b_sup)-fct(b_inf))
        b_inf = b_sup
        b_sup = m
        
    print(f"Valeur de la racine tronquée à 10^-5 : {m:.5f} et valeur de f(racine) : {fct(m):.0e}")
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
    
    print(f"Valeur de la racine tronquée à 10^-5 : {m:.5f} et valeur de f(racine) : {fct(m):.0e}")
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
    n = 0
    m = 1

    while abs(fct(m)) > precision:
        n = n + 1
        m = val-fct(val)/dfct(val)
        val = m
                
    
    print(f"Valeur de la racine tronquée à 10^-5 : {m:.5f} et valeur de f(racine) : {fct(m):.0e}")
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
    n = 0
    m = 1
    while abs(fct(m)) > precision:
        n = n + 1
        m = b_sup-(b_sup-b_inf)*fct(b_sup)/(fct(b_sup)-fct(b_inf))
        b_inf  = b_sup 
        b_sup = m
    print(f"Valeur de la racine tronquée à 10^-5 : {m:.5f} et valeur de f(racine) : {fct(m):.0e}")
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
    print("\n\nCalcul de la racine avec la méthode de la fausse position") 
    n = 0
    m = 1
    
    while abs(fct(m)) > precision:
        
        m = b_inf - ((b_sup-b_inf)/(fct(b_sup)-fct(b_inf)))*fct(b_inf)  
        n = n + 1
        if fct(b_inf)*fct(m) <= 0:
            b_sup = m  
        else:
            b_inf = m
        
    print(f"Valeur de la racine tronquée à 10^-5 : {m:.5f} et valeur de f(racine) : {fct(m):.0e}")
    print(f"Nombre de calcul nécessaire afin d'obtenir la précision voulue : {n}")
    return m

def racine_all_method(fct, dfct, b_inf, b_sup, precision):
    """Cette fonction effectue plusieurs méthodes de recherche de racine.

    Paramètres
    ----------
    fct : function
        La fonction pour laquelle la racine doit être trouvée.
    dfct : function
        La dérivée de la fonction fct.
    b_inf : float
        Borne inférieure de l'intervalle de recherche.
    b_sup : float
        Borne supérieure de l'intervalle de recherche.
    precision : float
        La précision souhaitée pour la racine.

    Retours
    -------
    Aucun retour, mais imprime les résultats des différentes méthodes de recherche de racine.
    
    Exemple
    -------
    racine_all_method(b_sup=1, b_inf=2, precision = 10**(-4), fct=lambda x: x**2-2, dfct=lambda x:2*x)
    """
    print(f"Étude dans l'intervalle [{b_inf},{b_sup}] à la précision {precision}")
    cordes(b_sup = b_sup, b_inf = b_inf, precision = precision, fct=fct)
    print("----------------")
    dicotomie(b_sup = b_sup, b_inf = b_inf, precision = precision, fct=fct)
    print("----------------")
    newton(val = (b_sup+b_inf)/2, precision = precision, fct=fct, dfct=dfct)
    print("----------------")
    secante(b_sup = b_sup, b_inf = b_inf, precision = precision, fct=fct)
    print("----------------")
    fausse_position(b_sup=b_sup, b_inf = b_inf, precision = precision, fct=fct)

################################################################################
#####                  Zone d'éxécution du programme/test                  #####
################################################################################
if __name__ == "__main__" :
    print("\n\nÉxécution du fichier main.py \n\n")   
    
     
    ######### Rappel #########
    # il est important de définir la dérivée (dfct pour newton) 
    
    ######### Fonction / Dérivées #########
    # --> à mettre en paramètres de la fonction
    # fct=lambda x: x**2-2, dfct=lambda x:2*x
    # fct=lambda x: 0.51 * x - np.sin(x), dfct=lambda x: 0.51 − np.cos(x)
    # fct=lambda x: (1 - 0.61 * x) / x, dfct=lambda x: -(1-0.61*x)/x**2-0.61/x
    # fct=lambda x: np.exp(x ** 2) - 56 * np.exp(-2 * x ** 2), dfct=lambda x: 224*x*np.exp(−2*x*2)+2*x*np.exp(x*2)
    
    
    ######### Partie 1 #########
    print("\n\nQuestion 1")
    print("\nUne fonction qui a pour racine : racine de 2 peut etre :")
    print("f(x)=x**2-2")
    racine_all_method(b_inf=1, b_sup=2, precision = 10**(-4), fct=lambda x: x**2-2, dfct=lambda x:2*x)
    print("\n\n--------------------------------")
    print("\nQuestion 2")
    print("\nf(x)=0.51 * x - np.sin(x)")
    racine_all_method(b_inf=1, b_sup=2, precision = 10**(-4), fct=lambda x: 0.51 * x - np.sin(x), dfct=lambda x: 0.51 - np.cos(x))
    print("\nf(x)=(1 - 0.61 * x) / x")
    racine_all_method(b_inf=1.5, b_sup=2, precision = 10**(-4), fct=lambda x: (1 - 0.61 * x) / x, dfct=lambda x: -(1-0.61*x)/x**2-0.61/x)
    print("\nf(x)=np.exp(x ** 2) - 56 * np.exp(-2 * x ** 2)")
    racine_all_method(b_inf=1, b_sup=2, precision = 10**(-4), fct=lambda x: np.exp(x ** 2) - 56 * np.exp(-2 * (x ** 2)), dfct=lambda x: 224*x*np.exp(-2*x**2)+2*x*np.exp(x**2)) 