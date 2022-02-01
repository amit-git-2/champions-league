# Import turtle package
import json

def print_final_game(g):
    teams = g['score']['teams']
    t1_l1_goals = 0
    t2_l1_goals = 0
    if g['score']['L1']['finished']:
        t1_l1_goals, t2_l1_goals = g['score']['L1']['result']['goals'].split('-')

    if not g['score']['L1']['finished']:
        return f"{teams[0]} v {teams[1]}"
    else:
        return f"{teams[0]} v {teams[1]} ({t1_l1_goals}-{t2_l1_goals})"

def print_game(g):
    teams = g['score']['teams']

    t1_l1_goals = 0
    t1_l2_goals = 0
    t2_l1_goals = 0
    t2_l2_goals = 0

    if g['score']['L1']['finished']:
        t1_l1_goals, t2_l1_goals = g['score']['L1']['result']['goals'].split('-')
    if g['score']['L2']['finished']:
        t1_l2_goals, t2_l2_goals = g['score']['L2']['result']['goals'].split('-')

    t1_agg = int(t1_l1_goals) + int(t1_l2_goals)
    t2_agg = int(t2_l1_goals) + int(t2_l2_goals)

    if not g['score']['L1']['finished'] and not g['score']['L2']['finished']:
        return f"{teams[0]} v {teams[1]}"
    else:
        return f"{teams[0]} v {teams[1]} ({t1_agg}-{t2_agg})"

def draw_tournament_bracket():
    f = open('tt.json')
    t = json.load(f)

    print(f"------------------------------------------------------------------------------------")
    print(f"    Round of 16            Quarterfinals          Semifinals             Final      ")
    print(f"------------------------------------------------------------------------------------")
    print(f"    {print_game(t['Final']['SF1']['QF1']['RS1'])}")
    print(f"                           {print_game(t['Final']['SF1']['QF1'])}")
    print(f"    {print_game(t['Final']['SF1']['QF1']['RS2'])}")
    print(f"                                                  {print_game(t['Final']['SF1'])}")
    print(f"    {print_game(t['Final']['SF1']['QF2']['RS3'])}")
    print(f"                           {print_game(t['Final']['SF1']['QF2'])}")
    print(f"    {print_game(t['Final']['SF1']['QF2']['RS4'])}")
    print(f"                                                                         {print_final_game(t['Final'])}")
    print(f"    {print_game(t['Final']['SF2']['QF3']['RS5'])}")
    print(f"                           {print_game(t['Final']['SF2']['QF3'])}")
    print(f"    {print_game(t['Final']['SF2']['QF3']['RS6'])}")
    print(f"                                                  {print_game(t['Final']['SF2'])}")
    print(f"    {print_game(t['Final']['SF2']['QF4']['RS7'])}")
    print(f"                           {print_game(t['Final']['SF2']['QF4'])}")
    print(f"    {print_game(t['Final']['SF2']['QF4']['RS8'])}")
    print(f"------------------------------------------------------------------------------------")


if __name__ == '__main__':
    draw_tournament_bracket()
