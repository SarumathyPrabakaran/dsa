#include<stdio.h>
#include<stdlib.h>

void swap(char a[], int l, int r){
    char temp;
    temp = a[l];
    a[l] = a[r];
    a[r] = temp;
   
}

int permutate(char* str, int l, int r, int x, int ans){
    int intstr, diff, diff2;
    if(l==r-1){
        printf("%s\n",str);
         intstr = atoi(str);
        return intstr;
    }
    
    for(int index=l;index<r;index++){
        swap(str, l, index);
         intstr = permutate(str,l+1,r,x,ans);
         diff = abs(intstr-x);
         diff2 = abs(ans-x);
        
        if(diff<diff2){
            printf("\n%d ans is %d\n",ans, intstr);
            ans = intstr;
        }
        
        swap(str, l, index);
    }
    return ans;
}

int main()
{
char str[11];
int n, x;

scanf("%s",str);
scanf("%d",&x );
n = strlen(str);

int ans =  permutate(str, 0, n, x, atoi(str));
printf("%d\n\n\n", ans);

printf("test");
}