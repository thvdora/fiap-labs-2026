#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0)); // Semente da sequência pseudoaleatória.

    // Criando a variável bola, que recebe um número aleatório entre 1 e 20, e a variável alvo, que recebe o valor de bola.
    int bola = rand() % 20 + 1;
    int alvo = bola;
    int palpite;

    cout << "Digite seu palpite (1 a 100): ";
    cin >> palpite;

    // Validação do palpite para garantir que esteja entre 1 e 100.
    while (palpite < 1 || palpite > 100) {
        cout << "Palpite invalido! Digite um numero de 1 a 100: ";
        cin >> palpite;
    }

    // Exibindo o valor do alvo e o palpite do usuário.
    cout << "O alvo era: " << alvo << endl;
    cout << "Seu palpite foi: " << palpite << endl;

    if (palpite != alvo) {
        cout << "Voce errou! Tente novamente." << endl;
    }

    // Loop que continua enquanto o alvo for menor ou igual a 100 e o palpite do usuário não for igual ao alvo.
    while (alvo <= 100 && palpite != alvo) {
        bola = rand() % 20 + 1;
        alvo = alvo + bola; // Atualizando o valor do alvo com um novo número aleatório.
        // Exibindo o valor do alvo e o palpite do usuário.
        if (alvo <= 100) {
            cout << "Digite seu palpite (1 a 100): ";
            cin >> palpite;

            // Validação do palpite para garantir que esteja entre 1 e 100.
            while (palpite < 1 || palpite > 100) {
                cout << "Palpite invalido! Digite um numero de 1 a 100: ";
                cin >> palpite;
            }

            cout << "O alvo era: " << alvo << endl;
            cout << "Seu palpite foi: " << palpite << endl;

            if (palpite != alvo) {
                cout << "Voce errou! Tente novamente." << endl;
            }
        }
    }
    // Exibindo o resultado final do jogo.
    if (palpite == alvo) {
        cout << "Parabens! Voce venceu!" << endl;
    }
    else {
        cout << "O alvo final foi: " << alvo << endl;
        cout << "Voce perdeu! O computador venceu!" << endl;
    }

    return 0;
}
