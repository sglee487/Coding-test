#include <iostream>
#include <fstream>
#include <string>
#include <vector>

int C;
int H, W;
char matrix[20][20];
int global_count;

bool is_all_fill(char matrix[20][20]){
    for (int r=0;r<H;r++){
        for (int c=0;c<W;c++){
            if (matrix[r][c] == '.') return false;
        }
    }
    return true;
}

bool can_fit(int r, int c, char matrix[20][20], int type){
    if (r+1>=H || c+1>=W) return false;
    if (type==0){
        // ##
        // #.
        if (matrix[r][c] == '.' && matrix[r][c+1] == '.' && matrix[r+1][c] == '.') return true;
        else return false;
    }else if (type==1){
        // ##
        // .#
        if (matrix[r][c] == '.' && matrix[r][c+1] == '.' && matrix[r+1][c+1] == '.') return true;
        else return false;
    }else if (type==2){
        // .#
        // ##
        if (matrix[r][c+1] == '.' && matrix[r+1][c] == '.' && matrix[r+1][c+1] == '.') return true;
        else return false;
    }else if (type==3){
        // #.
        // ##
        if (matrix[r][c] == '.' && matrix[r+1][c] == '.' && matrix[r+1][c+1] == '.') return true;
        else return false;
    }
    return false;
}

void dfs(int step, char matrix[20][20]){
    int r = step / W; int c = step % W;
    if (step == H*W){
        if (is_all_fill(matrix)) {
            global_count++;
        }
        return;
    }
    if (matrix[r][c] == '#'){
        dfs(step+1, matrix);
    }
    if (can_fit(r,c,matrix,0)){
        matrix[r][c] = '#';
        matrix[r][c+1] = '#';
        matrix[r+1][c] = '#';
        dfs(step+1, matrix);
        matrix[r][c] = '.';
        matrix[r][c+1] = '.';
        matrix[r+1][c] = '.';
    }
    if (can_fit(r,c,matrix,1)){
        matrix[r][c] = '#';
        matrix[r][c+1] = '#';
        matrix[r+1][c+1] = '#';
        dfs(step+1, matrix);
        matrix[r][c] = '.';
        matrix[r][c+1] = '.';
        matrix[r+1][c+1] = '.';
    }
    if (can_fit(r,c,matrix,2)){
        matrix[r][c+1] = '#';
        matrix[r+1][c] = '#';
        matrix[r+1][c+1] = '#';
        dfs(step+1, matrix);
        matrix[r][c+1] = '.';
        matrix[r+1][c] = '.';
        matrix[r+1][c+1] = '.';
    }
    if (can_fit(r,c,matrix,3)){
        matrix[r][c] = '#';
        matrix[r+1][c] = '#';
        matrix[r+1][c+1] = '#';
        dfs(step+1, matrix);
        matrix[r][c] = '.';
        matrix[r+1][c] = '.';
        matrix[r+1][c+1] = '.';
    }
    return;
}

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

        global_count = 0;
        dfs(0,matrix);
        std::cout << global_count << std::endl;

        

    }

    return 0;
}