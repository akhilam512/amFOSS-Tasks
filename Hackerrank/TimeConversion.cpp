#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the timeConversion function below.
 */


int main()
{
    

    char c;

    int hh,mm,ss;
    
    
    scanf("%d:%d:%d%c", &hh, &mm, &ss, &c);
    
    if(c=='P'&&hh!=12) //only PM requires conversion, AM is left as it is.
        hh+=12;
    else if((c=='A'||c=='P')&&hh==12) // 0000
        hh=0;
   
    

    printf("%02d:%02d:%02d\n", hh,mm,ss) ;

   

    return 0;
}
