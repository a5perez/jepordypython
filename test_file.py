
from jepordypython import user_interaction, game_responce, randomize_list, check_answer


def user_interaction():
    assert callable(user_interaction)
    assert key == category + difficulty

def game_responce():
    assert callable(game_responce)
    assert(len(answer) == 2)
    
def randomize_list():
    assert callable(randomized_list)
    
def check_answer():
    assert callable(check_answer)
    assert type(answer_rad) == str
