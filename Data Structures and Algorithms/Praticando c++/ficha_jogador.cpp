#include <iostream>
#include <string>
using namespace std;

int main() {
    string nome;
    int idade;
    float altura;
    float pontuacao;
    bool status;

    cout << "Digite seu nome: ";
    getline(cin, nome);

    cout << "Qual a sua idade? ";
    cin >> idade;

    cout << "Qual a sua altura? ";
    cin >> altura;

    cout << "Qual a pontuação do jogador? ";
    cin >> pontuacao;

    cout << "O jogador está ativo? (1 para sim, 0 para não): ";
    cin >> status;

    cout << "\n--- Dados do jogador ---\n";
cout << "Nome: " << nome << endl;
cout << "Idade: " << idade << endl;
cout << "Altura: " << altura << " m" << endl;
cout << "Pontuacao: " << pontuacao << endl;

    if (status) {
        cout << "Ativo.";
    }
    else {
        cout << "Inativo.";
    }
}