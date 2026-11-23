#include <iostream>
using namespace std;

int main() {
    int numero = 12;
    int palpite;

    cout << "Digite seu palpite: ";
    cin >> palpite;

    while (palpite != numero) {
        if (palpite < numero) {
            cout << "O número é maior. Tente novamente: ";
        } else {
            cout << "O número é menor. Tente novamente: ";
        }
        cin >> palpite;
    }

    cout << "Parabéns! Você acertou o número." << endl;

}