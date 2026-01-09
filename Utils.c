#ifndef UTILS_C
#define UTILS_C

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <errno.h>
#include <string.h>

// Function to trim strings.
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

// Function to trucate buffers.

void Utils_truncStr(char *str, int limite) {
    if (strlen(str) > limite) {
        str[limite] = '\0';
    }
}


/*
 * Checks whether a string is valid:
 * - is not NULL
 * - is not empty
 * - contains '\0' within the max_len limit
 * - contains only printable ASCII characters
 *
 * Returns:
 *  1 = valid
 *  0 = invalid
 */
int Utils_isStrValid(const char *str, size_t max_len) {
    if (str == NULL || max_len == 0)
        return 0;

    size_t i;

    for (i = 0; i < max_len; i++) {
        if (str[i] == '\0') {
            return (i > 0);  // valid if not empty
        }

        if (!isprint((unsigned char)str[i])) {
            return 0; // invalid character
        }
    }

    // null terminator not found within the limit
    return 0;
}

#endif