from datatype import TypeMeta,datatype

@datatype
class Natural(metaclass=TypeMeta):
    Zero : ()
    Succ : ("num",)
from m_Natural import *
print( Zero , Succ , Natural )
def toInt(nat):
    if isinstance(nat,Zero):
        return 0
    return 1 + toInt( nat.num )
zero = Zero ()
one = Succ ( zero )
two = Succ ( one )
def plus(a,b):
    if isinstance(a,Zero):
        return b
    return Succ( plus(a.num,b) )
print(   toInt(  plus ( one,two )  )   )
