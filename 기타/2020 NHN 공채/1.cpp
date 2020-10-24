#include <iostream>
#include <sstream>
#include <vector>
#include <cstring>
#include <map>

using namespace std;

void printarr(int *arr[],int len){
  for (int i=0;i<len;i++){
    cout << arr[i] << " ";
  }
  cout << '\n';
};

void printvector(vector<char> &v1, int len)
{
  for (int i=0;i<len;i++){
    cout << v1[i] << " ";
  }
  cout << '\n';
}

bool ishefast(char he, char *namesOfQuickPlayers, int len){
  for (int i=0;i < len;i++){
    if (((int)he - (int)namesOfQuickPlayers[i]) == 0){
      return true;
    }
  }
  return false;
}

void solution(int numOfAllPlayers, int numOfQuickPlayers, char *namesOfQuickPlayers, int numOfGames, int *numOfMovesPerGame) {
  // TODO: 이곳에 코드를 작성하세요. 추가로 필요한 함수와 전역변수를 선언해서 사용하셔도 됩니다.
  vector<char>table;
  map<char,int> mcount;
  mcount.insert(make_pair('A',1));
  for (int i=66; i < 66+numOfAllPlayers-1;i++){
    table.push_back((char)i);
    mcount.insert(make_pair((char)i,0));
  }
  char loser = 'A';
  int startpoint = 0;
  // printvector(table, numOfAllPlayers);
  for (int numofgame = 0; numofgame < numOfGames; numofgame++){
    int tmpstart = (startpoint + numOfMovesPerGame[numofgame]) % (numOfAllPlayers-1);
    if (tmpstart < 0){
      startpoint = numOfAllPlayers - 1 + tmpstart;
    } else{
      startpoint = tmpstart;
    }
    // cout << startpoint << '\n';
    char fsp = table[startpoint];
    if (ishefast(fsp,namesOfQuickPlayers,numOfQuickPlayers)){

    } else{
      table.erase(table.begin()+startpoint);
      table.insert(table.begin()+startpoint,loser);
      loser = fsp;
    }
    mcount[loser]++;
    // printvector(table, numOfAllPlayers);
  }

  for (int i=0;i < numOfAllPlayers-1;i++){
    cout << table[i] << ' ' << mcount[table[i]] << '\n';
  }
  cout << loser << ' ' << mcount[loser];
}

struct input_data {
  int numOfAllPlayers;
  int numOfQuickPlayers;
  char *namesOfQuickPlayers;
  int numOfGames;
  int *numOfMovesPerGame;
};

void process_stdin(struct input_data& inputData) {
  string line;
  istringstream iss;

  getline(cin, line);
  iss.str(line);
  iss >> inputData.numOfAllPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfQuickPlayers;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.namesOfQuickPlayers = new char[inputData.numOfQuickPlayers];
  for (int i = 0; i < inputData.numOfQuickPlayers; i++) {
    iss >> inputData.namesOfQuickPlayers[i];
  }

  getline(cin, line);
  iss.clear();
  iss.str(line);
  iss >> inputData.numOfGames;

  getline(cin, line);
  iss.clear();
  iss.str(line);
  inputData.numOfMovesPerGame = new int[inputData.numOfGames];
  for (int i = 0; i < inputData.numOfGames; i++) {
    iss >> inputData.numOfMovesPerGame[i];
  }
}

int main() {
  struct input_data inputData;
  process_stdin(inputData);

  solution(inputData.numOfAllPlayers, inputData.numOfQuickPlayers, inputData.namesOfQuickPlayers, inputData.numOfGames, inputData.numOfMovesPerGame);
  return 0;
}