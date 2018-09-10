#include <bits/stdc++.h>

using namespace std;

// SOLUTION
int diagonalDifference(vector<vector<int>> a) {
    
    int s1,s2; s1=s2=0;
    for(int i=0,j=a.size()-1;i <a.size(); i++, j--)
    {
        s1+=a[i][i];   
        s2+=a[i][j];
        
        
    }
    
    return abs(s1-s2);


}
// SOLUTION ENDS

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<vector<int>> a(n);
    for (int i = 0; i < n; i++) {
        a[i].resize(n);

        for (int j = 0; j < n; j++) {
            cin >> a[i][j];
        }

        cin.ignore(numeric_limits<streamsize>::max(), '\n');
    }

    int result = diagonalDifference(a);

    fout << result << "\n";

    fout.close();

    return 0;
}
