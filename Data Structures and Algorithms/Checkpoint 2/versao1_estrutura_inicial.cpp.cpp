// Versão para compreender o problema
#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    int bola = rand() % 20 + 1;
    int alvo = bola;
    int palpite;

    cout << "Digite seu palpite: ";
    cin >> palpite;

    cout << "O alvo era: " << alvo << endl;
    cout << "Seu palpite foi: " << palpite << endl;

    while (alvo <= 100 && palpite != alvo) {
        bola = rand() % 20 + 1;
        alvo = alvo + bola;

        if (alvo <= 100) {
    cout << "Digite seu palpite: ";
    cin >> palpite;

    cout << "O alvo era: " << alvo << endl;
    cout << "Seu palpite foi: " << palpite << endl;
        }
    }
        
    if (palpite == alvo) {
        cout << "Parabéns! Você venceu!";
    }
    else {
        cout << "Você perdeu!";
    }
}