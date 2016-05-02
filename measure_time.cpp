#include <ctime>
#include <iostream>

int main(){
  clock_t begin = clock();
  
  int a = 0;
  for(int i=0; i<10000000; i++) {
    a += i;
  }

  clock_t end = clock();
  double elapsed_secs = double(end - begin) / CLOCKS_PER_SEC;
  
  std::cout << elapsed_secs << "sec" << std::endl;

  return 0;
}
