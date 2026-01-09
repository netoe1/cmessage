// This file defines the MEssages behavior in app
#ifndef MESSAGE_C
#define MESSAGE_C

#include "Utils.c"
// Define MAX_SIZE for strings used.
#define LIMIT_STR_USERNAME 150 
#define LIMIT_STR_TEXT 500


// Global username to use.
char global_username[LIMIT_STR_USERNAME];

// Define data structure
typedef struct{
    char text[LIMIT_STR_TEXT];
}Message;


void Message_setUsername(Message *ptr,char *username){
    // Copy string to stack. 
    
    int result = Utils_isStrValid(global_username,LIMIT_STR_USERNAME);

    if(result == 1){
        snprintf(global_username,sizeof(global_username),"%s",username);
        return;
    }

    perror("setUsername-err: invalid username to set.");
}

void Message_setText(Message *ptr,char *text){
    int result = Utils_isStrValid(global_username,LIMIT_STR_USERNAME);
}


#endif