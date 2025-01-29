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
