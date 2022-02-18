#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C;
int N;
std::string numstr;
int cache[10002];

int INF = 987654321;

int difficulty(int index_A, int index_B){
    std::string substr = numstr.substr(index_A, (index_B-index_A)+1);
    if (substr == std::string(substr.size(),substr[0])) return 1;
    bool is_step = true;
    for (int i=0; i<substr.size()-1;i++)
        if (substr[i+1] - substr[i] != substr[1] - substr[0]) 
            is_step = false;
    if (is_step && abs(substr[0] - substr[1]) == 1)
        return 2;
    bool is_alter = true;
    for (int i=2; i<substr.size();i++)
        if (substr[i] != substr[i-2]) 
            is_alter = false;
    if (is_alter) return 4;
    if (is_step) return 5;
    return 10;
}


int dp(int start){ 
    if(start == N) return 0;
    int &ret = cache[start];
    if(ret != -1) return ret;
    ret = INF;
    for (int size=3; size <= 5; size++)
        if (start + size <= N)
            ret = std::min(ret, dp(start + size) + 
                                difficulty(start, start+size-1));
    return ret;
}

int main(){

    std::ifstream ifs;
    ifs.open("PI-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> numstr;
        N = numstr.size();
        for (int i=0;i<N;i++) cache[i] = -1;

        std::cout << dp(0) << std::endl;


    }

    return 0;
}