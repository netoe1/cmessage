#ifndef UTILS_C
#define UTILS_C
#include <ctype.h>
#include <string.h>

void Utils_trimStr(char *str) {
    int inicio = 0;
    int fim = strlen(str) - 1;

    // Remove espaços do início
    while (isspace(str[inicio])) {
        inicio++;
    }

    // Remove espaços do fim
    while (fim >= inicio && isspace(str[fim])) {
        fim--;
    }

    // Desloca os caracteres para o começo
    int i = 0;
    while (inicio <= fim) {
        str[i++] = str[inicio++];
    }

    str[i] = '\0';
}

void Utils_truncStr(char *str, int limite) {
    if (strlen(str) > limite) {
        str[limite] = '\0';
    }
}

#endif