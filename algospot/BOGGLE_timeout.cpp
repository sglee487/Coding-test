#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int TEST_CASES;
int N;
int candi_num;
char matrix[5][5];
std::string candidates[11];
std::string answers[11];

// 위 위오 오 오아 아 아왼 왼 왼위
std::vector<int> dy = {-1,-1,0,1,1,1,0,-1};
std::vector<int> dx = {0,1,1,1,0,-1,-1,-1};

bool is_possible(std::string word, char matrix[][5]);
bool dfs(int step, int r, int c, std::string word);

bool is_possible(std::string word, char matrix[][5]){
    for (int r=0;r<5;r++){
        for (int c=0;c<5;c++){
            if (word[0] == matrix[r][c]){
                if (dfs(1,r,c,word)) return true;
            }
        }
    }
    return false;
}

bool dfs(int step, int r, int c, std::string word){
    if (step == word.length()){
        return true;
    }
    bool result = false;
    for (int i=0;i<8;i++){
        int nr = r + dy[i];
        int nc = c + dx[i];
        if (0<=nr<5 && 0<=nc<5){
            if (word[step] == matrix[nr][nc]){
                if (dfs(step+1,nr,nc,word)) return true;
            }
        }
    }
    return false;
}


int main(){

    std::ifstream ifs;
    ifs.open("BOGGLE.txt");

    ifs >> TEST_CASES;

    for (int test_case=0; test_case<TEST_CASES; test_case++){
        for (int i=0; i<5;i++){
                ifs >> matrix[i];
            }

        ifs >> candi_num;
        for (int i=0; i<candi_num; i++){
            ifs >> candidates[i];
        }

        for (int cand=0; cand<candi_num; cand++){
            if (is_possible(candidates[cand], matrix)) {
                std::cout << candidates[cand] << " YES" << std::endl;
            }
            else std::cout << candidates[cand] << " NO" << std::endl;
        }


    }
    return 0;
}