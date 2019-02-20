# 1. Display welcome info
# 2. Display and capture user's choice
import cards_input
import cards_tools

# global variables
first_choice = ["0", "1", "2", "3"]


if __name__ == '__main__':
    while True:
        cards_tools.welcome_info()

        choice = input("请输入您想要进行的操作：")

        if choice not in first_choice:
            print("您输入的选项不正确！")

        elif choice == first_choice[0]:
            print("---退出系统成功！---")
            break

        elif choice == first_choice[1]:
            cards_input.new_card()

        elif choice == first_choice[2]:
            cards_input.show_all_cards()

        else:
            cards_input.query_and_other_oper()

    print("感谢您使用【名片管理系统】！")
