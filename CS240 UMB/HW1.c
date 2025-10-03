#include <stdio.h>

// Helper function to check for whitespace characters
static int is_space(int c) {
    return c==' ' || c=='\t' || c=='\n' || c=='\r' || c=='\v' || c=='\f';
}

// Prints a number digit by digit using putchar
static void put_digits(unsigned long n) {
    if (n >= 10) put_digits(n / 10);       // print higher places first
    putchar((int)('0' + (n % 10)));        // then the last digit
}

int main(void) {
    int c;
    unsigned long chars = 0, words = 0;
    int in_word = 0;          
    //Tracks variables current char, counter, and words and flages if we are isnide a word

    while ((c = getchar()) != EOF) {
        //Reach each character until EOF
        if (!is_space(c)) {          
            //If it's not a whitespace it coounts as a char       
            chars++;
            if (!in_word) {             
                in_word = 1;
                words++;
                //If we just ented a word it bumps the word count
            }
        } else {
            in_word = 0;  
            //If the char is a whitespace, we mark that were not inside a word                  
        }
    }

    
    put_digits(chars); putchar('\n');
    put_digits(words); putchar('\n');
    //prints the char count on first line and word on second line
    //hopefully this is ok to use since we are not using certain variables
    return 0;
    //ends program
}