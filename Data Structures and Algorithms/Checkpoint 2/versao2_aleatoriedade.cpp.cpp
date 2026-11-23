// Variando os sorteios testando bibliotecas diferentes
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0)); //Semente da sequência pseudoaleatória.
    
    int bola = rand() % 20 + 1;
    int alvo = bola;
    int palpite;

    cout << "Digite seu palpite: ";
    cin >> palpite;

    cout << "O alvo era: " << alvo << endl;
    //2cout << "Seu palpite foi: " << palpite << endl;


    if (palpite != alvo) {
        cout << "Você errou! Tente novamente." << endl;
    }

    while (alvo <= 100 && palpite != alvo) {
        bola = rand() % 20 + 1;
        alvo = alvo + bola;

        if (alvo <= 100) {
            cout << "Digite seu palpite: ";
            cin >> palpite;

            cout << "O alvo era: " << alvo << endl;
            //cout << "Seu palpite foi: " << palpite << endl;

        
            if (palpite != alvo) {
                cout << "Você errou! Tente novamente." << endl;
            }
        }
    }
        
    if (palpite == alvo) {
        cout << "Parabéns! Você venceu!";
    }
    else {
        cout << "Você perdeu!";
    }

    return 0;
}