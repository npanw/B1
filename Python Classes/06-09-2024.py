#Return Values From Function
def add(a,b):
    return a+b #Calling the function with alguments
    result = add(4,5)
    print(result) # Output: 9
    
#2
    x = 10  # Global variable

def outer_function():
    x = 20  # Enclosing variable
    print(f"value o x in outer  function after modification {x}")
    def inner_function():
        x = 30  # Local variable
        print(f"value in inner function after modification {x}") #Output: 30
    inner_function()
    print(x)  # Output: 20