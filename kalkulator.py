import math

def oblicz (a ,b , c):
    """ Oblicza pole trojkata wg wzoru Herona
    a ,b ,c dlugosci bokow trojkata
    >> heron (3 ,4 ,5)
    6.0
    """
    x = ( a + b + c )/2
    return math . sqrt ( x * (x -1) * (x - b ) * (x - c ))

if __name__ == "__main__":
    print (oblicz.__doc__)
    print(oblicz(3, 4, 5))