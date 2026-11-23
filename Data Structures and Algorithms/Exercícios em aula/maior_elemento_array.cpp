#include <iostream> 
using namespace std; 

int main() {
    int numbers[10] = {3, 5, 16, 19, 6, 22, 4, 10, 8, 11};
    int maior = numbers[0];

    for(int i = 0; i < 10; i++) 
    {
        if(numbers[i] > maior){
            maior = numbers[i];
        }
    }
    cout << numbers << endl;
    cout << "O maior elemento: " << maior << endl;
}