#include <stdio.h>
#define N 7
void Swap(int a[], int p1, int p2)//交换数据
{
    int temp = a[p1] ;
    a[p1] = a[p2] ;
    a[p2] = temp ;
}
void Simple_Selection_Sort(int *a, int n)//简单选择排序-------时间复杂度:O(n^2)   空间复杂度:O(1)    稳定
{
    for(int i = 0; i < n; i++)
    {
        int min = i ;
        for(int j = i+1; j < n; j++)
        {
            if(a[min] > a[j])
                min = j ;
        }
        if(min-i)
            Swap(a, i, min) ;
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
    int a[N] = {1,7,3,5,6,2,4} ;
    printf("Before sorting:\n") ;
    Print_Arr(a, N);
    Simple_Selection_Sort(a, N);
    printf("After sorting:\n") ;
    Print_Arr(a, N);
    return 0 ;
}
