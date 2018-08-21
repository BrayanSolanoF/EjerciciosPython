def mult_complex(Real1,Img1,Real2,Img2):
    if isinstance (Img1, complex) and isinstance (Img2, complex) and (Real1, int) and (Real2, int):
        numComplex = (complex(Real1,Img1) * complex(Real2,Img2))
        return numComplex
