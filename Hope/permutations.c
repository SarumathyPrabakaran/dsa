#include<stdio.h>
#include<stdlib.h>

void swap(char a[], int l, int r){
    char temp;
    temp = a[l];
    a[l] = a[r];
    a[r] = temp;
   
}

void permutate(char* str, int l, int r){
    
    if(l==r-1){
        printf("%s\n",str);
        return;
    }
    
    for(int index=l;index<r;index++){
        swap(str, l, index);
        permutate(str,l+1,r);
        swap(str, l, index);
    }
    
}
enna pa ippove dowry ah..apro naane othuka maaten..paathuko
/*
1) Tambaram la 2 ground villa drawing- 1
2) toy Benz car - 2
3) Rs. 100
4) 1 month world tour package plan.

romba nallavan apdiye..paakathana poran..



ok..appo nee vettiya tha irupa..velaiku pona enta yen keka pora..so vetti ya lam kalyanam pannika mudiyathu man..kelambu..
enga veetlayum same solluvanga..

..
 athu evlo nu  kooda therla.....no wayy
*/
int main()
{
    char str[11];
    int n;

    scanf("%s",str);
    n = strlen(str);
    printf("%d",n);
    permutate(str, 0, n);

    printf("test");
}