
参考: http://qiemengdao.iteye.com/blog/1660229


//DP:
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define len(a) (sizeof(a) / sizeof(a[0])) //数组长度
int lis1(int arr[], int len)//最长递增子序列
{
    int longest1[len];
    for (int i=0; i<len; i++)
    {
        longest1[i] = 1;
    }
    for (int j=1; j<len; j++)
    {
        for (int i=0; i<j; i++) 
        {
            if (arr[j]>arr[i] && longest1[j]<longest1[i]+1)
            { //注意longest[j]<longest[i]+1这个条件，不能省略。
                longest1[j] = longest1[i] + 1; //计算以arr[j]结尾的序列的最长递增子序列长度
            }
        }
    }
    int mmax = 0;
    for (int j=0; j<len; j++)
    {
        if (longest1[j] > mmax) 
        {
            mmax = longest1[j]; 
        } //从longest[j]中找出最大值
    }
    return mmax;
}
int lis2(int arr[], int len)//最长递减子序列
{
    int longest2[len];
    for (int i=0; i<len; i++)
    {
        longest2[i] = 1;
    }
    for (int j=1; j<len; j++) 
    {
        for (int i=0; i<j; i++) 
        {
            if (arr[j]<arr[i] && longest2[j]<longest2[i]+1)
            { //注意longest[j]<longest[i]+1这个条件，不能省略。
                longest2[j] = longest2[i] + 1; //计算以arr[j]结尾的序列的最长递增子序列长度
            }
        }
    }
    int mmax = 0;
    for (int j=0; j<len; j++)
    {
        if (longest2[j] > mmax) 
        {
            mmax = longest2[j]; 
        } //从longest[j]中找出最大值
    }
    return mmax;
}
int main()
{
    int t, n;
    int arr[100010];
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &arr[i]);
        }
        if(n - max(lis1(arr, n), lis2(arr, n)) <= 1)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}



//二分查找优化:
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <algorithm>
#define N 100010
#define INF 0x3f3f3f3f
using namespace std;
int len, a[N], aa[N], b[N];
int BiSearch(int *b, int len, int w)
{
    int left = 0, right = len-1;
    int mid;
    while(left <= right)
    {
        mid = (right + left) / 2;
        if(b[mid] > w)
        {
            right = mid - 1;
        }
        else
        {
            left = mid + 1;
        }
    }
    return left;
}
int lis(int array[], int n)
{
    len = 1;
    memset(b, INF, sizeof(b));
    b[0] = array[0];
    int i, pos = 0;
    for(i = 1; i < n; i++)
    {
        if(array[i] >= b[len-1])
        {
            b[len] = array[i];
            len++;
        }
        else
        {
            pos = BiSearch(b, len, array[i]);
            b[pos] = array[i];
        }
    }
    return len;
}
/*
int main()
{
    int t, n;
    scanf("%d", &t);
    while(t--)
    {
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%d", &a[i]);
            aa[n - i - 1] = a[i];
        }
        if(n - max(lis(a, n), lis(aa, n)) <= 1)
        {
            printf("YES\n");
        }
        else
        {
            printf("NO\n");
        }
    }
    return 0;
}
*/
