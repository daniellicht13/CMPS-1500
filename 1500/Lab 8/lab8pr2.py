"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 8 Part 1
04/11/2018"""

class Rational:
    def __init__(self, n, d):
        """ The rational number constructor 
            Args:
                self: object of type Rational
                n (int): Numerator
                d (int): Denominator
            Returns:
                None
        """
        self.numerator = n
        self.denominator = d
        
    def __str__(self):
        """ Overloading of str function 
            Args:
                self: object of type Rational
            Returns:
                String of rational number as a fraction
        """
        return str(self.numerator) + "/" + str(self.denominator)
        
    def __add__(self, other):
        """ Adds two rational numbers together
            Args:
                self: object of type Rational
                other: object of type Rational
            Returns:
                Two rational numbers added together
        """
        newNumerator = self.numerator * other.denominator + self.denominator * other.numerator
        newDenominator = self.denominator * other.denominator
        return Rational(newNumerator, newDenominator)
    
    def __truediv__(self, other):
        """ Divides one rational number by another
            Args:
                self: object of type Rational
                other: object of type Rational
            Returns:
                Result of one rational number divided by another
        """
        newNumerator = self.numerator * other.denominator
        newDenominator = self.denominator * other.numerator
        return Rational(newNumerator, newDenominator)
        
    def __pow__(self, exponent):
        """ Raises a rational number to a given power
            Args:
                self: object of type Rational
                exponent (int): power that self is raised to
            Returns:
                Rational number raised to a given power
        """
        newNumerator = int(self.numerator ** exponent)
        newDenominator = int(self.denominator ** exponent)
        return Rational(newNumerator, newDenominator)

    def __float__(self):
        """ Converts a rational number to a floating point number
            Args:
                self: object of type Rational
            Returns:
                Floating point number
        """
        self.numerator = int(self.numerator)
        self.denominator = int(self.denominator)
        return self.numerator / self.denominator
    
    def __eq__(self, other):
        """ Tests equality of two rational numbers
            Args:
                self: object of type Rational
                other: object of type Rational
            Returns:
                Boolean value of whether the rational numbers are equivalent
        """
        return self.numerator * other.denominator == self.denominator * other.numerator
    
    def __ge__(self, other):
        """ Tests if one rational number is greater than or equal to another
            Args:
                self: object of type Rational
                other: object of type Rational
            Returns:
                Boolean value of whether self is greater than or equal to other
        """
        return self.numerator * other.denominator >= self.denominator * other.numerator
