#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int C, n, m;
int friends[11][11];
int picked[11];

int dfs(int N,int picked[11], int friends[11][11]){
    int first = -1;
    for (int i=0;i<N;i++){
        if (!picked[i]){
            first = i;
            break;
        }
    }
    // std::cout << first << std::endl;
    if (first == -1){
        return 1;
    }
    int result = 0;
    for (int pair = first+1; pair < N; pair++){
        if (!picked[pair] && friends[first][pair] == 1){
            picked[first] = 1, picked[pair] = 1;
            // std::cout << first << pair << std::endl;
            result += dfs(N, picked, friends);
            picked[first] = 0, picked[pair] = 0;
        }
    }

    return result;
}

int main(){

    std::ifstream ifs;
    ifs.open("PICNIC.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> n >> m;

        for (int i=0;i<n;i++){
            picked[i] = 0;
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

        std::cout << dfs(n,picked,friends) << std::endl;


    }

    return 0;
}