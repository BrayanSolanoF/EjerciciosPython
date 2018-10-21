def suma_matriz(Mat1, Mat2):
    if len(Mat1)==len(Mat2) and len(Mat1[0])==len(Mat2[0]):
        return suma_matriz_aux(Mat1, Mat2, len(Mat1), len(Mat1[0]), 0, 0)
    else:
        return "Error"
def suma_matriz_aux(Mat1, Mat2, n, m, i, j):
    if i==n:
        return Mat1
    elif j==m:
        return suma_matriz_aux(Mat1, Mat2, n, m, i+1, 0)
    else:
        Mat1[i][j]=Mat1[i][j]+Mat2[i][j]
        return suma_matriz_aux(Mat1, Mat2, n, m, i, j+1)


