#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int C, n, m;
int friends[11][11];

int dfs(int step,int N,int friends[11][11]){
    for (int i=step; i<N; i++){

    }
}

int main(){

    std::ifstream ifs;
    ifs.open("PICNIC.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> n >> m;

        for (int i=0;i<n;i++){
            for (int j=0;j<n;j++){
                friends[i][j] = 0;
            }
        }

        for (int i=0;i<m;i++){
            int a, b;
            ifs >> a >> b;
            friends[a][b] = 1;
            friends[b][a] = 1;
        }

        std::cout << dfs(0,n,friends) << std::endl;


    }

    return 0;
}