#include "klee/klee.h"

void Success() {}

/* algorithm for computing simultaneously the GCD and the LCM, by Dijkstra */
int lcm(int a, int b)
{
    int x, y, u, v;

    x = a;
    y = b;
    u = b;
    v = a;

    while (x != y)
    {
        if (x > y)
        {
            x = x - y;
            v = v + u;
        }
        else
        {
            y = y - x;
            u = u + v;
        }
    }

    return (u + v) / 2;
}

int main()
{
    int a, b;
    klee_make_symbolic(&a, sizeof(a), "a");
    klee_make_symbolic(&b, sizeof(b), "b");
    klee_assume(a > 0);
    klee_assume(a < 100);
    klee_assume(b > 0);
    klee_assume(b < 100);
    int result = lcm(a,b);
    if (result == 37)
        Success();
    return 0;
}
