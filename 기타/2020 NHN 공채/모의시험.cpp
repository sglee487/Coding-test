#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>

using namespace std;

int N;
int Matrix[10][10];
vector<int> sizev;
int SIZE;
bool dfs(int r, int c){
  if (r < 0 || r >= N || c < 0 || c >= N){
    return false;
  }
  if (Matrix[r][c]==1){
    Matrix[r][c] = 0;
    dfs(r+1,c);
    dfs(r,c+1);
    dfs(r-1,c);
    dfs(r,c-1);
    SIZE++;
    return true;
  }
  return false;

}

void solution(int sizeOfMatrix, int **matrix) {
  // TODO: 이곳에 코드를 작성하세요.
	N = sizeOfMatrix;
  for (int i=0;i < N; i++){
    for (int j=0;j < N; j++){
      Matrix[i][j] = matrix[i][j];
    }
  }
  int count = 0;
  for (int r=0;r < N; r++){
    for (int c=0;c < N; c++){
      SIZE = 0;
      if (dfs(r,c)) {
        count++;
        sizev.push_back(SIZE);
      }
    }
  }
  cout << count << '\n';
  sort(sizev.begin(),sizev.end());
  for (int i=0; i < count;i++){
    cout << sizev[i] << ' ';
  }

}

struct input_data {
  int sizeOfMatrix;
  int **matrix;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.sizeOfMatrix;

  inputData.matrix = new int*[inputData.sizeOfMatrix];
  for (int i = 0; i < inputData.sizeOfMatrix; i++) {
    getline(cin, line);
    iss.clear();
    iss.str(line);
    inputData.matrix[i] = new int[inputData.sizeOfMatrix];
    for (int j = 0; j < inputData.sizeOfMatrix; j++) {
      iss >> inputData.matrix[i][j];
    }
  }
}

int main() {
  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.sizeOfMatrix, inputData.matrix);
  return 0;
}