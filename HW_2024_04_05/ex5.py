with open('input.txt', 'r', encoding='utf-8') as inp_file:
    content = inp_file.readlines()

with open('output.txt', 'w', encoding='utf-8') as out_file:
    for i, line in enumerate(content, start=1):
        out_file.write(f'{i}){line}')

############################################

# 1)abcd
# 2)xcnvmnvkje
# 3)32432423
# 4)sdflsdjkn34r43
# 5)345349854395#$%$#
# 6)jksdfkjsdfkjsd
# 7)lwerjlwerlkwe
# 8)jwfhjkwehkjwefkjwebfjkwe
# 9)djdddddddddddddddddddddddddddddddd
# 10)3249835438594390583490583490853490582349058340
# 11)sdfsjkldflksdjaflkjsdflkjsdlfkjsdlfjsldfsldkfjlsdkfjls