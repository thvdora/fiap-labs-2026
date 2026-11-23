#include <iostream>
#include <iomanip>
using namespace std;

struct Data {
    int dia;
    int mes;
    int ano;
};

// Data &data: a função acessa a variável original. As alterações são mantidas fora da função.
void lerData(Data &data, string identificacao) {
    cout << "\nDigite a " << identificacao << " data:\n";
    cout << "Dia: ";
    cin >> data.dia;

    cout << "Mes: ";
    cin >> data.mes;

    cout << "Ano: ";
    cin >> data.ano;
}

// Função para formatar a data 
void formatarData(Data data) {
    cout << setw(2) << setfill('0') << data.dia << "/" << setw(2) << setfill('0') << data.mes << "/" << setfill('0') << data.ano << endl;
}

// Função para comparar data A e data B
void compararDatas(Data dataA, Data dataB) {
    if (dataA.ano < dataB.ano){
        cout << "A primeira data é a mais antiga." << endl;
    }
    else if (dataA.ano == dataB.ano && dataA.mes < dataB.mes) {
        cout << "A primeira data é a mais antiga." << endl;
    }
    else if (dataA.ano == dataB.ano && dataA.mes == dataB.mes && dataA.dia < dataB.dia) {
        cout << "A primeira data é a mais antiga." << endl;
    }
    else if (dataA.ano == dataB.ano && dataA.mes == dataB.mes && dataA.dia == dataB.dia) {
        cout << "As datas são as mesmas." << endl;
    }
    else {
    cout << "A segunda data é a mais antiga." << endl;
    }   
}

int main() {
    Data dataA, dataB;

    lerData(dataA, "primeira");
    lerData(dataB, "segunda");

    formatarData(dataA);
    formatarData(dataB);

    compararDatas(dataA, dataB);
}