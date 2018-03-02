#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> result;
        string temp;
        for(int i=1; i <= n; i++){
            temp = "";
            if(i % 3 == 0)
                temp += "Fizz";
            if(i % 5 == 0)
                temp += "Buzz";
            if(temp == "")
                temp = to_string(i);
            result.push_back(temp);
        }
        return result;
        
    }
};

int main(){
   Solution A = Solution();
   vector<string> v = A.fizzBuzz(20);
   string temp;
   while(!v.empty()){
	temp = v.back();
	v.pop_back();
	cout << temp << '\n';
   }
}