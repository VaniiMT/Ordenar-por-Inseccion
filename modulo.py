def division_restas(dividendo, divisor):
    if divisor == 0:
        return False

    signo = 1
    if (dividendo < 0) != (divisor < 0):
        signo = -1
    a = abs(dividendo)
    b = abs(divisor)
    cociente = 0
    while a >= b:
        a = a - b      
        cociente += 1  
    return signo * cociente, a
print(division_restas(17, 5))  
    #a%b
  def modulo(a.b): 
    division = a//b
    producto = division*b
    resto = producto - a

     

