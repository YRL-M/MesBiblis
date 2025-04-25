# !git clone https://github.com/YRL-M/mesModules
# import sys
# sys.path.append('/content/mesModules')
# from arithmetique import *

# Liste des fonctions : 
  # racine
  # division
  # divLongue

#   ------------------   #

def heron(n, verbose=False):
    """
    Effectue l'algorithme de Héron, avec des divisions ENTIERES
    Renvoie b, r : booléen de quadraticité de n et la racine entière de n.
    """

    if n == 0:                 return True, 0
    if not isinstance(n, int): raise TypeError(f"{n} doit être un entier")
    if n < 0 :                 raise ValueError(f"{n} doit être positif")
  
    # Initialisation 
    (L, l) = (n, 1)

    # Boucle principale
    for _ in range( 100000 ) :
        L = quotient(L+l, 2)   # moyenne ENTIÈRE
        l = quotient(n, L)     # conservation de matière 
        if verbose: print(L, l)
      
        if L*L == n:
            return True, L
        if L <= l:
            return False, L
    else: # for,else:
        raise RuntimeError(f"Attention, heron({n}) a effetué 100000 itérations, c'est anormal.")

 

def quadratic(n):
    """
    Renvoie le booléen True ou False si n est un carré parfait.
    Basé sur b, r = heron(n)
    quadratic(n) >> b
    """
    b, r = heron(n)
    return b
  
def iracine(n):
    """
    Renvoie la racine entière de n
    Résultat exact si n est un carré parfait.
    Résultat approximatif sinon.
    Basé sur b,r = heron(n)
    iracine(n) >> r 
    """
    b, r = heron(n)
    return r


def division(D, d):
    """
    Renvoie le quotient et le reste de la division entière de D par d.
    division(D, d) >> q, r
    """

    if type(D)!=int: raise TypeError(f"{D} n'est pas un entier.")
    if type(d)!=int: raise TypeError(f"{d} n'est pas un entier.")
    if d==0:         raise ZeroDivisionError(f"Dividende = {D}, diviseur = {d}")
    if D==0:         return 0, 0
    if d < 0:        raise ValueError(f"Le diviseur {d} doit être positif.")
    if D < 0:        raise ValueError(f"Le Dividende {D} doit être positif.")

    # Initialisation
    q, r = 0, D

    # Calcul
    while r >= d:
        m = d
        p = 1
        # Recherche du multiple de d le plus proche de r
        while r >= m:
            m *= 10
            p *= 10

        # Il y va p fois
        r -= m // 10  # d
        q += p // 10  # 1

    return q, r # Quotient et reste de D/d




def quotient(D, d):
    """
    Renvoie le quotient de la division entière de D par d.
    quotient(D, d) >> q
    """
    q, r = division(D, d)
    return q



def reste(D, d):
    """
    Renvoie le reste de la division entière de D par d.
    reste(D, d) >> r
    """
    q, r = division(D, d)
    return r



def division_longue(D, d, p):
    """A partir d'un couple (Dividende, diviseur) : (D, d)
    On print les étapes d'une division 
    effectuée à la main sur p étapes
    """
    lD, ld = len(str(D)), len(str(d))
    r = D                # travail sur r local plutôt que l'argument D
    print( str(D).ljust(5+lD+p) + str(d).rjust(5+ld) +"\n"+"-"*(5+lD+p+5+ld) )

    for _ in range( p ) :
        (q, r) = division(r, d)

        if (q, r) == (0, 0) :
            break
            
        print( str(r).ljust(5+lD+p) + str(q).rjust(5+ld) )
        r *= 10

