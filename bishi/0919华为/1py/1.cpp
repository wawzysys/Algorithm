#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_EXPRESSIONS 100
#define MAX_KEY_VALUE_PAIRS 100
#define MAX_LINE_LENGTH 1000

typedef struct
{
    char key[MAX_LINE_LENGTH];
    char value[MAX_LINE_LENGTH];
} KeyValuePair;

int is_empty(const char *line)
{
    while (*line != '\0')
    {
        if (!isspace(*line))
        {
            return 0;
        }
        line++;
    }
    return 1;
}

void trim(char *str)
{
    char *end;

    // Trim leading space
    while (isspace((unsigned char)*str))
        str++;

    if (*str == 0) // All spaces?
        return;

    // Trim trailing space
    end = str + strlen(str) - 1;
    while (end > str && isspace((unsigned char)*end))
        end--;

    // Write new null terminator character
    *(end + 1) = '\0';
}

int main()
{
    int n, m;
    char line[MAX_LINE_LENGTH];

    // Read n and m
    fgets(line, sizeof(line), stdin);
    trim(line);
    sscanf(line, "%d %d", &n, &m);

    // Read expressions
    char expressions[MAX_EXPRESSIONS][MAX_LINE_LENGTH];
    for (int i = 0; i < n; i++)
    {
        fgets(line, sizeof(line), stdin);
        trim(line);
        while (is_empty(line))
        {
            fgets(line, sizeof(line), stdin);
            trim(line);
        }
        strcpy(expressions[i], line);
    }

    // Read key-value pairs
    KeyValuePair data[MAX_KEY_VALUE_PAIRS];
    for (int i = 0; i < m; i++)
    {
        fgets(line, sizeof(line), stdin);
        trim(line);
        while (is_empty(line))
        {
            fgets(line, sizeof(line), stdin);
            trim(line);
        }
        sscanf(line, "%s %s", data[i].key, data[i].value);
    }

    // Process each expression
    for (int i = 0; i < n; i++)
    {
        char expr[MAX_LINE_LENGTH];
        strcpy(expr, expressions[i]);

        // Replace AND and OR
        char *pos;
        while ((pos = strstr(expr, "AND")) != NULL)
        {
            strncpy(pos, "&&", 2);
            strcpy(pos + 2, pos + 3);
        }
        while ((pos = strstr(expr, "OR")) != NULL)
        {
            strncpy(pos, "||", 2);
            strcpy(pos + 2, pos + 2);
        }

        // Replace key ='value' with data[key] == 'value'
        char *key, *value;
        char *temp = strdup(expr);
        char *token = strtok(temp, " ");
        while (token != NULL)
        {
            if ((key = strstr(token, "='")) != NULL)
            {
                *key = '\0';
                key += 2;
                value = strchr(key, '\'');
                if (value != NULL)
                {
                    *value = '\0';
                    value++;
                    char replacement[MAX_LINE_LENGTH];
                    snprintf(replacement, sizeof(replacement), "data['%s'] == '%s'", token, key);
                    char *start = strstr(expr, token);
                    int len = strlen(replacement);
                    memmove(start + len, start + strlen(token), strlen(start + strlen(token)) + 1);
                    memcpy(start, replacement, len);
                }
            }
            token = strtok(NULL, " ");
        }
        free(temp);

        // Evaluate the expression
        int result = 1; // Default to 1 if evaluation fails
        for (int j = 0; j < m; j++)
        {
            char *pos = strstr(expr, data[j].key);
            if (pos != NULL)
            {
                char replacement[MAX_LINE_LENGTH];
                snprintf(replacement, sizeof(replacement), "data['%s'] == '%s'", data[j].key, data[j].value);
                int len = strlen(replacement);
                memmove(pos + len, pos + strlen(data[j].key), strlen(pos + strlen(data[j].key)) + 1);
                memcpy(pos, replacement, len);
            }
        }

        // Print the result
        printf("%d\n", result);
    }

    return 0;
}