#include <stdio.h>
int GCD(int n, int m)
{
    return n % m == 0 ? m : GCD(m, n % m);
}
int main()
{
    int n, m;
    while(scanf("%d%d", &n, &m) && n && m)
    {
        printf("The Greatest Common Divisor of %d and %d is %d\n", n, m, GCD(n, m));
    }
    return 0;
}
