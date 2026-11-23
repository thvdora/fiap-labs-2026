#include <iostream>
#include <vector>
#include <string>
#include <limits>
#include <windows.h>
#include <algorithm>
using namespace std;

// Estruturando dados
struct Ocorrencia {
    string categoria;
    string regiao;
};
vector<Ocorrencia> listaDeOcorrencias;

void listarOcorrencias() {
    if (listaDeOcorrencias.empty()) {
        cout << "Não há ocorrências registradas!" << endl;
        return;
    }
    cout << "\n--- TODAS AS OCORRÊNCIAS ---" << endl;
    for (int i = 0; i < listaDeOcorrencias.size(); i++) {
        cout << i + 1 << ") Categoria: " << listaDeOcorrencias[i].categoria << endl;
        cout << "   Região:    " << listaDeOcorrencias[i].regiao << endl;
        cout << "-----------------------------" << endl;
    }
}

// Limpa o buffer após leituras com cin 
void limparBuffer() {
    cin.ignore((numeric_limits<streamsize>::max)(), '\n');
}

// VALIDAÇÕES
bool validarEntrada(int& numero) {
    cin >> numero;

    if (cin.fail()) {
        cin.clear();
        limparBuffer();
        cout << "Opção inválida!" << endl;
        return false;
    }

    limparBuffer();
    return true;
}
bool validarRegistros() {
    if (listaDeOcorrencias.empty()) {
        cout << "Não há ocorrências registradas!" << endl;
        return false;
    }

    return true;
}

void ordenarOcorrencias();

void registrarOcorrencia() {
    Ocorrencia novaOcorrencia;

    cout << "Digite a categoria: ";
    getline(cin, novaOcorrencia.categoria);

    cout << "Digite a região da ocorrência: ";
    getline(cin, novaOcorrencia.regiao);

    listaDeOcorrencias.push_back(novaOcorrencia);
    ordenarOcorrencias();
    cout << "Ocorrência cadastrada com sucesso!" << endl;
}

void mostrarMenu() {
    cout << "\n====================================" << endl;
    cout << "      MENU OCORRÊNCIAS URBANAS" << endl;
    cout << "====================================" << endl;
    cout << "1 - Cadastrar ocorrência" << endl;
    cout << "2 - Listar todas as ocorrências" << endl;
    cout << "3 - Buscar por categoria" << endl;
    cout << "4 - Buscar por região" << endl;
    cout << "5 - Estatísticas" << endl;
    cout << "0 - Sair" << endl;
    cout << "Escolha uma opção: ";
}


// FUNÇÕES DE BUSCA
void buscarPorCategoria() {
    if (!validarRegistros()) {
        return;
    }
    string categoriaAlvo;
    bool encontrou = false;

    cout << "Digite a categoria desejada: ";
    getline(cin, categoriaAlvo);

    cout << "\n--- Regiões com ocorrências de \"" << categoriaAlvo << "\" ---" << endl;
    for (size_t i = 0; i < listaDeOcorrencias.size(); i++) {
        if (listaDeOcorrencias[i].categoria == categoriaAlvo) {
            cout << " • " << listaDeOcorrencias[i].regiao << endl;
            encontrou = true;
        }
    }
    if (!encontrou) {
        cout << "Não foram encontrados registros!" << endl;
    }
}
void buscarPorRegiao() {
    if (!validarRegistros()) {
        return;
    }

    string regiaoAlvo;
    bool encontrou = false;

    cout << "Digite a região desejada: ";
    getline(cin, regiaoAlvo);

    cout << "\n--- Categorias registradas em \"" << regiaoAlvo << "\" ---" << endl;
    for (int i = 0; i < listaDeOcorrencias.size(); i++) {
        if (listaDeOcorrencias[i].regiao == regiaoAlvo) {
            cout << " • " << listaDeOcorrencias[i].categoria << endl;
            encontrou = true;
        }
    }

    if (!encontrou) {
        cout << "Não foram encontrados registros!" << endl;
    }
}

// FUNÇÕES DE ESTATÍSTICAS
void totalOcorrencias() {
    cout << "\n===== TOTAL DE OCORRÊNCIAS =====" << endl;

    cout << "Total de registros cadastrados: "
         << listaDeOcorrencias.size() << endl;

    cout << "================================" << endl;
}
void totalCategorias() {
    int contador = 0;

    cout << "\n===== OCORRÊNCIAS POR CATEGORIA =====" << endl;
    
    for (int i = 0; i < listaDeOcorrencias.size(); i ++) {
        bool jaContabilizada = false;
        
        for (int j = 0; j < i; j++) {
            if (listaDeOcorrencias[i].categoria == listaDeOcorrencias[j].categoria) {
                jaContabilizada = true;
            }
        }
        if (jaContabilizada == false) {
            contador = 0;
            for (int k = 0; k < listaDeOcorrencias.size(); k++) {
                if (listaDeOcorrencias[i].categoria == listaDeOcorrencias[k].categoria){
                    contador++;
                }
            }
            cout << listaDeOcorrencias[i].categoria << ": " << contador << endl;
        }
    }
    cout << "====================================" << endl;
}
void totalRegioes() {
    int contador = 0;

    cout << "\n===== OCORRÊNCIAS POR REGIÃO =====" << endl;
    
    for (int i = 0; i < listaDeOcorrencias.size(); i ++) {
        bool jaContabilizada = false;
        
        for (int j = 0; j < i; j++) {
            if (listaDeOcorrencias[i].regiao == listaDeOcorrencias[j].regiao) {
                jaContabilizada = true;
            }
        }
        if (jaContabilizada == false) {
            contador = 0;
            for (int k = 0; k < listaDeOcorrencias.size(); k++) {
                if (listaDeOcorrencias[i].regiao == listaDeOcorrencias[k].regiao){
                    contador++;
                }
            }
            cout << listaDeOcorrencias[i].regiao << ": " << contador << endl;
        }
    }
    cout << "==================================" << endl;
}
void mostrarEstatisticas() {
    if (!validarRegistros()) {
        return;
    }

    totalOcorrencias();
    totalCategorias();
    totalRegioes();
}

// Colocando em ordem alfabética por categoria e em seguida, por região
void ordenarOcorrencias() {
    sort(
        listaDeOcorrencias.begin(), 
        listaDeOcorrencias.end(),
        [](const Ocorrencia& a, const Ocorrencia&  b) {
            if (a.categoria != b.categoria){
                return a.categoria < b.categoria;
            }
            else {
                return a.regiao < b.regiao;
            }
        }
    );
}

int main() {
    // Apenas para configurar os caracteres especiais no meu terminal
    SetConsoleOutputCP(CP_UTF8);
    SetConsoleCP(CP_UTF8);

    int inicio;
    int opcao;
    int voltar;

    cout << "Digite 10 para visualizar o menu ou 0 para sair." << endl;

    if (!validarEntrada(inicio)) {
        return 0;
    }

    if (inicio == 10) {
        do {
            mostrarMenu();

            if (!validarEntrada(opcao)) {
                opcao = -1;
                continue;
            }

            switch (opcao) {
                case 1: registrarOcorrencia(); break;
                case 2: listarOcorrencias();   break;
                case 3: buscarPorCategoria();  break;
                case 4: buscarPorRegiao();     break;
                case 5: mostrarEstatisticas(); break;
                case 0: cout << "Encerrando o programa..." << endl; break;
                default: cout << "Opção inválida!" << endl; break;
            }

            if (opcao != 0) {
                do {
                    cout << "\nDigite 10 para voltar ao menu ou 0 para sair: ";

                    if (!validarEntrada(voltar)) {
                        voltar = -1;
                        continue;
                    }

                    if (voltar != 10 && voltar != 0) {
                        cout << "Opção inválida! Digite apenas 10 ou 0." << endl;
                    }
                
                } while (voltar != 10 && voltar != 0);

                if (voltar == 0) {
                    cout << "Encerrando o programa..." << endl;
                    opcao = 0;
                }
            }
        } while (opcao != 0);
    }
    else if (inicio != 0) {
        cout << "Opção inválida!" << endl;
    }
}