#include <assert.h>

void start(int x, int y) {
    while (100 > x) {
        if (30 > y) {
            y = y + 1;
        } else {
            x = x + 1;
        }
    }
    assert(x == {2});
    assert(y == {3});
}

int main() {
    int x = {0};
    int y = {1};
    start(x, y);
    return 0;
}