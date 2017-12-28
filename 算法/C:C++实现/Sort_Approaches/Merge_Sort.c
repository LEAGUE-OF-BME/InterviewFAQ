#include <stdio.h>
#include <stdlib.h>
#define N 7
void Merge(int a[], int low, int mid, int high)//合并
{
    int left_low = low ;
    int left_high = mid ;
    int right_low = mid+1 ;
    int right_high = high ;
    int *temp = (int *)malloc((high-low+1)*sizeof(int)) ;
    int k = 0 ;
    for(;left_low <= left_high && right_low <= right_high;)
    {
        if(a[left_low] < a[right_low])
        {
            temp[k++] = a[left_low++] ;
        }
        else
        {
            temp[k++] = a[right_low++] ;
        }
    }
    while(left_low <= left_high)
    {
        temp[k++] = a[left_low++] ;
    }
    while(right_low <= right_high)
    {
        temp[k++] = a[right_low++] ;
    }
    for(int i = 0; i<high-low+1; i++)
    {
        a[low+i] = temp[i] ;
    }
    free(temp) ;
}
void Merge_Sort(int a[], int start, int end)//归并排序-------时间复杂度:O(n*logn)   空间复杂度:O(n)    稳定
{
    if(start < end)
    {
        int mid = (start+end)/2 ;
        Merge_Sort(a, start, mid) ;
        Merge_Sort(a, mid+1, end) ;
        Merge(a, start, mid, end) ;
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
    int a[N] = {1,4,3,2,5,7,6} ;
    printf("Before sorting:\n") ;
    Print_Arr(a, N);
    Merge_Sort(a, 0, N-1) ;
    printf("After sorting:\n") ;
    Print_Arr(a, N);
    return 0;
}
