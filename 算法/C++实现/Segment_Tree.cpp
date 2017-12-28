#include <cstdio>
const int N = 100010;
int n, p, a, b, m, x, y, ans;
struct node
{
	int l, r, w, f;
}tree[N<<2];
inline void Up(int k)
{
	tree[k].w = tree[k<<1].w + tree[k<<1|1].w;
}
inline void Down(int k)
{
	tree[k<<1].f += tree[k].f;
	tree[k<<1|1].f += tree[k].f;
	tree[k<<1].w += tree[k].f * (tree[k<<1].r-tree[k<<1].l+1);
	tree[k<<1|1].w += tree[k].f * (tree[k<<1|1].r-tree[k<<1|1].l+1);
	tree[k].f = 0;
}
void Build(int l, int r, int k)
{
	tree[k].l = l;
	tree[k].r = r;
	if(tree[k].l == tree[k].r)
	{
		scanf("%d", &tree[k].w);
		return;
	}
	int m = (l + r) >> 1;
	Build(l, m, k<<1);
	Build(m+1, r, k<<1|1);
	Up(k);
}
void Query_point(int k)
{
	if(tree[k].l == tree[k].r)
	{
		ans = tree[k].w;
		return;
	}
	if(tree[k].f)
	{
		Down(k);
	}
	int m = (tree[k].l + tree[k].r) >> 1;
	if(x <= m)
	{
		Query_point(k<<1);
	}
	else
	{
		Query_point(k<<1|1);
	}
}
void Update_point(int k)
{
	if(tree[k].l == tree[k].r)
	{
		tree[k].w += y;
		return;
	}
	if(tree[k].f)
	{
		Down(k);
	}
	int m = (tree[k].l + tree[k].r) >> 1; 
	if(x <= m)
	{
		Update_point(k<<1);
	}
	else
	{
		Update_point(k<<1|1);
	}
	Up(k);
}
void Query_Interval(int k)
{
	if(a <= tree[k].l && b >= tree[k].r)//if(tree[k].l == tree[k].r)
	{
		ans += tree[k].w;
		return;
	}
	if(tree[k].f)
	{
		Down(k);
	}
	int m = (tree[k].l + tree[k].r) >> 1;
	if(a <= m)
	{
		Query_Interval(k<<1);
	}
	if(b > m)
	{
		Query_Interval(k<<1|1);
	}
}
void Update_interval(int k)
{
	if(a <= tree[k].l && b >= tree[k].r)
	{
		tree[k].w += (tree[k].r-tree[k].l+1)*y;
		tree[k].f += y;
		return;
	}
	if(tree[k].f)
	{
		Down(k);
	}
	int m = (tree[k].l + tree[k].r) >> 1;
	if(a <= m)
	{
		Update_interval(k<<1);
	}
	if(b > m)
	{
		Update_interval(k<<1|1);
	}
	Up(k);
}
int main()
{
	scanf("%d", &n);//n nodes
	Build(1, n, 1);
	scanf("%d", &m);//m operations
	for(int i = 1; i <= m; i++)
	{
		scanf("%d", &p);
		ans = 0;
		if(p == 1)
		{
			scanf("%d", &x);
			Query_point(1);//output the xth number
			printf("%d\n", ans);
		}
		else if(p == 2)
		{
			scanf("%d%d", &x, &y);
			Update_point(1);
		}
		else if(p == 3)
		{
			scanf("%d%d", &a, &b);
			Query_Interval(1);
			printf("%d\n", ans);
		}
		else
		{
			scanf("%d%d%d", &a, &b, &y);
			Update_interval(1);
		}
	}
	return 0;
}
