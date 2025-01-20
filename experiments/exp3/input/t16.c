void func(int x,int y)
{
    int z=0;
    while(x<y)
    {
        x=x-y-1;
        z=100+2*y;
        while(z>0)
        {
            z=z-1;
        }
    }
    return;
}

int main()
{
    return 0;
}