a = input("Enter number a: ")
b = input("Enter number b: ")

mod_a = int(a) % 10
mod_b = int(b) % 10

if mod_a == mod_b and int(a)- int(b) < 0:
    print( b + " has bigger last digit than " + a)
    
elif mod_a == mod_b and int(a)- int(b) > 0:
    print( a + " has bigger last digit than " + b)
    
elif mod_a > mod_b:
    print(a + " has bigger last digit than " + b)

else:
    print(b + " has bigger last digit than " + a)
