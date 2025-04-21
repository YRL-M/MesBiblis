# !git clone https://github.com/YRL-M/MesBiblis
# import sys
# sys.path.append('/content/MesBiblis')
# from arithmetique import *

# Liste des fonctions : 
  # racine
  # division
  # divLongue

#   ------------------   #

def Heron(n, verbose=False) :
    """
        Vérifie si True ou False un entier n est un carré parfait.
        Renvoie b, r : booléen et la racine de n.
    """

    if n == 0 : 
        return True
    if not isinstance(n, int):
        raise TypeError(f"{n} doit être un int")
    if n < 0 :
        raise ValueError(f"{n} doit être positif")
    
    ( L , l ) = ( n , 1 )
    
    for _ in range( 10000 ) :  
        L = quotient( L + l, 2)
        l = quotient(n, L) 
        if verbose : 
            print( L, l)
        if L*L == n:
            return True, L
        if L <= l :
            return False, L
    return False, L
 

def est_carré(n):
  """
    Renvoie le booléen si True ou False n est un carré parfait.
    Basé sur b,r = Heron(n)
    est_carré(n) >> b True ou False
    """
  b, r = Heron(n)
  return b
  
def iracine(n):
    """
    Renvoie la racine entière exacte sur n est un carré parfait.
    Ou approximative si n n'en est pas un.
    Basé sur b,r = Heron(n)
    iracine(n) >> r (int)
    """
  b, r = Heron(n)
  return r



def division(D:int, d:int):
    """
    Renvoie le quotient et le reste de la division entière de D par d.
    division(D, d) >> q, r
    """

    if d==0:
        raise ZeroDivisionError(f"Dividende = {D}, diviseur = {d}")
    if type(D)!=int :
        raise TypeError(f"{D} n'est pas un entier.")
    if type(d)!=int:
        raise TypeError(f"{d} n'est pas un entier.")
    if d < 0:
        raise ValueError(f"Le diviseur {d} doit être positif.")
    if D < 0:
        raise ValueError(f"Le Dividende {D} doit être positif.")

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




def quotient(D:int, d:int):
    """
    Renvoie le quotient de la division entière de D par d.
    quotient(D, d) >> q
    """
    q, r = division(D, d)
    return q



def reste(D:int, d:int):
    """
    Renvoie le reste de la division entière de D par d.
    reste(D, d) >> r
    """
    q, r = division(D, d)
    return r



def division_longue(D:int, d:int, p:int):
    """A partir d'un couple Dividende diviseur : (D, d)
    On print les étapes d'une division 
    effectuée à la main sur p étapes
    """

    r = D                # travail sur r local plutôt que l'argument D
    print( str(D).ljust(10) + str(d).rjust(5) +"\n---------------" )

    for _ in range( p ) :
        (q, r) = division(r, d)

        if (r, q) == (0, 0) :
            break
            
        print(str(r).ljust(10) + str(q).rjust(5) )
        r *= 10

