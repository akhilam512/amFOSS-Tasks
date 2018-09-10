#include <bits/stdc++.h>

using namespace std;

vector<string> split_string(string);

// Complete the miniMaxSum function below.
void miniMaxSum(vector<int> a) {  
    
    int n=a.size(),p=0;
    long s=0,result[n];    
    for(unsigned int i=1; i<a.size(); i++) //finding sum in first iteration excluding element a[0]
    {
     	s+=a[i];
        
    }

    result[p++]=s;//storing sum into result array
    
    for(unsigned int j=1; j<a.size(); j++)
    {   
   	    s=s-a[j]+a[j-1]; //using the same sum and removing the element currently present from sum and adding element which was not included in previous iterations
        
        result[p++]=s;   // i.e. storing each possible sum 
    }

    long max=result[0], min=result[0]; //finding min and max of result array.
	
    for(auto it: result)
    {	if(it>max)
            max=it;
     
        if(it<min)
            min=it;
    }
    
    
    cout<<min<<' '<<max<<endl;
}



int main()
{
    string arr_temp_temp;
    getline(cin, arr_temp_temp);

    vector<string> arr_temp = split_string(arr_temp_temp);

    vector<int> arr(5);

    for (int i = 0; i < 5; i++) {
        int arr_item = stoi(arr_temp[i]);

        arr[i] = arr_item;
    }

    miniMaxSum(arr);

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
