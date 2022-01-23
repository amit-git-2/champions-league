# from bracket import draw_tournament_bracket
from initcl import new_tournament
from viewstage import view_current_stage, view_all_stages
from recordresult import record_result
from bracket import draw_tournament_bracket

def show_menu():
    print("\n------------- Champions League Menu -------------")
    print("\t 1. Create new tournament")
    print("\t 2. View current stage")
    print("\t 3. Show tournament")
    print("\t 4. View tournament brackets")
    print("\t 5. Record match result")
    print("\t 6. Quit")


if __name__ == "__main__":
    continue_loop = True
    while continue_loop:
        show_menu()
        opt = input(">>> ")

        opt_num = int(opt)

        if opt_num == 1:
            new_tournament()
        elif opt_num == 2:
            view_current_stage()
        elif opt_num == 3:
            view_all_stages()
        elif opt_num == 4:
            draw_tournament_bracket()
        elif opt_num == 5:
            record_result()
        else:
            print("Goodbye")
            continue_loop = False
