#include <assert.h>
void start(int i, int x, int flag) {
    while (i<100) {
        if(flag!=0){
            if (x > 5) {
                x = x - 5;
                i = i + 3;
            } else {
                x =x+2;
                i = i+7;
            }
        } else {
            x = x-7;
            flag = 1;
        }
    }
    assert(i=={3});
    assert(x=={4});
    assert(flag=={5});
}

int main() {
    int i ={0},x={1}, flag={2};
    start(i, x,flag);
    return 0;
}
