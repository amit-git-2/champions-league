import json
import enum


class Stages(enum.Enum):
    R16 = 1
    QF = 2
    SF = 3
    Final = 4


def find_current_stage(t):
    is_rs1_finished = t['Final']['SF1']['QF1']['RS1']['score']['L1']['finished'] and t['Final']['SF1']['QF1']['RS1']['score']['L2']['finished'] 
    is_rs2_finished = t['Final']['SF1']['QF1']['RS2']['score']['L1']['finished'] and t['Final']['SF1']['QF1']['RS2']['score']['L2']['finished']
    is_rs3_finished = t['Final']['SF1']['QF2']['RS3']['score']['L1']['finished'] and t['Final']['SF1']['QF2']['RS3']['score']['L2']['finished']
    is_rs4_finished = t['Final']['SF1']['QF2']['RS4']['score']['L1']['finished'] and t['Final']['SF1']['QF2']['RS4']['score']['L2']['finished']
    is_rs5_finished = t['Final']['SF2']['QF3']['RS5']['score']['L1']['finished'] and t['Final']['SF2']['QF3']['RS5']['score']['L2']['finished']
    is_rs6_finished = t['Final']['SF2']['QF3']['RS6']['score']['L1']['finished'] and t['Final']['SF2']['QF3']['RS6']['score']['L2']['finished']
    is_rs7_finished = t['Final']['SF2']['QF4']['RS7']['score']['L1']['finished'] and t['Final']['SF2']['QF4']['RS7']['score']['L2']['finished']
    is_rs8_finished = t['Final']['SF2']['QF4']['RS8']['score']['L1']['finished'] and t['Final']['SF2']['QF4']['RS8']['score']['L2']['finished']

    if is_rs1_finished and is_rs2_finished and is_rs3_finished and is_rs4_finished and is_rs5_finished and is_rs6_finished and is_rs7_finished and is_rs8_finished:
        ## Check Quarters
        is_qf1_finished = t['Final']['SF1']['QF1']['score']['L1']['finished'] and t['Final']['SF1']['QF1']['score']['L2']['finished']
        is_qf2_finished = t['Final']['SF1']['QF2']['score']['L1']['finished'] and t['Final']['SF1']['QF2']['score']['L2']['finished']
        is_qf3_finished = t['Final']['SF2']['QF3']['score']['L1']['finished'] and t['Final']['SF2']['QF3']['score']['L2']['finished']
        is_qf4_finished = t['Final']['SF2']['QF4']['score']['L1']['finished'] and t['Final']['SF2']['QF4']['score']['L2']['finished']
        if is_qf1_finished and is_qf2_finished and is_qf3_finished and is_qf4_finished:
            # Check Semi Finals
            is_sf1_finished = t['Final']['SF1']['score']['L1']['finished'] and t['Final']['SF1']['score']['L2']['finished']
            is_sf2_finished = t['Final']['SF2']['score']['L1']['finished'] and t['Final']['SF2']['score']['L2']['finished']
            if is_sf1_finished and is_sf2_finished:
                return Stages.Final
            else:
                return Stages.SF
        else:
            return Stages.QF
    else:
        return Stages.R16 


def print_score(score):
    print(f"\n{score['teams'][0]} v {score['teams'][1]}")
    if score['L1']['finished']:
        print(f"Leg 1 : {score['L1']['result']['goals']}")
    if score['L2']['finished']:
        if score['L2']['result']['penalties'] != "":
            print(f"Leg 2 : {score['L2']['result']['goals']} ({score['L2']['result']['penalties']})")
        else:
            print(f"Leg 2 : {score['L2']['result']['goals']}")

    if score['L1']['finished'] and score['L2']['finished']:
        print(f"Winner :: {score['winner']}")


def print_stage(t, stage):
    if stage == Stages.R16:
        print_score(t['Final']['SF1']['QF1']['RS1']['score'])
        print_score(t['Final']['SF1']['QF1']['RS2']['score'])
        print_score(t['Final']['SF1']['QF2']['RS3']['score'])
        print_score(t['Final']['SF1']['QF2']['RS4']['score'])
        print_score(t['Final']['SF2']['QF3']['RS5']['score'])
        print_score(t['Final']['SF2']['QF3']['RS6']['score'])
        print_score(t['Final']['SF2']['QF4']['RS7']['score'])
        print_score(t['Final']['SF2']['QF4']['RS8']['score'])
    elif stage == Stages.QF:
        print_score(t['Final']['SF1']['QF1']['score'])
        print_score(t['Final']['SF1']['QF2']['score'])
        print_score(t['Final']['SF2']['QF3']['score'])
        print_score(t['Final']['SF2']['QF4']['score'])
    elif stage == Stages.SF:
        print_score(t['Final']['SF1']['score'])
        print_score(t['Final']['SF2']['score'])
    else:
        print_score(t['Final']['score'])



def view_current_stage():
    # Read tt.json to load current state
    f = open('tt.json')
    tournament = json.load(f)

    # Find target stage that does not have results recorded yet
    current_stage = find_current_stage(tournament)
    print(f"Current stage is {current_stage}")

    # Print all the games in the target stage
    print_stage(tournament, current_stage)
    pass
