#include <stdio.h>
#define N 7
void Quick_Sort(int s[], int l, int r)//快速排序--------时间复杂度:O(n*logn)   空间复杂度:O(logn)   不稳定
{
    if(l < r)
    {
        int i = l, j = r, x = s[l];
        while(i < j)
        {
            while(i < j && s[j] >= x)
            {
                j--;
            }
            if(i < j)
            {
                s[i++] = s[j];
            }
            while(i < j && s[i] < x)
            {
                i++;
            }
            if(i < j)
            {
                s[j--] = s[i];
            }
        }
        s[i] = x;
        Quick_Sort(s, l, i-1);
        Quick_Sort(s, i+1, r);
    }
}
void Print_Arr(int *a, int n)
{
    for(int i = 0; i < n; i++)
    {
        if(i)
            printf(" ") ;
        printf("%d", a[i]) ;
        if(i == n-1)
            printf("\n") ;
    }
}
int main()
{
    int s[N] = {1,7,5,2,4,3,6};
    printf("Before sorting:\n") ;
    Print_Arr(s, N);
    Quick_Sort(s, 0, N-1);
    printf("After sorting:\n") ;
    Print_Arr(s, N);
    return 0;
}
