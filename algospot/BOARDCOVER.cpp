#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int C;

int main(){

    std::ifstream ifs;
    ifs.open("BOARDCOVER.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        std::cout << test_case << std::endl;


    }

    return 0;
}