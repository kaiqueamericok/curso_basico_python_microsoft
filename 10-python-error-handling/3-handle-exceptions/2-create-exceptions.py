#Os astronautas limitam o uso de água a cerca de 11 litros por dia. Vamos criar uma função que, dependendo do #número de astronautas, pode calcular a quantidade de água que restará após um dia ou mais:

def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            # If argument is an int, the following operation will work
            argument / 10
        except TypeError:
            # TypeError will be raised only if it isn't the right type 
            # Raise the same exception but with a better error message
            raise TypeError(f"All arguments must be of type int, but received: '{argument}'")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

#O código acima faz uma verificação para garantir que todos os argumentos ('astronauts','water_left','days_left') #sejam do tipo 'int'. A operação argument é usada para verificar isso, se argumento não for um n´mero, o python #levantará um "typeError"
#RuntimeError Ocorre se não houver água suficiente para os astronautas após o número especificado de dias. A $mensagem de erro explica a falta de água em relação ao número de astronautas e dias.