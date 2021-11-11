#include <stdio.h>

#define max(a, b) (((a) > (b)) ? (a) : (b))

int main()
{
    int w, l, h;
    int len;
    long long int total = 0;
    while (scanf("%dx%dx%d\n", &w, &l, &h) != EOF)
    {
        len = w + l + h - max(w, max(l, h));
        len <<= 1;
        len += w * l * h;
        total += len;
    }
    printf("%lld\n", total);
    return 0;
}
