#include <cstdio>
#define VertexNum 10
typedef struct
{
    int vertex[VertexNum];
    int edge[VertexNum][VertexNum];
    int cntv, cnte;
}Graph;
int path[VertexNum][VertexNum];
void Floyd(Graph g, int n)
{
    for(int k = 0; k < n; k++)
    {
        for(int i = 0; i < n; i++)
        {
            for(int j = 0;j < n; j++)
            {
                if(g.edge[i][j] > g.edge[i][k] + g.edge[k][j])
                {
                    g.edge[i][j] = g.edge[i][k] + g.edge[k][j];
                    path[i][j] = k;
                }
            }
        }
    }
}
/*
int main()
{
    Graph g;
    scanf("%d%d", &g.cntv, &g.cnte);
    int n = g.cntv;
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &g.vertex[i]);
    }
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            scanf("%d", &g.edge[i][j]);
        }
    }
    Floyd(g, g.cntv);
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            printf("%d ", g.edge[i][j]);
        }
        printf("\n");
    }
    return 0;
}
*/
