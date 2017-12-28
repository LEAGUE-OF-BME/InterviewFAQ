#include <stdio.h>
#define N 7
void Bubble_Sort(int *a, int n)//冒泡排序-----时间复杂度:O(n^2)   空间复杂度:O(1)    稳定
{
    for(int i = 0; i < n; i++)
    {
        for(int j = i+1; j < n; j++)
        {
            if(a[i] > a[j])
            {
                int temp = a[i] ;
                a[i] = a[j] ;
                a[j] = temp ;
            }
        }
    }
}
void Print_Arr(int *a, int n)
{
    for(int i = 0; i<N; i++)
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
    int a[N] = {1,7,5,4,2,3,6} ;
    printf("Before sorting:\n") ;
    Print_Arr(a, N);
    Bubble_Sort(a, N);
    printf("After sorting:\n") ;
    Print_Arr(a, N);
    return 0 ;
}
