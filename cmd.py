# from bracket import draw_tournament_bracket
from initcl import new_tournament
from viewcurrent import view_current_stage
from recordresult import record_result

def show_menu():
    print("\n------------- Champions League Menu -------------")
    print("\t 1. Create new tournament")
    print("\t 2. View current level")
    print("\t 3. Record match result")
    print("\t 4. Draw brackets")
    print("\t 5. Quit")

def draw_brackets():
    print("Asking turtle to draw tournament brackets")
    # draw_tournament_bracket()

if __name__ == "__main__":
    continue_loop = True
    while continue_loop:
        show_menu()
        opt = input(">>> ")
        print(f"You selected {opt}")

        opt_num = int(opt)

        if opt_num == 1:
            new_tournament()
        elif opt_num == 2:
            view_current_stage()
        elif opt_num == 3:
            record_result()
        elif opt_num == 4:
            draw_brackets()
        else:
            print("Goodbye")
            continue_loop = False
