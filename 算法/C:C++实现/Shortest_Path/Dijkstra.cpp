#include <cstdio>
#include <cstring>
#include <algorithm>
#define M 0x3f3f3f3f
#define N 1010
using namespace std;
int map[N][N];//城市之间的邻接矩阵表示法
int dist[N];//  起点到各个点的最短路径
int pre[N];//存储最短路径
bool vis[N];//标记是否访问过
int t, s, d;
int a, b, tim;
int nn, minn;
void Dijkstra(int v0)//计算单源最短路径, v0为起点
{
    for(int i = 1; i <= nn; i++)//初始化
    {
        dist[i] = map[v0][i];
        vis[i] = false;//所有城市都未访问过
        if(dist[i] == M)
        {
            pre[i] = -1;//与起点之间没有路径，设它的前一座城市为-1, 否则就是起点
        }
        else
        {
            pre[i] = v0;
        }
    }
    dist[v0] = 0;//起点到自身的距离为0
    vis[v0] = true;//标记为访问过
    for(int i = 2; i <= nn; i++)
    {
        minn = M;
        int pos = v0;
        for(int j = 1; j <= nn; j++)//寻找已存在路径中的最短路径
        {
            if(!vis[j] && dist[j] < minn)
            {
                minn = dist[j];
                pos = j;
            }
        }
        vis[pos] = true;//加入到访问过的集合中去
        for(int j = 1;j <= nn; j++)//松弛---经过pos这座城市且以之为中心点的最短路径
        {
            if(!vis[j] && map[pos][j] < M)
            {
                if(dist[pos] + map[pos][j] < dist[j])
                {
                    dist[j] = dist[pos] + map[pos][j];
                    pre[j] = pos;
                }
            }
        }
    }
}
/*
int main()
{
    while(~scanf("%d%d%d", &t, &s, &d))
    {
        nn = 0;
        memset(map, M, sizeof(map));
        for(int i = 0; i < t; i++)
        {
            scanf("%d%d%d", &a, &b, &tim);
            nn = max(nn, max(a, b));
            map[a][b] = map[b][a] = min(tim, map[a][b]);
        }
        for(int i = 0; i < s; i++)
        {
            scanf("%d", &a);
            map[0][a] = 0;
        }
        int m = M;
        Dijkstra(0);
        for(int i = 0; i < d; i++)
        {
            scanf("%d", &a);
            m = min(m, dist[a]);
        }
        printf("%d\n", m);
    }
    return 0;
}
*/
