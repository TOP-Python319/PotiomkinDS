
d = {}
s = input().split()
while s != []:
    d1 = {s[0]:s[1]}
    d.update(d1)
    s = input().split()

item_of_search = input('Введите значение поиска\n')

list_of_keys = [key for key in d if d[key] == item_of_search]
print(''.join(list_of_keys))
if list_of_keys == []:
    print('! value error !')

    #######################################

# 1004 ER_CANT_CREATE_FILE
# 1005 ER_CANT_CREATE_TABLE
# 1006 ER_CANT_CREATE_DB
# 1007 ER_DB_CREATE_EXISTS
# 1008 ER_DB_DROP_EXISTS                     
# 1010 ER_DB_DROP_RMDIR
# 1016 ER_CANT_OPEN_FILE
# 1022 ER_DUP_KEY

# Введите значение поиска
# ER_CANT_CREATE_DB
# 1006
    
    #######################################

# 4107 ER_SRS_UNUSED_PROJ_PARAMETER_PRESENT
# 4108 ER_GIPK_COLUMN_EXISTS
# 4111 ER_DROP_PK_COLUMN_TO_DROP_GIPK
# 4113 ER_DA_EXPIRE_LOGS_DAYS_IGNORED
# 4114 ER_CTE_RECURSIVE_NOT_UNION

# Введите значение поиска
# ER_CANT_OPEN_FILE

# ! value error !


# комментарий преподавателя:
# всё верно!