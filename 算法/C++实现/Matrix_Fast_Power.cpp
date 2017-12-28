#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
const int N = 10;
typedef long long lint;
int k , MOD;
int arr[N] , f[N];
struct Matrix
{
    lint mat[N][N];
    Matrix operator*(const Matrix &m)const
    {
        Matrix tmp;
        for(int i = 0 ; i < N ; i++)
        {
            for(int j = 0 ; j < N ; j++)
            {
                tmp.mat[i][j] = 0;
                for(int k = 0 ; k < N ; k++)
                {
                    tmp.mat[i][j] += mat[i][k]*mat.m[k][j]%MOD;
                    tmp.mat[i][j] %= MOD;
                }
            } 
        }
        return tmp;
    }
};

lint Pow(Matrix &m , int k)
{
    Matrix ans;
    memset(ans.mat , 0, sizeof(ans.mat));
    for(int i = 0 ; i < N ; i++)
        ans.mat[i][i] = 1;
    k -= 9;
    while(k)
    {
        if(k & 1)
           ans = ans*m;
        k >>= 1;
        m = m*m;
    } 
    lint sum = 0;
    for(int i = 0 ; i < N ; i++)
    {
        sum += ans.mat[0][i]*f[N-i-1]%MOD;
        sum %= MOD;
    }
    return sum;
}
void init(Matrix &m)
{
    memset(mat.m , 0 , sizeof(mat.m));
    for(int i = 0 ; i < N ; i++)
    {
        mat.m[0][i] = arr[i];
        f[i] = i;
        if(i != N-1)
        {
        	mat.m[i+1][i] = 1;
        }
    }   
}
int main()
{
    Matrix m;
    while(scanf("%d%d" , &k , &MOD) != EOF)
    {
        for(int i = 0 ; i < N ; i++)
        {
            scanf("%d" , &arr[i]);
        }
        init(m);
        if(k < 10)
        {
            printf("%d\n" , k%MOD);
        }
        else
        {
            printf("%lld\n" , Pow(m ,k));
        }
    }
    return 0;
}
