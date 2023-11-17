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