#include <assert.h>

void start(int x, int y) {
    int z;
    while (x > y) {
        x = x - y - 1;
        z = 100 + 2 * y;
        while (z > 0) {
            z = z - 1;
        }
    }
    assert(x == {2});
    assert(z == {3});
}

int main() {
    int x = {0};
    int y = {1};
    start(x, y);
    return 0;
}
