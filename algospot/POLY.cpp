#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C, N, S;
int cache[101][101];

const int MOD = 10000000;

int poly(int remain, int pre_blocks){
    if (remain == pre_blocks) return 1;
    int &ret = cache[remain][pre_blocks];
    if (ret != -1) return ret;
    ret = 0;
    for (int cur_blocks = 1; cur_blocks <= remain - pre_blocks; cur_blocks++){
        int add = pre_blocks + cur_blocks - 1;
        add *= poly(remain - pre_blocks, cur_blocks);
        add %= MOD;
        ret += add;
        ret %= MOD;
    }

    return ret;
}

int solve(int n){
    int result = 0;
    for (int i=1;i<=n;i++)
        result += poly(n, i);
        result %= MOD;
    return result;
}

int main(){

    std::ifstream ifs;
    ifs.open("POLY-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> N;
        memset(cache, -1, sizeof(cache));
        std::cout << solve(N) << std::endl;
    }

    return 0;
}