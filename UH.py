class UH:
    def __init__(self,caminho_arquivo):
        with open(caminho_arquivo+".txt", "r", encoding="utf-8") as arquivo:
            arquivo = arquivo.read()
        self.representacao = arquivo
        self.representacao_maquina = ""
        self.representacao_palavra = ""
    def __representacao_maquina__(self):
        _contador_3_zeros = 0
        _contador_zeros = 0
        for caracter in self.representacao:
            if _contador_3_zeros < 2:
                self.representacao_maquina += caracter
            else:
                self.representacao_palavra += caracter
            if caracter == "0":
                _contador_zeros += 1
            else:
                _contador_zeros = 0
            if _contador_zeros == 3:
                _contador_3_zeros += 1
    def __imprimir_representacao_maquina__(self):
        print(self.representacao_maquina)
