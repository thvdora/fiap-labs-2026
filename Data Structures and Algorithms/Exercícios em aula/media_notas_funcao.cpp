#include <iostream>
using namespace std;

float calcularMedia(float nota1, float nota2) {
    return (nota1 + nota2) / 2;
}

int main() {
    float nota1, nota2;

for (int i = 1; i <= 5; i++) {
    cout << "Aluno " << i << endl;

    cout << "Digite a primeira nota: ";
    cin >> nota1;

    cout << "Digite a segunda nota: ";
    cin >> nota2;

    float media = calcularMedia(nota1, nota2);
    cout << "Media do aluno " << i << ": " << media << endl;
}
}