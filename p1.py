num = int(input("Enter a number: "))
str_num = str(num)
for i in range(len(str_num) // 2):
        if str_num == str_num[::-1]:
            print(f"{num} is a palindrome.")
        else:
             print(f"{num} is not a palindrome.")


