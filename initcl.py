import json
import pprint
import random


def new_tournament():
    print("Initializing Tournament")
    f = open('teams.json')
    teams_loaded = json.load(f)
    teams = teams_loaded['teams']
    pprint.pprint(teams)
    print(f"Total teams loaded {len(teams)}")
    random.shuffle(teams)
    pprint.pprint(teams)

    tt = build_empty_data()
    # teams[0], teams[1] should be assigned to rs1
    tt['Final']['SF1']['QF1']['RS1']['score']['teams'] = [teams[0], teams[1]]
    # teams[2], teams[3] should be assigned to rs2
    tt['Final']['SF1']['QF1']['RS2']['score']['teams'] = [teams[2], teams[3]]
    # teams[4], teams[5] should be assigned to rs3
    tt['Final']['SF1']['QF2']['RS3']['score']['teams'] = [teams[4], teams[5]]
    # teams[6], teams[7] should be assigned to rs4
    tt['Final']['SF1']['QF2']['RS4']['score']['teams'] = [teams[6], teams[7]]

    # Remaining teams
    tt['Final']['SF2']['QF3']['RS5']['score']['teams'] = [teams[8], teams[9]]
    tt['Final']['SF2']['QF3']['RS6']['score']['teams'] = [teams[10], teams[11]]
    tt['Final']['SF2']['QF4']['RS7']['score']['teams'] = [teams[12], teams[13]]
    tt['Final']['SF2']['QF4']['RS8']['score']['teams'] = [teams[14], teams[15]]

    pprint.pprint(tt)

    # save tournament structure
    wf = open('tt.json', 'w')
    json.dump(tt, wf, indent=4)

    print("New tournament saved to tt.json")



def build_leg():
    leg = {}
    leg['finished'] = False
    leg['result'] = {
        'goals':  "",
        'penalties': ""
    }
    return leg


def build_score(is_final=False):
    score = {}
    score['winner'] = 'TBD'
    score['teams'] = []

    if is_final:
        score['L1'] = build_leg()
    else:
        score['L1'] = build_leg()
        score['L2'] = build_leg()
    return score


def build_empty_data():
    # Round of 16
    rs1 = {
      'score' : build_score()
    }
    rs2 = {
      'score' : build_score()
    }
    rs3 = {
      'score' : build_score()
    }
    rs4 = {
      'score' : build_score()
    }
    rs5 = {
      'score' : build_score()
    }
    rs6 = {
      'score' : build_score()
    }
    rs7 = {
      'score' : build_score()
    }
    rs8 = {
      'score' : build_score()
    }

    # Quarter finals
    qf1 = {
        'score': build_score(),
        'RS1': rs1,
        'RS2': rs2
    }
    qf2 = {
        'score': build_score(),
        'RS3': rs3,
        'RS4': rs4
    }
    qf3 = {
        'score': build_score(),
        'RS5': rs5,
        'RS6': rs6
    }
    qf4 = {
        'score': build_score(),
        'RS7': rs7,
        'RS8': rs8
    }

    # Semi finals
    sf1 = {
        'score': build_score(),
        'QF1': qf1,
        'QF2': qf2
    }
    sf2 = {
        'score': build_score(),
        'QF3': qf3,
        'QF4': qf4
    }

    # Final
    final = {
        'score': build_score(True),
        'SF1': sf1,
        'SF2': sf2
    }

    return {
        'Final': final
    }


if __name__ == "__main__":
    new_tournament()
