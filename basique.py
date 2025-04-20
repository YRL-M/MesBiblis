# !git clone https://github.com/YRL-M/MesBiblis
# import sys
# sys.path.append("/content/MesBiblis")
# from basique import division

# Liste des fonctions : 
  # racine
  # division
  # divLongue

#   ------------------   #

def racine( A ) :
  """Calcul de la racine carrée de A par Héron en 10 étapes"""
  ( L , l ) = ( A , 1 )
  for i in range(10) :
    L = ( L + l ) / 2
    l = A / L
  return (L + l) / 2



# def division(D:int, d:int):
#     """Renvoit q et r , quotient et reste de la division de D par d."""

#     if d == 0:
#         raise ValueError("Le diviseur ne peut pas être zéro.")

#     q, r = 0, D
#     while r >= d:
#         r -= d
#         q += 1

#     return q, r



def division(D, d):

    q, r = 0, D
    while r >= d:
        m = d
        p = 1

        while r >= m:
            m *= 10
            p *= 10

        r -= m //10  #d
        q += p //10  #1
    return q, r
  




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

