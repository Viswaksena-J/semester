%{
#include<stdio.h>
int no_lines = 0, no_words = 0, no_chars = 0, no_other_char = 0, totalchar = 0;
%}

%%
\n      { no_lines++; no_words++; }
[\t ' ']    no_words++;
[A-Za-z0-9]    no_chars++;
.       no_other_char++; 
%%

int main(int argc, char **argv) {
    ++argv; --argc; /* skip over program name */
    if (argc > 0)
        yyin = fopen(argv[0], "r");
    else
        yyin = stdin;

    yylex();

    totalchar = no_chars + no_other_char;

    printf("\n------ Result ------\n");
    printf("Number of lines: %d\n", no_lines);
    printf("Number of words: %d\n", no_words);
    printf("Number of alphanumeric characters: %d\n", no_chars);
    printf("Number of other characters: %d\n", no_other_char);
    printf("Total number of characters: %d\n", totalchar);
}

int yywrap() {
    return 1;
}
