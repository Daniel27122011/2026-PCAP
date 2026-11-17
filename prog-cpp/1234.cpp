#include <iostream>
#include <string>
using namespace std;

int main() {
    string linha;

    while (getline(cin, linha)) {
        bool d_s_m = true;
        for (int i = 0; i < linha.length(); i++) {
            if (linha[i] <= 'z') {
                if (d_s_m) {
                    linha[i] = linha[i] - 32;
                }
                d_s_m = !d_s_m;
            }
            else if (linha[i] >= 'A' && linha [i] <= 'Z') {
                if (!d_s_m) {
                    linha[i] = linha[i] + 32;
                }
                d_s_m = !d_s_m;
            }
        }
        cout << linha << endl;
    }

    return 0;
}