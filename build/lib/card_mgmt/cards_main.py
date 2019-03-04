#!/usr/local/bin/python3

# 当在IDE中启动解释器时，当前的工作目录就是项目目录，能顺利调用同项目中的模块；
# 但是当通过命令行启动时，当前工作目录为启动解释器时所在的目录，
# 如果当时的位置不是项目目录，那么项目目录中的模块就不会被找到，
# 因此运行的时候报错:ModuleNotFoundError: No Module named ...
#
# 解决方法：就是把模块路径提供给解释器：
# 1. 把模块路径放到环境变量中作为全局变量（sys.path能扫描到）
# 若不加以下两行，当把card_mgmt作为一个包时，外界引入这个包，经常会出错：
# 因为这个包中的模块之间互相import，所以经常出现"ModuleNotFound Error"
# import sys
# sys.path.append("/Users/taixiaomei/IdeaProjects/card_mgmt")
# 如此操作，包中模块各处在互相import时，直接写"import 模块名"即可
# 但是，这只是在包所在目录下执行时OK，若换另外的目录，引入包则报错ModuleNotFoundError

# 2. 另外的解决办法是，包中的模块之间互相import时，使用from 包名 import 模块名 的方式


# 1. Display welcome info
# 2. Display and capture user's choice

from card_mgmt import cards_tools

__VERSION_TYPE = True  # True = OO, False = non-OO

if __VERSION_TYPE:
    from card_mgmt import cards_input_oo as cards_input
else:
    from card_mgmt import cards_input_non_oo as cards_input


# global variables define a tuple due to its unchangeable attribute
FIRST_CHOICE = ("0", "1", "2", "3")


def main():

    while True:
        cards_tools.welcome_info()

        choice = input("请输入您想要进行的操作：")

        try:

            if choice not in FIRST_CHOICE:
                print("您输入的选项不正确！")

            elif choice == FIRST_CHOICE[0]:
                print("---退出系统成功！---")
                break

            elif choice == FIRST_CHOICE[1]:
                cards_input.new_card()

            elif choice == FIRST_CHOICE[2]:
                cards_input.show_all_cards()

            else:
                cards_input.query_and_other_oper()

        except Exception as result:
            print("操作异常： ", result)

    print("感谢您使用【名片管理系统】！")


if __name__ == '__main__':

    main()
