# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

from typing import no_type_check_decorator


scorer_1 = 'Ruud Gullit'
scorer_2 = 'Marco van Basten'

goal_0 = 32
goal_1 = 54

scorers = f"{scorer_1} {goal_0}, {scorer_2} {goal_1}"

report = f"{scorer_1} scored in the {goal_0}nd minute"'\n'f"{scorer_2} scored in the {goal_1}th minute"

player = "Hans van Breukelen"
first_name = (player[0:4])
last_name_len = len(player[5:])
name_short = player[0] + ". " + str(player[5:])
chant = len(first_name) * (first_name + "" + "!")
good_chant = chant[-1] != ""


print(chant)
print(good_chant)
