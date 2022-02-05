#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

int C;


std::string vertical_flip(std::string::iterator& it){
    // 1 2 3 4 가 3 4 1 2 로 바껴야 함.
    char head = *(it++);
    if (head == 'w' or head == 'b')
        return std::string(1, head);
    std::string child_1 = vertical_flip(it);
    std::string child_2 = vertical_flip(it);
    std::string child_3 = vertical_flip(it);
    std::string child_4 = vertical_flip(it);
    return std::string(1, head) + child_3 + child_4 + child_1 + child_2;

}

int main(){

    std::ifstream ifs;
    ifs.open("QUADTREE.txt");

    ifs >> C;
    for (int test_case=0;test_case<C;test_case++){
        std::string word;
        ifs >> word;
        std::string::iterator it = word.begin();
        std::cout << vertical_flip(it) << std::endl;

    }

    return 0;
}