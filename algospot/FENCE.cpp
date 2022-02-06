#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

int C;
int nl[20001];

int solve(int left, int right, int heights[]){
    if (left == right) return heights[left];
    int mid = (left + right) / 2;
    int ret = std::max(solve(left, mid, heights), solve(mid+1, right, heights));
    // 중간부터 펼쳐나가며 큰거로 확장.
    int lm = mid, rm = mid+1;
    int height = std::min(heights[lm], heights[rm]);
    ret = std::max(ret, 2*height);
    while (left < lm || rm < right){
        if (left < lm && (rm == right || heights[lm-1] > heights[rm+1]))
            height = std::min(height, heights[--lm]);
        else
            height = std::min(height, heights[++rm]);
        ret = std::max(ret, height * (rm - lm + 1));
    }
    return ret;
}

int main(){

    std::ifstream ifs;
    ifs.open("FENCE-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        int N;
        ifs >> N;
        for (int i=0;i<N;i++)
            ifs >> nl[i];
        std::cout << solve(0, N-1, nl) << std::endl;

    }

    return 0;
}