#include <stdio.h>
#define N 7
void Shell_Sort1(int a[], int n)//希尔排序--------时间复杂度:O(n*logn)~O(n*n)   空间复杂度:O(1)   不稳定
{
    int i, j, gap;
    for(gap = n /2; gap > 0; gap /= 2)//增量
    {
        for(i = 0; i < gap; i++)//直接插入排序
        {
            for(j = i + gap; j < n; j += gap)
            {
                if(a[j] < a[j - gap])
                {
                    int temp = a[j];
                    int k = j - gap;
                    while(k >= 0 && a[k] > temp)
                    {
                        a[k + gap] = a[k];
                        k -= gap;
                    }
                    a[k + gap] = temp;
                }
            }
        }
    }
}
void Shell_Sort2(int a[], int n)
{
    int i, gap;
    for(gap = n /2; gap > 0; gap /= 2)
    {
        for(i = gap; i < n; i++)
        {
            if(a[i] < a[i - gap])//每个元素与自己组内的数据进行直接插入排序
            {
                int temp = a[i];
                int k = i - gap;
                while(k >= 0 && a[k] > temp)
                {
                    a[k + gap] = a[k];
                    k -= gap;
                }
                a[k + gap] = temp;
            }
        }
    }
}
void Shell_Sort3(int a[], int n)
{
    int i, j, gap;
    for(gap = n / 2; gap > 0; gap /= 2)
    {
        for(i = gap; i < n; i++)
        {
            for(j = i - gap; j >= 0 && a[j] > a[j + gap]; j -= gap)
            {
                int temp = a[j];
                a[j] = a[j + gap];
                a[j + gap] = temp;
            }
        }
    }
}
void Print_Arr(int a[], int n)
{
    for(int i = 0; i < n; i++)
    {
        if(i)
        {
            printf(" ");
        }
        printf("%d", a[i]);
        if(i == n-1)
        {
            printf("\n");
        }
    }
}
int main()
{
    int a[N] = {1, 7, 5, 3, 4, 6, 2};
    printf("Before sorting:\n") ;
    Print_Arr(a, N);
    Shell_Sort1(a, N);
    //Shell_Sort2(a, N);
    //Shell_Sort3(a, N);
    printf("After sorting:\n") ;
    Print_Arr(a, N);
    return 0;
}
