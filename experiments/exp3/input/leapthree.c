void func(int t)
{
    int x=2;
    int y=1;
    while(t>0)
    {
        if(x-y==1)
        {
            y+=2;
        }
        else if(y-x==1)
        {
            x+=2;
        }
        t-=1;
    }
    return;
}

int main()
{
    return 0;
}
