#include <stdio.h>

int main() {
    char word[10000], longest[10000];
    int wlen = 0, maxlen = 0;
    int c;
//Storage chunk
// This chunk stores the current word word[] as well as the longest word longest[]
// The current word length = wlen
// As well as the max length found = maxlen
// c = current character

    while ((c = getchar()) != EOF) {
        if (c != ' ' && c != '\n' && c != '\t') {
            word[wlen++] = c;   
        } else {
// Reading Chunk
// This will loop through each character until EOF
// As well as checking if the char is a space, newline, or tab
// If it is not one of those it adds the current word word[] and increments wlen

            if (wlen > 0) {
                word[wlen] = '\0';     
                if (wlen > maxlen) {
                    maxlen = wlen;
                    for (int i = 0; i <= wlen; i++)
                        longest[i] = word[i]; 
                }
                wlen = 0; 
// This Chunk handles EOF
// If the current word length wlen is greater than 0 it means we have a word to check
// It will also increment/update maxlen and longest[], it then will reset wlen to 0 to start a new word
            }
        }
    }

    
    if (wlen > 0 && wlen > maxlen) {
        word[wlen] = '\0';
        for (int i = 0; i <= wlen; i++)
            longest[i] = word[i];
    }
// This one will check to ensure the last word is counted if no space afterwards
// It does the same as the previous chunk but only if wlen > maxlen
// This chunk is necessary since the last word may not be followed by a space


    printf("%s\n", longest); 
    return 0;
}
// Prints the longest word found in the input