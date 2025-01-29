def monHeron( A ) :
  ( L , l ) = ( A , 1 )
  for i in range(10) :
    L = ( L + l ) / 2
    l = A / L
  return (L + l) / 2
