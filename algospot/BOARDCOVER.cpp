#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int C;
int H, W;
char matrix[20][20];

int main(){

    std::ifstream ifs;
    ifs.open("BOARDCOVER.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        
        ifs >> H >> W;

        for (int h=0;h<H;h++){
            for (int w=0;w<W;w++){
                ifs >> matrix[h][w];
            }
        }

        

    }

    return 0;
}