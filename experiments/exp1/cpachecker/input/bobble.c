#include <assert.h>
void start(int t, int b, int c){
    int flag = 1;
    while (t > 0){
        if (flag == 1){
            b += 1;
            c += 1;
            flag = -1;
        }
        else {
            b += 1;
            c -= 1;
            flag = 1;
        }
        t -= 1;
    }
    assert(t == {3});
    assert(b == {4});
    assert(c == {5});
    assert(flag == {6});
}

int main() {
    int t ={0},b={1}, c={2};
    start(t, b, c);
    return 0;
}