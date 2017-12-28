#include <stdio.h>
#define N 7
void Insert_Sort(int a[])//直接插入排序--------时间复杂度:O(n^2)    空间复杂度:O(1)    稳定
{
    for(int i = 1; i<N; i++)
    {
        if(a[i] < a[i-1])
        {
            int j, temp = a[i] ;
            for(j = i-1; a[j] > temp; j--)
            {
                a[j+1] = a[j] ;
            }
            a[j+1] = temp ;
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
    int a[N] = {1,2,7,5,3,4,6} ;
    printf("Before sorting:\n") ;
    Print_Arr(a, N);
    Insert_Sort(a) ;
    printf("After sorting:\n") ;
    Print_Arr(a, N);
    return 0;
}
