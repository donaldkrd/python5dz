# Создайте программу для игры в ""Крестики-нолики"".

# print('*'*100)
# print('\n')

# board = list(range(1,10))

# def design_board(board):
#     print('-'*12)
#     for i in range(3):
#         print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
#         print('-'*12)

# def choice(tic_tac):
#     valid = False
#     while not valid:
#         player_index = input('Выберите ячейку для хода ' + tic_tac + ' --> ')
#         try:
#             player_index =int(player_index)
#         except:
#             print('ошибка')
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if(str(board[player_index-1]) not in 'XO'):
#                 board[player_index-1] = tic_tac
#                 valid = True
#             else:
#                 print('Занято')
#         else:
#             print('Еще раз')

# def victory_check(board):
#     victory = ((0,1,2),(3,4,5),(6,7,8),
#                (0,3,6),(1,4,7),(2,5,8),
#                (0,4,8),(2,4,6))
#     for i in victory:
#         if board[i[0]] == board[i[1]] == board[i[2]]:
#             return board[i[0]]
#     return False

# def game(board):
#     counter =0
#     vic = False
#     while not vic:
#         design_board(board)
#         if counter % 2 == 0:
#             choice('X')
#         else:
#             choice('0')
#         counter +=1
#         if counter > 4:
#             tt_win = victory_check(board)
#             if tt_win:
#                 print(tt_win,'Победа')
#                 vic = True
#                 break
#             if counter == 9:
#                 print('Ничья')
#         design_board(board)
# game(board)


# Напишите программу, удаляющую из 
# текста все слова, содержащие ""абв"".

# text1 = 'абв про бва ааа ооо'
# text1_list = list(filter(lambda i: 'а' not in i and 'б' not in i and 'в' not in i, text1.split()))
# print(text1_list)


# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# def press(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             ind = 0
#         inp_str = text.readline()
#         count = 1
#         while ind < len(inp_str) - 1:
#             if inp_str[ind] == inp_str[ind + 1]:
#                 count += 1
#             else:
#                 if count == 1:
#                     res.write(inp_str[ind])
#                 else:
#                     res.write(str(count) + inp_str[ind])
#                 count = 1
#             ind += 1
# press('result.txt', 'result2.txt')

# def depress(file, result):
#     with open(file, 'r', encoding='utf-8') as text:
#         with open(result, 'w', encoding='utf-8') as res:
#             inp_str = text.readline()
#             count = ''
#             for letter in inp_str:
#                 if letter.isdigit():
#                     count += letter
#                 else:
#                     if not count:
#                         res.write(int(count) * letter)
#                     else:
#                         res.write(letter)
#                     count = ''

# depress('result.txt', 'result2.txt')



