
def IMC(height, weight):
    return weight/(height * height)

def IMC_interpretation(IMC):
    if IMC < 18.5:
        interpretation ='Bajo peso'
    elif IMC >= 18.5 and IMC < 25:
        interpretation ='Peso normal'
    elif IMC >= 25 and IMC < 30:
        interpretation = 'Peso normal'
    else: #IMC superior a 30
        interpretation = 'Obesidad'
    return interpretation    

if __name__ == "__main__":
    # Llamamos a la función saludar() cuando el script se ejecuta directamente
    height = float(input("Ingrese su altura en metros: "))
    weight = float(input("Ingrese su peso: "))
    interpretation = IMC_interpretation(IMC( height,weight)) 
    print(interpretation)        

