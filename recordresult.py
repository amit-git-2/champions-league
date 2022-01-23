import re
import json

from viewstage import Stages

def find_game(t, team_1, team_2):
    # Check round of 16 teams
    if team_1 in t['Final']['SF1']['QF1']['RS1']['score']['teams'] and team_2 in t['Final']['SF1']['QF1']['RS1']['score']['teams']:
        return t['Final']['SF1']['QF1']['RS1']['score'], Stages.R16

    if team_1 in t['Final']['SF1']['QF1']['RS2']['score']['teams'] and team_2 in t['Final']['SF1']['QF1']['RS2']['score']['teams']:
        return t['Final']['SF1']['QF1']['RS2']['score'], Stages.R16

    if team_1 in t['Final']['SF1']['QF2']['RS3']['score']['teams'] and team_2 in t['Final']['SF1']['QF2']['RS3']['score']['teams']:
        return t['Final']['SF1']['QF2']['RS3']['score'], Stages.R16

    if team_1 in t['Final']['SF1']['QF2']['RS4']['score']['teams'] and team_2 in t['Final']['SF1']['QF2']['RS4']['score']['teams']:
        return t['Final']['SF1']['QF2']['RS4']['score'], Stages.R16

    if team_1 in t['Final']['SF2']['QF3']['RS5']['score']['teams'] and team_2 in t['Final']['SF2']['QF3']['RS5']['score']['teams']:
        return t['Final']['SF2']['QF3']['RS5']['score'], Stages.R16

    if team_1 in t['Final']['SF2']['QF3']['RS6']['score']['teams'] and team_2 in t['Final']['SF2']['QF3']['RS6']['score']['teams']:
        return t['Final']['SF1']['QF3']['RS6']['score'], Stages.R16

    if team_1 in t['Final']['SF2']['QF4']['RS7']['score']['teams'] and team_2 in t['Final']['SF2']['QF4']['RS7']['score']['teams']:
        return t['Final']['SF2']['QF4']['RS7']['score'], Stages.R16

    if team_1 in t['Final']['SF2']['QF4']['RS8']['score']['teams'] and team_2 in t['Final']['SF2']['QF4']['RS8']['score']['teams']:
        return t['Final']['SF2']['QF4']['RS8']['score'], Stages.R16

    # Check quarter final teams
    if team_1 in t['Final']['SF1']['QF1']['score']['teams'] and team_2 in t['Final']['SF1']['QF1']['score']['teams']:
        return t['Final']['SF1']['QF1']['score'], Stages.QF

    if team_1 in t['Final']['SF1']['QF2']['score']['teams'] and team_2 in t['Final']['SF1']['QF2']['score']['teams']:
        return t['Final']['SF1']['QF2']['score'], Stages.QF

    if team_1 in t['Final']['SF2']['QF3']['score']['teams'] and team_2 in t['Final']['SF2']['QF3']['score']['teams']:
        return t['Final']['SF2']['QF3']['score'], Stages.QF
    
    if team_1 in t['Final']['SF2']['QF4']['score']['teams'] and team_2 in t['Final']['SF2']['QF4']['score']['teams']:
        return t['Final']['SF2']['QF4']['score'], Stages.QF

    # Check semi finals teams
    if team_1 in t['Final']['SF1']['score']['teams'] and team_2 in t['Final']['SF1']['score']['teams']:
        return t['Final']['SF1']['score'], Stages.SF
    
    if team_1 in t['Final']['SF2']['score']['teams'] and team_2 in t['Final']['SF2']['score']['teams']:
        return t['Final']['SF2']['score'], Stages.SF
    
    # Check final teams
    if team_1 in t['Final']['score']['teams'] and team_2 in t['Final']['score']['teams']:
        return t['Final']['score'], Stages.Final
    
    return None, None


def save_game_result(team_1, team_2, team_1_score, team_2_score, team_1_penalties=0, team_2_penalties=0):
    f = open('tt.json')
    tournament = json.load(f)
    found_winner = False
    game, stage = find_game(tournament, team_1, team_2)
    if game is None:
        print(f"Invalid teams {team_1} v {team_2}")
    else:
        if not game['L1']['finished']:
            # record Leg 1 result
            game['L1']['result']['goals'] = f"{team_1_score}-{team_2_score}"
            if team_1_score == team_2_score and (team_1_penalties != 0 or team_2_penalties != 0):
                game['L1']['result']['penalties'] = f"{team_1_penalties}-{team_2_penalties}"
            game['L1']['finished'] = True
        else:
            # record Leg 2 result
            game['L2']['result']['goals'] = f"{team_1_score}-{team_2_score}"
            if team_1_score == team_2_score and (team_1_penalties != 0 or team_2_penalties != 0):
                game['L2']['result']['penalties'] = f"{team_1_penalties}-{team_2_penalties}"
            game['L2']['finished'] = True
        
        # Find winner
        if game['L1']['finished'] and game['L2']['finished']:
            found_winner = True
            # record the winner
            goals_l1_t1, goals_l1_t2 = game['L1']['result']['goals'].split('-')
            goals_l2_t1, goals_l2_t2 = game['L2']['result']['goals'].split('-')
            team_1_agg_goals = goals_l1_t1 + goals_l2_t1
            team_2_agg_goals = goals_l1_t2 + goals_l2_t2
            if team_1_agg_goals == team_2_agg_goals:
                # check away goals
                away_goals_t1 = goals_l2_t1
                away_goals_t2 = goals_l1_t2
                if away_goals_t1 == away_goals_t2:
                    # check L2 penalties
                    pen_t1, pen_t2 = game['L2']['result']['penalties'].split('-')
                    if pen_t1 > pen_t2:
                        game['winner'] = team_1
                    else:
                        game['winner'] = team_2
                else:
                    if away_goals_t1 > away_goals_t2:
                        game['winner'] = team_1
                    else:
                        game['winner'] = team_2
            else:
                if team_1_agg_goals > team_2_agg_goals:
                    game['winner'] = team_1
                else:
                    game['winner'] = team_2
        else:
            # check if final, then only check L1 and penalties, if applicable
            if stage == Stages.Final:
                found_winner = True
                goals_t1, goals_t2 = game['L1']['result']['goals'].split('-')
                if goals_t1 == goals_t2:
                    pen_t1, pen_t2 = game['L1']['result']['penalties'].split('-')
                    if pen_t1 > pen_t2:
                        game['winner'] = team_1
                    else:
                        game['winner'] = team_2
                else:
                    if goals_t1 > goals_t2:
                        game['winner'] = team_1
                    else:
                        game['winner'] = team_2
        if found_winner:
            print(f"Winner of the {stage} between {team_1} and {team_2} is {game['winner']}")
    
    promote_stage_teams(tournament)

    wf = open('tt.json', 'w')
    json.dump(tournament, wf, indent=4)
    print("Game result recorded.")

def promote_stage_teams(t):
    rs1_winner = t['Final']['SF1']['QF1']['RS1']['score']['winner']
    rs2_winner = t['Final']['SF1']['QF1']['RS2']['score']['winner']
    t['Final']['SF1']['QF1']['score']['teams'] = [rs1_winner, rs2_winner]

    rs3_winner = t['Final']['SF1']['QF2']['RS3']['score']['winner']
    rs4_winner = t['Final']['SF1']['QF2']['RS4']['score']['winner']
    t['Final']['SF1']['QF2']['score']['teams'] = [rs3_winner, rs4_winner]

    rs5_winner = t['Final']['SF2']['QF3']['RS5']['score']['winner']
    rs6_winner = t['Final']['SF2']['QF3']['RS6']['score']['winner']
    t['Final']['SF2']['QF3']['score']['teams'] = [rs5_winner, rs6_winner]

    rs7_winner = t['Final']['SF2']['QF4']['RS7']['score']['winner']
    rs8_winner = t['Final']['SF2']['QF4']['RS8']['score']['winner']
    t['Final']['SF2']['QF4']['score']['teams'] = [rs7_winner, rs8_winner]

    qf1_winner = t['Final']['SF1']['QF1']['score']['winner']
    qf2_winner = t['Final']['SF1']['QF2']['score']['winner']
    qf3_winner = t['Final']['SF2']['QF3']['score']['winner']
    qf4_winner = t['Final']['SF2']['QF4']['score']['winner']
    t['Final']['SF1']['score']['teams'] = [qf1_winner, qf2_winner]
    t['Final']['SF2']['score']['teams'] = [qf3_winner, qf4_winner]

    sf1_winner = t['Final']['SF1']['score']['winner']
    sf2_winner = t['Final']['SF2']['score']['winner']
    t['Final']['score']['teams'] = [sf1_winner, sf2_winner]




# Record result format "DOR v POR = 3-3 (3-5)"
def record_result():
    score = input("Enter the game score :: ")
    if re.search(r"\(\d-\d\)", score) is not None:
        team_1, ignored_1, team_2, ignored_2, score_main, penalties = score.split(' ')
        team_1_score, team_2_score = score_main.split('-')
        team_1_penalties, team_2_penalties = penalties.split('-')
        team_1_penalties = team_1_penalties.removeprefix('(')
        team_2_penalties = team_2_penalties.removesuffix(')')
        # print(f"Team 1 {team_1} score {team_1_score} and penalties {team_1_penalties}")
        # print(f"Team 2 {team_2} score {team_2_score} and penalties {team_2_penalties}")
        save_game_result(team_1, team_2, team_1_score, team_2_score, team_1_penalties, team_2_penalties)
    else:
        team_1, ignored_1, team_2, ignored_2, score_main = score.split(' ')
        team_1_score, team_2_score = score_main.split('-')
        # print(f"Team 1 {team_1} score {team_1_score}")
        # print(f"Team 2 {team_2} score {team_2_score}")
        save_game_result(team_1, team_2, team_1_score, team_2_score)





