#№1
s = 'шоипощукп!!!нгунмгкне'
curch = 0
b = 0
for i in range(len(s)):
    if s[i] == 'н':
        curch += 1
    else:
        b = max(b, curch)
        sum = 0
b = max(b, curch)
print(b)
s = s.replace('!', '.')
print(s)

# 2
# s = "slidufasdjdf;(a;sdiofjlksdjf;lksjdfaoidfsaklf)alsdkjfisdufeejlsd;jfa;fa"
# flag = False
# for i in s:
#     if i == ")": flag = False
#     if flag: print(i, end="")
#     if i == "(": flag = True


# 3
# s = "фжыдшялчжфоцущшляждлаофлоащшуаавфыафжяяяфшуаолаоядафаожфдллыяаождлдав"
# for i in range(len(s)):
#     if s[i] == "а":
#         for j in range(i, len(s)):
#             if s[j] != "я": print(s[j], end="")
#             else: 
#                 print("\n")
#                 break               