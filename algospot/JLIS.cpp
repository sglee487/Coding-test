#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C;
int N, M;
int A[101], B[101];
int cache[102][102];

const long long NEGINF = std::numeric_limits<long long>::min();

int jlis(int starta, int startb){
    int& ret = cache[starta+1][startb+1];
    if (ret != -1) return ret;
    ret = 2;
    long long a = (starta == -1 ? NEGINF : A[starta]);
    long long b = (startb == -1 ? NEGINF : B[startb]);
    long long maxEle = std::max(a,b);
    for (int nexta = starta+1; nexta < N; nexta++)
        if (maxEle < A[nexta])
            ret = std::max(ret, jlis(nexta, startb)+1);
    for (int nextb = startb+1; nextb < M; nextb++)
        if (maxEle < B[nextb])
            ret = std::max(ret, jlis(starta, nextb)+1);
    return ret;
}


int main(){

    std::ifstream ifs;
    ifs.open("JLIS-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> N >> M;
        for (int i=0;i<N;i++)
            ifs >> A[i];
        for (int i=0;i<M;i++)
            ifs >> B[i];
        memset(cache, -1, sizeof(cache));
        std::cout << jlis(-1,-1)-2 << std::endl;
        

    }

    return 0;
}