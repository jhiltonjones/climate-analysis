# Todo: Code is a bit unclear

def convert_fahr_to_celsius(fahr):
    """
    Arguements§
        fahr:Temperature in fahrenheit
    """
    
    celsius = (fahr - 32) * (5 / 9)
    if celsius < -273.15:
        # If temperture is below absolute zero, throw an error
        raise ValueError(
            f"Trying to convert impossible temperture: {fahr}f"
        )
    return celsius

def convery_fahr_to_kelvin(fahr):
    """
    Arguements
        :param fahr:Temperature in fahrenheit
        :return: The temperture in kelvin
    """
    celsius = convert_fahr_to_celsius(fahr)
    kelvin = celsius + 273.15
    return kelvin
