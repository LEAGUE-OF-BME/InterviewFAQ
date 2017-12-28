#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define N 5010
int p[N] ;
int rank[N];
void InitSet(int p[])
{
    for(int i = 0; i<N; i++)
    {
        p[i] = i ;
    }
    memset(rank, 0, sizeof(rank));
}
int Find(int x)             //查(+路径压缩)
{
    if(x != p[x])
        p[x] = Find(p[x]) ;
    return p[x] ;
}
void Union(int x, int y)     //并
{
    int t1 = Find(x) ;
    int t2 = Find(y) ;
    if(t1 > t2)
    {
        p[t1] = t2 ;
        rank[t2]++;
    }
    else if(t1 < t2)
    {
        p[t2] = t1 ;
        rank[t1]++;
    }
    else
        return ;
}
int main()
{
    int n, m, x, y;
    bool flag;
    int gro = 0;
    while(~scanf("%d %d", &n, &m))
    {
        InitSet(p);
        while(m--)
        {
            scanf("%d%d", &x, &y);
            Union(x, y);
        }
        gro = 0;
        flag = true;
        for(int i = 1; i <= n; i++)
        {
            if(rank[i] != 0)
            {
                gro++;
                if((rank[i]+1)%3)
                {
                    flag = false;
                }
            }
        }
        if(n >= 3 && n % 3 == 0 && gro >= 1 && gro <= n/3 && flag)
        {
            printf("Yes\n");
        }
        else
        {
            printf("No\n");
        }
    }
    return 0 ;
}
