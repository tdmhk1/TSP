#include <iostream>
#include <vector>
#include <algorithm>

int main(){
  int n;
  std::cin >> n;
  std::vector<int> route;
  for(int i=1; i<n; i++){
    route.push_back(i);
  }

  double dist[n][n];
  for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
      std::cin >> dist[i][j];
    }
  }

  double min = 10000000;
  std::vector<int> min_route = route;
  do{
    double total = 0;
    total += dist[0][route[0]];
    for(int i=0; i<route.size(); i++){
      total += dist[route[i]][route[i+1]];
    }
    total += dist[route[n-1]][0];

    if (total < min) {
      min = total;
      min_route = route;
    }
  }while(next_permutation(route.begin(), route.end()));

  std::cout << "0";
  for(auto i : min_route) {
    std::cout << " " << i;
  }
  std::cout << std::endl;

  std::cout << min << std::endl;

  return 0;
}
