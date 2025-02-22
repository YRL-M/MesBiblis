# !git clone https://github.com/YRL-M/MesBiblis
# import sys
# sys.path.append("/content/MesBiblis")
# from basique import division


def racine( A ) :
  """Calcul de la racine carrée de A par Héron en 10 étapes"""
  ( L , l ) = ( A , 1 )
  for i in range(10) :
    L = ( L + l ) / 2
    l = A / L
  return (L + l) / 2



def division( a , b ) :
  """Renvoit q et r , quotient et reste de la division de a par b."""
  q , r = 0 , a
  while r >= b :
    r = r - b
    q = q + 1
  
  return ( q , r )


def divLongue( D , d , p ) :
  """A partir d'un couple Dividende diviseur : (D,d)
  On print les étapes d'une division 
  effectuée à la main  sur p étapes
  """

  print( str(D).ljust(10) + str(d).rjust(5) )

  for i in range( p ) :
    
    ( q , r ) = division( D , d )
    D = 10*r

    if ( r , q ) == ( 0 , 0 ) :
      break
      
    print(str(r).ljust(10) + str(q).rjust(5) )

