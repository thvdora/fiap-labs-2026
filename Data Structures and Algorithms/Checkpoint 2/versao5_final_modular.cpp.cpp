// Versão modular do jogo de adivinhação em C++.
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

// Função para sortear um número aleatório entre 1 e 20.
int sortearBola() {
    return rand() % 20 + 1;
}

// Função para receber e validar o palpite do usuário.
int receberPalpite() {
    int palpite;
    cout << "Digite seu palpite (1 a 100): ";
    cin >> palpite;
    
    // Validação do palpite para garantir que esteja entre 1 e 100.
    while (palpite < 1 || palpite > 100) {
        cout << "Palpite invalido! Digite um numero de 1 a 100: ";
        cin >> palpite;
    }

    return palpite;
}

// Função para exibir dicas sobre o próximo alvo.
void exibirDica(int alvo) {
    int minimo = alvo + 1;
    int maximo = alvo + 20;

    if (maximo > 100) {
        maximo = 100;
    }

    if (minimo <= 100) {
        cout << "Dica: O proximo alvo estará entre "
             << minimo << " e " << maximo << "." << endl;
    }
}


// Função principal do jogo.
int main() {
    srand(time(0));
    int alvo = sortearBola();
    int palpite = 0;

    // Loop que continua enquanto o alvo for menor ou igual a 100 e o palpite do usuário não for igual ao alvo.
    while (alvo <= 100 && palpite != alvo) {
        palpite = receberPalpite();

        cout << "O alvo era: " << alvo << endl;
        cout << "Seu palpite foi: " << palpite << endl;

    // Exibindo o valor do alvo e o palpite do usuário.
        if (palpite != alvo) {
            cout << "Voce errou! Tente novamente." << endl;

            exibirDica(alvo);
            alvo += sortearBola(); // Atualizando o valor do alvo com um novo número aleatório.
        }
    }
// Exibindo o vencedor da partida.
if (palpite == alvo) {
    cout << "Parabens! Voce venceu!" << endl;
}
else {
    cout << "O alvo final foi: " << alvo << endl;
    cout << "Voce perdeu! O computador venceu!" << endl;
}

return 0;
}