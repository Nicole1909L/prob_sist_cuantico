import numpy as np
def separar(numero):
    n = complex(numero)
    real = np.real(n)
    imagin = np.imag(n)
    return real,imagin
def prob_sist_linea(vect,pos):
    vector = np.array(vect)
    i = int(pos)
    a,b = separar(vector[i])
    numer = (a**2 + b**2)
    denom = 0
    for j in range(len(vector)):
        x,y = separar(vector[j])
        d = (x**2 + y**2)
        denom += d
    return (numer/denom)
def amplitud_trans(v1,v2):
    vect_1 = np.array(v1)
    vect_2 = np.array(v2)
    Vn1 = vect_1 / np.linalg.norm(vect_1)
    Vn2 = vect_2 / np.linalg.norm(vect_2)
    if len(Vn1) == len(Vn2):
        Vn2 = np.transpose(Vn2.conjugate())
        result = np.array(np.dot(Vn2,Vn1))
        return (result)
    else:
        return ("No cumple requerimientos") 
if __name__ == '__main__':
    print(prob_sist_linea([2+1j,-3j,4],1))
    print("-----------------------------------------")
    print(amplitud_trans([3+8j,1j,1],[5j,6,2-1j]))
    