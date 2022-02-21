from sympy import comp


class complex:
    def __init__(self,real,complex) -> None:
        self.real = real
        self.complex = complex
        
    def __add__(self,other):
        return complex(self.real+other.real,self.complex+other.complex)
    def __str__(self) -> str:
        return f"{self.real}+{self.complex}i"
    def __mul__(self,other):
        return complex(self.real*other.real-self.complex*other.complex,self.real*other.complex+self.complex*other.real)
    

def main():
    a = complex(1,2)
    b = complex(5,4)
    print(a*b)

main()