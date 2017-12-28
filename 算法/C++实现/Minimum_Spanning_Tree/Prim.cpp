#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#define MAX 999
#define VNUM 5
using namespace std;
int edge[VNUM][VNUM];
int lowcost[VNUM] = {0};
int addvnew[VNUM];
int adjecent[VNUM] = {0};
void Prim(int start)
{
	int sumweight = 0;
	int i, j, k = 0;
	for(i = 1; i < VNUM; i++)
	{
		lowcost[i] = edge[start][i];
		addvnew[i] = -1;
	}
	addvnew[start] = 0;
	/*for(i = 1; i < VNUM; i++)//初始化adjecent数组
	{
		adjecent[i] = start;
	}*/
	fill(adjecent, adjecent+VNUM, start);
	for(i = 1; i < VNUM-1; i++)
	{
		int min = MAX;
		int v = -1;
		for(j = 1; j < VNUM; j++)
		{
			if(addvnew[j] == -1 && lowcost[j] < min)
			{
				min = lowcost[j];
				v = j;
			}
		}
		if(v != -1)
		{
			printf("%d %d %d\n", adjecent[v], v, lowcost[v]);
			addvnew[v] = 0;
			sumweight += lowcost[v];
			for(j = 1; j < VNUM; j++)
			{
				if(addvnew[j] == -1 && edge[v][j] < lowcost[j])
				{
					lowcost[j] = edge[v][j];
					adjecent[j] = v;
				}
			}
		}
	}
	printf("The minmum weight is %d\n", sumweight);
}
int main()
{
	for(int i = 1; i < VNUM; i++)
	{
		for(int j = 1; j < VNUM; j++)
		{
			scanf("%d", &edge[i][j]);
		}
	}
	Prim(1);
	return 0;
}
