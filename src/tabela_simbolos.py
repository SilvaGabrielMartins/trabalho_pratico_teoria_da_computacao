class tabela_simbolos:
    def __init__(self,codigo,tipo):
        self.codigo = codigo
        self.tipo = tipo
    def traduzir_simbolo(self):
        if self.tipo == "estado":
            return "Q" + str(len(self.codigo) - 1)
        elif self.tipo == "simbolo":
            if self.codigo ==  "1":
                return "a"
            elif self.codigo == "11":
                return "b"
        elif self.tipo == "movimento":
            if self.codigo == "1":
                return "R"
            elif self.codigo == "11":
                return "L"