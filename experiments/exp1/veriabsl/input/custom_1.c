#include <assert.h>
void start(int i, int x) {
    while (i<100) {
        if (x > 1) {
            x = x + 1;
            i = i + 3;
        } else if (x < -1) {
            x = x+1;
            i = i+5;
        } else {
            x =x+1;
            i = i+7;
        }
    }
    assert(i=={2});
    assert(x=={3});
}

int main() {
    int i ={0},x={1};
    start(i, x);
    return 0;
}
