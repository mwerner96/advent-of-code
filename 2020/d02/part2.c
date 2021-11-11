#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdlib.h>

int main() {
    int lower, upper, n_valid = 0;
    char c, *str, *line;
    size_t len = 0;
    ssize_t read;
    FILE * fp = fopen("input", "r");
    if (fp == NULL) {
        printf("alles kaputt\n");
        exit(1);
    }

    while ((read = getline(&line, &len, fp)) != -1)
    {
        sscanf(line, "%d-%d %c: %s", &lower, &upper, &c, str);
        lower--;
        upper--;
        if ((str[lower] == c || str[upper] == c) && (str[lower] != str[upper]))
            n_valid++;
    }
    printf("%d\n", n_valid);

    fclose(fp);
}
