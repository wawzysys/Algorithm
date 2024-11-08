
# a = 'CompletionMessage(content=\''
# b = '\', role=\'assistant\', tool_calls=None)'
# c = '\\n'
# print(c)
# print(len(a))
# print(len(b))
# s = input()
# s = s[len(a):-len(b)]
# for c in s:
#     print(c)
# print(s)
content = input()
content = content.replace('CompletionMessage(content=\'', '')
content = content.replace('\', role=\'assistant\', tool_calls=None)', '')
content = content.replace('\\n', '')
print(content)
