def monHeron( A ) :
  (L , l) = ( A , 1)
  for i in range(10) :
    L = (L + l) / 2
    l = A / L
    # print( L )
  # print( "carré" , L * L)
  print( A , L )

  return L
