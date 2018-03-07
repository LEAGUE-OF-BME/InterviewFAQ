//蚁群算法关于简单的TSP问题求解//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>

#define M 13  //蚂蚁的数量
#define N 52  //城市的数量
#define R 1000 //迭代次数
#define IN 1  //初始化的信息素的量
#define MAX 0x7fffffff //定义最大值

struct coordinate
{
	char city[15];  //城市名
	int x;          //城市相对横坐标
	int y;          //城市相对纵坐标
}coords[N];

double graph[N][N];   //储存城市之间的距离的邻接矩阵,自己到自己记作MAX
double phe[N][N];  //每条路径上的信息素的量
double add[N][N];  //代表相应路径上的信息素的增量
double yita[N][N]; //启发函数,yita[i][j]=1/graph[i][j]

int vis[M][N];  //标记已经走过的城市
int map[M][N];  //map[K][N]记录第K只蚂蚁走的路线
double solution[M]; //记录某次循环中每只蚂蚁走的路线的距离
int bestway[N]; //记录最近的那条路线
double bestsolution=MAX;
int NcMax; //代表迭代次数,理论上迭代次数越多所求的解更接近最优解,最具有说服力
double alpha,betra,rou,Q;

void Initialize(); //信息初始化
void Inputcoords(FILE *fp); //将文件中的坐标信息读入
void GreateGraph(); //根据坐标信息建图
double Distance(int *p); //计算蚂蚁所走的路线的总长度
void Result(); //将结果保存到out.txt中

void Initialize()//初始化参数和迭代次数
{
	alpha=2; betra=4; rou=0.5; Q=50;
    NcMax=R;
	return ;
}
//从文件读入城市坐标
void Inputcoords(FILE *fp)
{
	int i;
	int number;
	if(fp==NULL)
	{
		printf("Sorry,the file is not exist\n");
		exit(1);
	}
	else
	{
		for(i=0; i<N; ++i)
		{
			fscanf(fp,"%d,%d,%d,%s",&number,&coords[i].x,&coords[i].y,coords[i].city);
		}
	}
}
//初始化任意两个城市间的距离
void GreateGraph( )
{
	int i,j;
	double d;
	for(i=0; i<N-1; ++i)
	{
		graph[i][i]=MAX;   //自己到自己标记为无穷大
		for(j=i+1; j<N; ++j)
		{
			d=(double)((coords[i].x-coords[j].x)*(coords[i].x-coords[j].x)+(coords[i].y-coords[j].y)*(coords[i].y-coords[j].y));
			graph[j][i]=graph[i][j]=sqrt(d);
		}
	}
	graph[N-1][N-1]=MAX;
	return ;
}
//计算环路的最小代价
double Distance(int *p)
{
	double d=0;
	int i;
	for(i=0; i<N-1; ++i)
	{
		d+=graph[*(p+i)][*(p+i+1)];
	}
	d+=graph[*(p+i)][*(p)];
	return d;
}
//输出各个结果
void Result()
{
	FILE *fl;
	int i;
	fl = fopen("out.txt","a");  //将结果保存在out.txt这个文件里面
	fprintf(fl,"%s\n","本次算法中的各参数如下:");
	fprintf(fl,"alpha=%.3lf, betra=%.3lf, rou=%.3lf, Q=%.3lf\n",alpha,betra,rou,Q);
	fprintf(fl,"%s %d\n","本次算法迭代次数为:",NcMax);
	fprintf(fl,"%s %.4lf\n","本算法得出的最短路径长度为:",bestsolution);
	fprintf(fl,"%s\n","本算法求得的最短路径为:");
	for(i=0; i<N; ++i)
		fprintf(fl,"%s →  ",coords[bestway[i]].city);
	fprintf(fl,"%s",coords[bestway[0]].city);
	fprintf(fl,"\n\n\n");
	fclose(fl);
	return ;
}

int main()
{
	int NC=0;//迭代次数
	int i,j,k;
	int s;
	double drand,pro,psum;
	FILE *fp;
	Initialize();
	fp = fopen("coords.txt","r+");
	Inputcoords(fp);
	GreateGraph();
	fclose(fp);
	for(i=0; i<N; ++i)//初始化
	{
		for(j=0; j<N; ++j)
		{
			phe[i][j]=IN; //信息素初始化
			if(i!=j)
			yita[i][j]=100.0/graph[i][j];  //期望值,与距离成反比
		}
	}
	memset(map,-1,sizeof(map));  //把蚂蚁走的路线置空
	memset(vis,0,sizeof(vis));  //0表示未访问,1表示已访问
	srand(time(NULL));
	while(NC++<=NcMax)//迭代次数小于等于最大值
	{
		for(k=0; k<M; ++k)
		{
			map[k][0]=(k+NC)%N; //给每只蚂蚁分配一个起点,并且保证起点在N个城市里
			vis[k][map[k][0]]=1; //将起点标记为已经访问，第k个蚂蚁第1个点标记为访问。每个蚂蚁都有一个map
		}
		s=1;//当前每个蚂蚁应该走的第几个城市，下标从0开始，0是每个蚂蚁的起点且已经走过
		while(s<N)
		{
			for(k=0; k<M; ++k)//为第k个蚂蚁选择下一个城市
			{
				psum=0;//Pij（概率）的分母部分，按照公式来计算
				for(j=0; j<N; ++j)
				{
					if(vis[k][j]==0)
					{
						psum+=pow(phe[map[k][s-1]][j],alpha)*pow(yita[map[k][s-1]][j],betra);
					}
				}
				drand=(double)(rand()%5000);
				drand/=5000.0;  //生成一个小于1的随机数（轮盘随机）
				pro=0;//累计的概率之和，当和大于随机数的时候，代表选中当前城市，很形象的模拟
				for(j=0; j<N; ++j)
				{
					if(vis[k][j]==0)
					pro+=pow(phe[map[k][s-1]][j],alpha)*pow(yita[map[k][s-1]][j],betra)/psum;
					if(pro>drand)
					break;
				}
				vis[k][j]=1;  //将走过的城市标记起来（选中j，将j标记）
				map[k][s]=j;  //记录城市的顺序
			}
			s++;
		}//一次迭代完成
		memset(add,0,sizeof(add));
		for(k=0; k<M; ++k)  //计算本次中的最短路径//
		{
			solution[k]=Distance(map[k]);  //蚂蚁k所走的路线的总长度
			if(solution[k]<bestsolution)
			{
				bestsolution=solution[k];
				for(i=0; i<N; ++i)
					bestway[i]=map[k][i];//记录当前最好的路径
			}
		}
		for(k=0; k<M; ++k)
		{
			for(j=0; j<N-1; ++j)//计算路径上信息素的增量
			{
				add[map[k][j]][map[k][j+1]]+=Q/solution[k];
			}
			add[N-1][0]+=Q/solution[k];//首尾相接
		}
		for(i=0; i<N; ++i)
		{
			for(j=0; j<N; ++j)
			{
				phe[i][j]=phe[i][j]*rou+add[i][j];//更新信息素
				if(phe[i][j]<0.0001)  //设立一个下界
					phe[i][j]=0.0001;
				else if(phe[i][j]>20)  //设立一个上界,防止启发因子的作用被淹没
					phe[i][j]=20;
			}
		}
		memset(vis,0,sizeof(vis));
		memset(map,-1,sizeof(map));
	}

	Result();
	printf("Result is saved in out.txt\n");
	return 0;
}
