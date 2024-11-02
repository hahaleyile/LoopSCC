#include <assert.h>

void start(int i0, int det) {
    int i = i0;
    int n = 100;
    int j;
    while (i < n) {
        while (j < n) {
            if (det) {
                j = j - 1;
                n = n - 1;
            }
            j = j + 1;
        }
        i = i + 1;
    }
    assert(i == {2});
    assert(n == {3});
    assert(j == {4});
}

int main() {
    int i = {0};
    int det = {1};
    start(i, det);
    return 0;
}
