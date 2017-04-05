"""
Created on 26.10.2016

@author: Matthias Stickler
@version: 1.2
"""
from __future__ import division, print_function, unicode_literals


class Bruch(object):
    """ Bruch

    :param int zaehler: Zaehler
    :param int nenner: Nenner
    :ivar int zaehler: Zaehler
    :ivar int nenner: Nenner
    """

    def __iter__(self):

        """Laesst durch den Bruch iterieren
        """
        return (self.zaehler, self.nenner).__iter__()

    def __init__(self, zaehler=0, nenner=1):

        """Konstruktor

        :raise TypeError: incompatible types
        :param zaehler: Bruch oder int
        :param nenner: int - nicht 0
        """
        if isinstance(zaehler, Bruch):
            self.zaehler, self.nenner = zaehler
            return
        elif type(zaehler) is not int:
            raise TypeError('incompatible type:' + type(zaehler).__name__)
        elif type(nenner) is not int:
            raise TypeError('incompatible type:' + type(nenner).__name__)
        if nenner == 0:
            raise ZeroDivisionError
        self.zaehler = zaehler
        self.nenner = nenner

    def __float__(self):

        """überschreibt float()

        :return: float
        """
        return self.zaehler / self.nenner

    def __int__(self):

        """überschreibt int()

        :return: int
        """
        return int(self.__float__())

    def __neg__(self):

        """negiert den Bruch

        :return: Bruch
        """
        return Bruch(-self.zaehler, self.nenner)

    def __radd__(self, zaehler):

        """add für Python 2.x

        :raise TypeError: incompatible types
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        return self.__add__(zaehler)

    def __add__(self, zaehler):

        """Addition

        :raise TypeError: incompatible types
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' + Bruch()')
        nennerneu = self.nenner * n2
        zaehlerneu = z2 * self.nenner + n2 * self.zaehler
        return Bruch(zaehlerneu, nennerneu)

    def __complex__(self):

        """überschreibt complex()

        :return: complex
        """
        return complex(self.__float__())

    def __rsub__(self, left):

        """sub für Python 2.x

        :raise TypeError: incompatible types
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left
            nennerneu = self.nenner
            zaehlerneu = z2 * self.nenner - self.zaehler
            return Bruch(zaehlerneu, nennerneu)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' - Bruch()')

    def __sub__(self, zaehler):

        """Subtraktion

        :raise TypeError: incompatible types
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        return self.__add__(zaehler * -1)

    def __rmul__(self, zaehler):

        """mul für Python 2.x

        :raise TypeError: incompatible types
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        return self.__mul__(zaehler)

    def __mul__(self, zaehler):

        """Multiplikation

        :raise TypeError: incompatible types
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' * Bruch()')
        z2 *= self.zaehler
        n2 *= self.nenner
        return Bruch(z2, n2)

    def __pow__(self, p):

        """Exponential

        :raise TypeError: incompatible types
        :param int p: power
        :return: Bruch
        """
        if type(p) is int:
            return Bruch(self.zaehler ** p, self.nenner ** p)
        else:
            raise TypeError('incompatible types:' + type(p).__name__ + ' should be an int')

    def __rdiv__(self, other):

        """div für Python 2.x

        :param zaehler: int oder Bruch
        :return: Bruch
        """
        return self.__rtruediv__(other)

    def __rtruediv__(self, left):

        """div für Python >= 3.x

        :raise TypeError: incompatible types
        :param zaehler: int oder Bruch
        :return: Bruch
        """
        if type(left) is int:
            z2 = left * self.nenner
            if self.zaehler == 0:
                raise ZeroDivisionError
            return Bruch(z2, self.zaehler)
        else:
            raise TypeError('incompatible types:' + type(left).__name__ + ' / Bruch()')

    def __div__(self, other):

        """div für Python 2.x

        :param other: int oder Bruch
        :return: Bruch
        """
        return self.__truediv__(other)

    def __truediv__(self, zaehler):

        """Division

        :raise TypeError: incompatible types
        :param zaehler: Bruch oder int
        :return: Bruch
        """
        if isinstance(zaehler, Bruch):
            z2, n2 = zaehler
        elif type(zaehler) is int:
            z2, n2 = zaehler, 1
        else:
            raise TypeError('incompatible types:' + type(zaehler).__name__ + ' / Bruch()')
        if z2 == 0:
            raise ZeroDivisionError
        return self.__mul__(Bruch(n2, z2))

    def __invert__(self):

        """Inversieren des Bruchs

        :return: Bruch
        """
        return Bruch(self.nenner, self.zaehler)

    def __repr__(self):

        """Bruch objekt representieren

        :return str: the representation
        """
        # Vor der Ausgabe wird gekuerzt!
        shorten = Bruch.gcd(self.zaehler, self.nenner)
        self.zaehler //= shorten
        self.nenner //= shorten
        # Nenner stehts positiv
        if self.nenner < 0:
            self.nenner *= -1
            self.zaehler *= -1

        if self.nenner == 1:
            return "(%d)" % self.zaehler
        else:
            return "(%d/%d)" % (self.zaehler, self.nenner)

    def __makeBruch(other):

        """Bruch erstellen oder referenz zurueckgeben

        :raise TypeError: incompatible types
        :param other: Bruch oder int
        :return: Bruch
        """
        if isinstance(other, Bruch):
            return other
        elif type(other) is int:
            b = Bruch(other, 1)
            return b
        else:
            raise TypeError('incompatible types:' + type(other).__name__ + ' not an int nor a Bruch')

    def __eq__(self, other):

        """equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner == other.zaehler * self.nenner

    def __ne__(self, other):

        """not equal to

        :param Bruch other: other Bruch
        :return: boolean
        """
        return not self.__eq__(other)

    def __gt__(self, other):

        """groesser als

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner > other.zaehler * self.nenner

    def __lt__(self, other):

        """kleiner als

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner < other.zaehler * self.nenner

    def __ge__(self, other):
        """groesser gleich

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner >= other.zaehler * self.nenner

    def __le__(self, other):
        """kleiner gleich

        :param Bruch other: other Bruch
        :return: boolean
        """
        other = Bruch.__makeBruch(other)
        return self.zaehler * other.nenner <= other.zaehler * self.nenner

    def __abs__(self):
        """absolute Werte von Bruch

        :return: positive Bruch
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __iadd__(self, other):

        """interne Addition

        :param Bruch other: Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self + other
        return self

    def __isub__(self, other):

        """interne Subtraktion

        :param Bruch other: Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self - other
        return self

    def __imul__(self, other):

        """interne Multiplikation

        :param Bruch other: other Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self * other
        return self

    def __idiv__(self, other):

        """interne Division für Python 2.x

        :param Bruch other: other Bruch
        :return: self
        """
        return self.__itruediv__(other)

    def __itruediv__(self, other):

        """interne Division für Python 3.x

        :param Bruch other: other Bruch
        :return: self
        """
        other = Bruch.__makeBruch(other)
        self = self / other
        return self

    @classmethod
    def gcd(cls, x, y):

        """euclidischer Algorithmus

        :param int x: first value
        :param int y: second value
        :return: groesster gemeinsamer nenner
        """
        x, y = abs(x), abs(y)
        if x < y:
            x, y = y, x
        """Berechnung """
        while y != 0:
            x, y = y, x % y
        return x
