#include <assert.h>
#include <stdio.h>

#define tos stack[sp - 1]
#define STACKSIZE 1024

typedef long long stack_t;

stack_t stack[STACKSIZE];
int sp = 0;

static inline void push(stack_t x)
{
    stack[sp++] = x;
}

static inline stack_t pop()
{
    return stack[--sp];
}

static inline void reduce()
{
    stack_t val = pop();
    stack_t op = pop();
    tos = op == '*' ? tos * val : tos + val;
}

stack_t calc_line()
{
    char tok = getchar();
    if (tok == EOF)
        return -1;
    do
    {
        switch (tok)
        {
        case '(': // enter nesting in stack
            push(0);
            push('+');
            break;
        case ')': // leave nesting in stack
            reduce();
            break;
        case '*':
        case '+':
            if (sp > 1) // before pushing next op, resolve pending operation
                reduce();
            push(tok);
            break;
        case ' ': // skip spaces
            break;
        default: // always push digits, result is calculated later; digits are only possible remaining (sane) input
            push(tok - '0');
            break;
        }
    } while ((tok = getchar()) != '\n');
    if (sp > 1) // only theoretically need this for trivial input lines (one single number)
        reduce();
    return pop();
}

int main()
{
    stack_t sum = 0;
    stack_t res;
    while ((res = calc_line()) != -1)
        sum += res;
    assert(!sp);
    printf("%lld\n", sum);
    return 0;
}
