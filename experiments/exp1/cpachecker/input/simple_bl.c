#include <assert.h>


void start(int t){
    int d=1;
    while(t>0){
        if(d*d==1){
            d=-d;
        } else {
            d=5;
        }
        t --;
    }
    assert(t=={1});
    assert(d=={2});
}


int main() {
    int t={0};
    start(t);
    return 0;
}
