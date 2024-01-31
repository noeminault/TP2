def fun(fonction, x):
    y = fonction(x)
    return y

resultat = fun(lambda x: x ** 2, 1)
print(resultat)











def cordes(): ##calcul 3 racines

    a =float(input("entrez a: "))
    b =float(input("entrez b: "))
    g =a
    d =b
    m =True
    n =0
    E =10**(-4)   
    t = 1
    while abs(f(m)) > E:
        
        n += 1
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        a = b
        b = m

    print("Valeur de la racine {} : {}".format(t,b))
    print("Nombre de calcul nécessaire afin d'obtenir la précision voulue : {}".format(n))
    a =g+0.1
    b =d-g
    m =True
    n =0
    t +=1
    while abs(f(m)) > E:
        
        n += 1
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        a = b
        b = m

    print("Valeur de la racine {} : {}".format(t,b))
    print("Nombre de calcul nécessaire afin d'obtenir la précision voulue : {}".format(n))
    a =g+0.1
    b =d-abs(g)
    m =True
    n =0
    t +=1
    while abs(f(m)) > E:
        
        n += 1
        m = (a*f(b)-b*f(a))/(f(b)-f(a))
        a = b
        b = m

    print("Valeur de la racine {} : {}".format(t,b))
    print("Nombre de calcul nécessaire afin d'obtenir la précision voulue : {}".format(n))
 