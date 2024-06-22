#include<iostream>

using namespace std;

int main(){
    int n1, n2, suma = 0;

    cout << "Digite un numero: "; 
    cin >> n1;
    cout << "Digite un numero mas, por favor: "; 
    cin >> n2;

    suma = n1 + n2;

    cout << "La suma de los dos numeros es: " << suma << endl;

    return 0;
}