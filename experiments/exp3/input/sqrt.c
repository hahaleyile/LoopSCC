#include "klee/klee.h"

void Success() {}

/* algorithm computing the floor of the square root of a natural number */
int sqrt(int n)
{
    int a, su, t;

    a = 0;
    su = 1;
    t = 1;

    while (su <= n)
    {
        a = a + 1;
        t = t + 2;
        su = su + t;
    }

    return a;
}

int main()
{
    int n;
    int result;
    klee_make_symbolic(&n, sizeof(n), "n");
    klee_assume(n >= 0);
    klee_assume(n <= 10000);
    result = sqrt(n);
    if (result == 201)
        Success();
    return 0;
}
