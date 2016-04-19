import math

def heron (a ,b , c):
    """ Oblicza pole trojkata wg wzoru Herona
    a ,b ,c dlugosci bokow trojkata
    >> heron (3 ,4 ,5)
    6.0
    """
    x = ( a + b + c )/2
    return math . sqrt ( x * (x -1) * (x - b ) * (x - c ))

if __name__ == "__main__":
    print (heron.__doc__)
    print(heron(3, 4, 5))