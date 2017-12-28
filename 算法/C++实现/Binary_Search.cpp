#include <stdio.h>
#include <algorithm>
using namespace std;
const int N = 7;
int Binary_Search(int a[], int low, int high, int key)//二分查找
{
    while(low <= high)
    {
        int mid = (low+high)/2;
        if(a[mid] == key)
        {
            return mid;
        }
        else if(a[mid] > key)
        {
            high = mid -1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return -1;
}
int main()
{
    int a[N] = {1,4,6,9,22,34,100};//数组元素可自定义
    int n;
    //sort(a, a+N);
    while(1)
    {
        printf("Search number:");
        scanf("%d", &n);
        if(!n)//输入0表示不再查询，循环终止
        {
            break;
        }
        if(Binary_Search(a, 0, N-1, n) == -1)
        {
            printf("No such a number!\n");
            continue;
        }
        printf("The position of number %d is %d\n", n, Binary_Search(a, 0, N-1, n)+1);
    }
    return 0;
}


//-------------------------------------------------------------------------------------------------------------------------------------
#include <stdio.h>
const int N = 10;
int Binary_Search(int a[], int low, int high, int key)//二分查找
{
    while(low <= high)
    {
        int mid = (low+high)/2;
        if(a[mid] == key)
        {
            return mid;
        }
        else if(a[mid] > key)
        {
            high = mid -1;
        }
        else
        {
            low = mid + 1;
        }
    }
    return -1;
}
int main()
{
	int a[N], n;
	for(int i = 0; i < N; i++)
	{
		a[i] = i;
	}
	char *name[N] = {"Xu", "Li", "Zhang", "Chen", "He", "Liu", "Zhu", "Zhao", "Zhu", "Wu"};
	while(1)
	{
		printf("Input the student number:");
		scanf("%d", &n);
		n %= 10;
		n = Binary_Search(a, 0, N-1, n);
		printf("Name: %s\n", name[n]);
	}
	return 0;
}
