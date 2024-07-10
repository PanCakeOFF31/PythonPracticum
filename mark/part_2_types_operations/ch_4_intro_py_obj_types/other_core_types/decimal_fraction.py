import Lib.decimal as decimal
import Lib.fractions as fractions

d = decimal.Decimal('3.1415')
print(d)
d += 1
print(d)

f = fractions.Fraction(3, 5)
print(f)

f += f
print(f)
