# 要想知道某一个数能否被另一个数整除，首先看它们相除所得到的商是否为整数。
# 如何判断商是否为整数呢？我使用了"int"转换数字的方法，这样得到的数都是经过四舍五入后得到整数的。只要判断原数是否于这个数被四舍五入取整后的数有别就行了。

big_number = int(input("请输入一个数，我会判断其是否能被你想要的数字整除，你现在输入的数为被除数"))
# big_number 就是被除数啊
small_number = int(input("请输入除数"))
# small_number 就是除数啊
first_answer = big_number / small_number
# first_answer 就是商啊
first_before_answer = first_answer - int(first_answer)
# first_before_number 就是判断这个数是否为整数啊

if first_answer < 1:
    stop_first = input("你输入的除数似乎比被除数大呢，不过没有关系，是否需要调换被除数与除数位置，再得到一次结果？按任意键继续，按q退出程序")
    # 众所周知啊，一个小一点的数除以大一点的数会得到一个真分数，真分数一定是小于一的！所以就可以判断输入的除数比被除数大了
    if stop_first != "q":
        print("程序继续")
        changed_first_number = small_number / big_number
        # changed_first_number 就是把这俩数反过来相除得到的数
        if changed_first_number == int(changed_first_number):
            print("你输入的数可以被除数整除！所得的答案为" + str(int(changed_first_number)))
        else:
            print("不好意思，你输入的两个数无论咋除都没法被整除，所得的结果为" + str(changed_first_number))
    else:
        print("程序结束")

elif first_before_answer > 0:
    print("这个数没法被除数整除！结果为" + str(first_answer))
    # 商不是整数，你觉得这除数能被被除数整除么
elif first_answer == int(first_answer):
    print("你输入的数字可以被你所输入的除数整除，所得的答案为" + str(int(first_answer)))
