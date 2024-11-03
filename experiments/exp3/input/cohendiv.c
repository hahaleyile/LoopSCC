#include "klee/klee.h"

void Success() { }

/* integer division algorithm, by Cohen */
int division(int x, int y)
{
    int q, r;

    q = 0;
    r = x;

    while (r >= y)
    {

        int d, dd;

        d = 1;
        dd = y;

        while (r >= 2 * dd)
        {
            d = 2 * d;
            dd = 2 * dd;
        }
        r = r - dd;
        q = q + d;
    }

    return r;
}

int main()
{
    int x, y;
    int result;
    klee_make_symbolic(&x, sizeof(x), "x");
    klee_make_symbolic(&y, sizeof(y), "y");
    klee_assume(x >= 0);
    klee_assume(x <= 100);
    klee_assume(y >= 0);
    klee_assume(y <= 100);
    result = division(x, y);
    if (result == 37)
        Success();
    return 0;
}
