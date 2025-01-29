def racine( A ) :
  """Calcul de la racine carrée de A par Héron en 10 étapes"""
  ( L , l ) = ( A , 1 )
  for i in range(10) :
    L = ( L + l ) / 2
    l = A / L
  return (L + l) / 2
