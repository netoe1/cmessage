// This file defines the MEssages behavior in app
#ifndef MESSAGE_C
#define MESSAGE_C

// Define MAX_SIZE for strings used.
#define LIMIT_STR_USERNAME 150 
#define LIMIT_STR_TEXT 500

// Define data structure
typedef struct{
    char username[LIMIT_STR_USERNAME];
    char text[LIMIT_STR_TEXT];
}Message;


void Message_setUsername(char *username);
void Message_setText(char *text);
#endif