class AutomatoFinito:
    def __init__(self):
        self.estados = ['q0', 'q1', 'q2', 'q3'];
        self.alfabeto = ['a', 'b'];
        self.transicoes = [('q0', 'q1', 'a'), ('q1', 'q1', 'a'), ('q1', 'q2', 'b'), ('q2', 'q1', 'b'), ('q2', 'q3', 'a')];
        self.estado_inicial = 'q0';
        self.estados_finais = ['q1', 'q3'];

    def aceita(self, palavra):
        estado_atual = self.estado_inicial;

        for simbolo in palavra:
            if (estado_atual, simbolo) in self.transicoes:
                estado_atual = self.transicoes[(estado_atual, simbolo)];
            else:
                return False;

        return estado_atual in self.estados_finais;

def main():
    automato = AutomatoFinito();

    palavra = input("Palavra: ");
    if automato.aceita(palavra):
        print("Aceita");
    else:
        print("Rejeita");

if __name__ == "__main__":
    main();