#include <bits/stdc++.h>

using namespace std;

// SOLUTION
void staircase(int n) {
    
    int i,j;
    for(i=0;i<n;i++)
    {
        for(j=i+1;j<n;j++)
            cout<<' ';
        
        for(j=n-i;j<=n;j++)
            cout<<'#';
        
        cout<<endl;
        
        
    }


}

// END OF SOLUTION

int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    staircase(n);

    return 0;
}
