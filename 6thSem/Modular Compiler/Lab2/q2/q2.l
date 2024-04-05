%{
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
%}

letter [a-zA-Z]
digit [0-9]

%%
"int"|"char"|"float"|"if"|"printf"    { printf("%s is a keyword\n", yytext); }
"+"|"-"|"*"|"/"|"^"|"="|"++"          { printf("%s is an operator\n", yytext); }
","|";"|"{"|"}"|"("|")"               { printf("%s is a special character\n", yytext); }
{digit}+                              { printf("%s is a number\n", yytext); }
{letter}({letter}|{digit})*           { printf("%s is an identifier\n", yytext); }
[ \t\n]+                              /* ignore whitespace */
\"[^\"\n]*\"                          { printf("%s is a string\n", yytext); } /* identify strings */
.                                     { printf("Error\n"); } /* ignore other characters */
%%

int main(int argc, char **argv) {
    ++argv, --argc; /* skip over program name */
    if (argc > 0)
        yyin = fopen(argv[0], "r");
    else
        yyin = stdin;
    yylex();
}

int yywrap() {
    return 1;
}
