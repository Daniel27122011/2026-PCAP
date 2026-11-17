#include <iostream>
#include <string>

int main() {
    
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);

    const int ledsPorDigito[] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};

    int n;
    if (std::cin >> n) {
        while (n--) {
            std::string valor;
            std::cin >> valor;

            long long totalLeds = 0;
            for (char digito : valor) {

                int num = digito - '0';
                totalLeds += ledsPorDigito[num];
            }
            std:: cout << totalLeds << "leds\n";
        }
    }
    return 0;
}