#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C, N, S;
int cache[101];

int MOD = 1000000007;

int tiling(int n){
    if (n <= 1) return 1;
    int &ret = cache[n];
    if (ret != -1) return ret;
    
    return ret = (tiling(n-2) + tiling(n-1)) % MOD;
}

int asymtiling(int n){
    if ((n % 2) == 1){
        return (tiling(n)+MOD - tiling(n/2))%2;
    } else{
        int result = tiling(n);
        result = (result - tiling(n/2) + MOD) % MOD;
        result = (result - tiling((n/2)-1) + MOD) % MOD;
        return result;
    }
}

int main(){

    std::ifstream ifs;
    ifs.open("ASYMTILING-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> N;
        memset(cache, -1, sizeof(cache));
        std::cout << asymtiling(N) << std::endl;
    }

    return 0;
}