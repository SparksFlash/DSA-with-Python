#include <bits/stdc++.h>
using namespace std;
int main()
{
   vector<int> v;
   for (int i = 0; i < v.size(); i++)
   {
      int nums;
      cin >> nums;
         v.push_back(nums);
      }

   for (int x : v)
      cout << x;
}