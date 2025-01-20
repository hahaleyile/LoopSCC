void func(int x,int y,int det)
{
    while(x>0)
    {
        x=x-1;
        if(det>0)
        {
            y=y+1;
        }
        else
        {
            while(y>0)
            {
                y=y-1;
            }
        }
    }
    return;
}

int main()
{
    return 0;
}
