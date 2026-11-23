#include <iostream> 
#include <vector> 
using namespace std; 

int main() { 

    vector<string> alunos; // é possível criar direto ao invés de adicionar por pushback

    alunos.push_back("Ana"); 
    alunos.push_back("Carlos"); 
    alunos.push_back("Marcos"); 

    for(int i = 0; i < alunos.size(); i++) { 

        cout << alunos[i] << endl; 

    } 
    
    return 0; 

} 