class SistemaExpertoAhorro:

    def __init__(self):
        self.hechos = {}          # Base de hechos (respuestas del usuario)
        self.reglas = []          # Base de conocimiento (reglas IF-THEN)
        self.conclusiones = []    # Resultados generados por el sistema

    def cargar_hechos(self):
        print("Responde con si/no\n")

        # Entrada de datos (hechos)
        self.hechos["tiene_ahorro"] = input("¿Tienes ahorros? ") == "si"
        self.hechos["ahorra_mensualmente"] = input("¿Ahorras cada mes? ") == "si"
        self.hechos["gasta_mas_de_lo_que_gana"] = input("¿Gastas más de lo que ganas? ") == "si"
        self.hechos["tiene_deudas"] = input("¿Tienes deudas? ") == "si"
        self.hechos["deudas_altas"] = input("¿Tus deudas son altas? ") == "si"
        self.hechos["ingresos_estables"] = input("¿Tus ingresos son estables? ") == "si"
        self.hechos["planifica_gastos"] = input("¿Planificas tus gastos? ") == "si"
        self.hechos["usa_credito_frecuente"] = input("¿Usas crédito frecuentemente? ") == "si"

    def definir_reglas(self):

        # Base de conocimiento (reglas del experto)
        self.reglas = [

            {
                "id": 1,
                "premisas": [("tiene_ahorro", True), ("ahorra_mensualmente", True),
                             ("planifica_gastos", True), ("gasta_mas_de_lo_que_gana", False)],
                "conclusion": "Buen_Ahorro",     # Diagnóstico
                "certeza": 0.9                  # Nivel de confianza
            },

            {
                "id": 2,
                "premisas": [("tiene_deudas", True), ("usa_credito_frecuente", True),
                             ("ahorra_mensualmente", False)],
                "conclusion": "Riesgo_Financiero",
                "certeza": 0.7
            },

            {
                "id": 3,
                "premisas": [("gasta_mas_de_lo_que_gana", True), ("deudas_altas", True),
                             ("ahorra_mensualmente", False)],
                "conclusion": "Problema_Financiero",
                "certeza": 0.95
            }
        ]

    def evaluar(self):
        # MOTOR DE INFERENCIA
        # Evalúa las reglas con base en los hechos

        for regla in self.reglas:     # Recorre cada regla
            cumple = True

            for hecho, valor in regla["premisas"]:   # Evalúa condiciones (IF)
                if self.hechos[hecho] != valor:
                    cumple = False
                    break

            if cumple:
                # Genera conclusión (THEN)
                self.conclusiones.append((regla["conclusion"], regla["certeza"]))

    def mostrar_resultados(self):

        if not self.conclusiones:
            print("\nNo se pudo determinar un estado claro.")
        else:
            print("\nResultados:")
            for c in self.conclusiones:
                print(f"- {c[0]} (Certeza: {c[1]})")

        # Recomendaciones basadas en la conclusión
        print("\nRecomendaciones:")

        for c in self.conclusiones:
            if c[0] == "Buen_Ahorro":
                print("Mantén tus buenos hábitos financieros.")
            elif c[0] == "Riesgo_Financiero":
                print("Reduce gastos y comienza a ahorrar.")
            elif c[0] == "Problema_Financiero":
                print("Reduce deudas urgentemente.")


# PROGRAMA PRINCIPAL
se = SistemaExpertoAhorro()
se.cargar_hechos()     # Entrada de datos
se.definir_reglas()    # Carga conocimiento
se.evaluar()           # Motor de inferencia
se.mostrar_resultados() # Salida
