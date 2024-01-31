# Todo: Code is a bit unclear

def convert_fahr_to_celsius(fahr):
    """
    Arguements§
        fahr:Temperature in fahrenheit
    """
    
    celsius = (fahr - 32) * (5 / 9)
    return celsius

def convery_fahr_to_kelvin(fahr):
    """
    Arguements
        fahr:Temperature in fahrenheit
    """
    celsius = convert_fahr_to_celsius(fahr)
    kelvin = celsius + 273.15
    return kelvin
