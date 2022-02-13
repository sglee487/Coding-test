#include <iostream>
#include <fstream>
#include <string>
#include <string.h>
#include <vector>
#include <map>

#include <algorithm>

int C, N;
std::string word;
std::string cands[51];
int dp[101][101];

int is_char_matching(int n_step, int m_step, std::string word, std::string cand){
    int &ret = dp[n_step][m_step];
    if (ret != -1)
        return ret;

    if ((n_step == word.size() && m_step == cand.size()))
        return ret = 1;
    if (n_step < word.size() && m_step < cand.size() && 
        (word[n_step] == cand[m_step] || word[n_step] == '?'))
        return ret = is_char_matching(n_step+1, m_step+1, word, cand);
    if (word[n_step] == '*')
        return ret = ((m_step < cand.size() && is_char_matching(n_step, m_step+1, word, cand))
            || (is_char_matching(n_step+1, m_step, word, cand)));
    
    return ret = 0;
}

bool is_match(std::string word, std::string cand){
    memset(dp, -1, sizeof(dp));
    return is_char_matching(0,0,word, cand) == 1;
}

std::vector<std::string> solve(std::string word, std::string cands[]){
    std::vector<std::string> answers;

    for (int i=0;i<N;i++){
        if (is_match(word, cands[i]))
            answers.push_back(cands[i]);
    }

    return answers;

}

int main(){

    std::ifstream ifs;
    ifs.open("WILDCARD-1.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        ifs >> word;
        ifs >> N;
        for (int i=0;i<N;i++)
            ifs >> cands[i];
        std::vector<std::string> answers = solve(word, cands);
        std::sort(answers.begin(), answers.end());
        for (int i=0; i<answers.size();i++)
            std::cout << answers[i] << std::endl;

    }

    return 0;
}