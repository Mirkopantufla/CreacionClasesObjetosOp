class Te():
    #Duracion en días
    duracion = 365

    # Tipos de te
    #  1: Té negro
    #  2: Té verde
    #  3: Agua de hierbas.
    @staticmethod
    def definir_recomendacion(sabor:int):
        if sabor == 1:
            return 3, "Al desayunar"
        elif sabor == 2:
            return 5, "Al mediodía"
        elif sabor == 3:
            return 6, "Al anochecer"

            
    # Formatos pemitidos son 300 g y 500 g
    @staticmethod
    def formato_precio(formato):
        if formato == 300:
            return 3000
        elif formato == 500:
            return 5000