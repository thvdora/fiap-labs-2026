#include <iostream> 
using namespace std; 
int main() 

{ 

    int notas[5] = {7, 8, 6, 9, 10}; 

    int soma = 0; 

    for(int i = 0; i < 5; i++) 

    { 

        soma += notas[i]; 

    } 

    double media = soma / 5.0; 

    cout << "Media = " << media << endl; 

    return 0; 

} 