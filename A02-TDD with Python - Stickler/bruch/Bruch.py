"""
Created on 26.10.2016

@author: mstickler01
"""
from __future__ import division, print_function, unicode_literals

class Bruch(object):

    """ Bruch
    :param int zaehler: numerator
    :param int nenner: denominator
    :ivar int zaehler: numerator
    :ivar int nenner: denominator
    """
    def __iter__(self):
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=0):

        """constructor
        :raise TypeError: incompatible types
        :param zaehler: int
        :param nenner: int (not zero)
        """
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:'+type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:'+type(nenner).__name__) 
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner

    def __float__(self):

        """overrides float()

        :return: float
        """
        return self.zaehler / self.nenner

    def __int__(self):

        """overrides int()

        :return: int
        """
        return int(self.__float__())

    def __neg__(self):

        """
        Negation

        :return: Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __radd__(self, zaehler):

        """
        Another version of add

        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler)

    def __add__(self, zaehler):

        """
        Addition

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__)
        nnenner = self.nenner * n2
        nzaehler = z2*self.nenner + n2*self.zaehler
        return Bruch(nzaehler, nnenner)
    
    def __complex__(self):

        """
        overrides complex()

        :return: complex
        """
        return complex(self.__float__())
        
    def __rsub__(self, tmp):

        """
        another version of sub

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if type(tmp) is int:
            z2 = tmp
            nnenner = self.nenner
            nzaehler = z2 * self.nenner - self.zaehler
            return Bruch(nzaehler, nnenner)
        else:
            raise TypeError('incompatible types:' + type(tmp).__name__)

    def __sub__(self, zaehler):

        """sub

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__add__(zaehler*-1)
    
    def __rmul__(self, zaehler):

        """right version of mul

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__mul__(zaehler)
        
    def __mul__(self, zaehler):

        """mul

        :raise TypeError: incompatible types
        :param zaehler: int or Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:'+type(zaehler).__name__)
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)
    
    def __pow__(self, p):

        """Bruch power

        :raise TypeError: incompatible types
        :param int p: power
        :return: Bruch
        """
        if type(p) is int:
            return Bruch(self.zaehler**p, self.nenner**p)
        else:
            raise TypeError('incompatible types:'+type(p).__name__)

    def __rdiv__(self, tmp):

        """
        right version of division for python 2.x

        :param zaehler: int or Bruch
        :return: Bruch
        """
        return self.__rtruediv__(tmp)
    
    def __rtruediv__(self, tmp):

        """
        right version of div for python >= 3.x

        :raise TypeError: incompatible types
        :param tmp: int or Bruch
        :return: Bruch
        """
        if type(tmp) is int:
            z2 = tmp * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('incompatible types:'+type(tmp).__name__)

    def __div__(self, tmp):

        """
        division for python 2.x

        :param other: int or Bruch
        :return: Bruch
        """
        return self.__truediv__(tmp)

    def __truediv__(self, tmp):

        """
        division python >= 3.x

        :raise TypeError: incompatible types
        :param zaehler: Bruch or int
        :return: Bruch
        """
        if isinstance(tmp, Bruch):
            z2, n2 = tmp
        elif type(tmp) is int:
            z2, n2 = tmp, 1
        else:
            raise TypeError('incompatible types:'+type(tmp).__name__)
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))
    
    def __invert__(self):

        """
        invert function

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __makeBruch(tmp):

        """
        make a bruch

        :raise TypeError: incompatible types
        :param tmp: Bruch or int
        :return: Bruch
        """
        if isinstance(tmp, Bruch):
            return tmp
        elif type(tmp) is int:
            b = Bruch(tmp, 1)
            return b
        else:
            raise TypeError('incompatible types:'+type(tmp).__name__)
    
    def __eq__(self, tmp):

        """
        equal

        :param Bruch tmp: temporary Bruch
        :return: boolean
        """
        tmp = Bruch.__makeBruch(tmp)
        return self.zaehler * tmp.nenner == tmp.zaehler * self.nenner
        
    def __ne__(self, tmp):

        """
        not equal

        :param Bruch tmp: temporary Bruch
        :return: boolean
        """
        return not self.__eq__(tmp)
    
    def __gt__(self, tmp):

        """
        greather than

        :param Bruch tmp: temporary Bruch
        :return: boolean
        """
        tmp = Bruch.__makeBruch(tmp)
        return self.zaehler * tmp.nenner > tmp.zaehler * self.nenner
        
    def __lt__(self, tmp):

        """
        lower than

        :param Bruch tmp: temporary Bruch
        :return: boolean
        """
        tmp = Bruch.__makeBruch(tmp)
        return self.zaehler * tmp.nenner < tmp.zaehler * self.nenner
        
    def __ge__(self, tmp):
        """
        greather or equal to

        :param Bruch tmp: temporary Bruch
        :return: boolean
        """
        tmp = Bruch.__makeBruch(tmp)
        return self.zaehler * tmp.nenner >= tmp.zaehler * self.nenner
        
    def __le__(self, tmp):
        """
        lower or equal to

        :param Bruch tmp: temporary Bruch
        :return: boolean
        """
        tmp = Bruch.__makeBruch(tmp)
        return self.zaehler * tmp.nenner <= tmp.zaehler * self.nenner
    
    def __abs__(self):
        """
        overridesabs(Bruch)

        :return: positive Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))
    
    def __iadd__(self, tmp):

        """intern add

        :param Bruch tmp: temporary Bruch
        :return: self
        """
        tmp = Bruch.__makeBruch(tmp)
        self = self + tmp
        return self
        
    def __isub__(self, tmp):

        """intern sub

        :param Bruch tmp: temporary Bruch
        :return: self
        """
        tmp = Bruch.__makeBruch(tmp)
        self = self - tmp
        return self
        
    def __imul__(self, tmp):

        """intern mul

        :param Bruch tmp: temporary Bruch
        :return: self
        """
        tmp = Bruch.__makeBruch(tmp)
        self = self * tmp
        return self
    
    def __idiv__(self, tmp):

        """intern division 2.x

        :param Bruch tmp: temporary Bruch
        :return: self
        """
        return self.__itruediv__(tmp)

    def __itruediv__(self, tmp):

        """intern division 3.x

        :param Bruch tmp: temporary Bruch
        :return: self
        """
        tmp = Bruch.__makeBruch(tmp)
        self = self / tmp
        return self