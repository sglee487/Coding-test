#include <iostream>
#include <sstream>

using namespace std;

void printarr(int arr[],int len){
  for (int i=0;i<len;i++){
    cout << arr[i] << " ";
  }
  cout << '\n';
};

void solution(int day, int width, int **blocks) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
  int blocktall[width];
  for (int i=0;i<width;i++){
    blocktall[i] = 0;
  }
  int semant = 0;
  for (int d=0;d<day;d++){
    for (int j=0;j<width;j++){
      blocktall[j] += blocks[d][j];
    }
    for (int c=0;c<width;c++){
      // left
      int left = c-1;
      for (;left >=0;left--){
        if (blocktall[left] >= blocktall[c]) {
          break;
        }
      }
      // right
      int right=c+1;
      for (;right<width;right++){
        if (blocktall[right] >= blocktall[c]) {
          break;
          }
      }
      // cout << 'l' << left << '\n';
      // cout << 'r' << right << '\n';
      // cout << 'c' << c << '\n';
      // printarr(blocktall,width);
      // cout << semant << '\n';
      // fill left
      if (left >= 0){
        for (int leftf = c-1; leftf>left;leftf--){
          for (int h=blocktall[leftf]; h < blocktall[c]; h++){
            semant++;
            blocktall[leftf]++;
          }
        }
      }
      // fill right
      if (right < width){
        for (int rightf = c+1; rightf<right;rightf++){
          for (int h=blocktall[rightf]; h < blocktall[c]; h++){
            semant++;
            blocktall[rightf]++;
          }
        }
      // cout << 'c' << c << '\n';
      // printarr(blocktall,width);
      // cout << semant << '\n' << '\n';
      }
    }
  }
  cout << semant;
}

struct input_data {
  int day;
  int width;
  int **blocks;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.day;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.width;

  inputData.blocks = new int*[inputData.day];
  for (int i = 0; i < inputData.day; i++) {
    getline(cin, line);
    iss.clear();
    iss.str(line);
    inputData.blocks[i] = new int[inputData.width];
    for (int j = 0; j < inputData.width; j++) {
      iss >> inputData.blocks[i][j];
    }
  }
}

int main() {
	struct input_data inputData;
	process_stdin(inputData);

	solution(inputData.day, inputData.width, inputData.blocks);
	return 0;
}