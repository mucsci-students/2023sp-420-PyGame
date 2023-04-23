""" 
done - ShuffleKey
done - get_word_points
done - RankIndex
 """


import os, sys, pytest
if os.name!="nt": 
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC")
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Controller")
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Model")
    sys.path.append(os.getcwd()+"/PyGame_Project/MVC/Model/Database")
else:
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC")
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Controller")
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Model")
    sys.path.append(os.getcwd()+"\\PyGame_Project\\MVC\\Model\\Database")



from PyGame_Project.MVC.Model.model_puzzle import *
from PyGame_Project.MVC.Controller.controller_universal import *

## default puzzle generation for testing 
pytest.fixture
def generateString():
    return f"""
According to all known laws
of aviation,
there is no way a bee
should be able to fly.
Its wings are too small to get
its fat little body off the ground. 
The bee, of course, flies anyway
because bees don't care
what humans think is impossible.
"""

## ---------- Testing shuffle ---------- ##
def test_encrypt_decrpyt(): 
    gene = generateString()

    bee = encrypt(gene) 
    bee = decrypt(bee)
    assert bee == gene
def test_encrypt():
    gene = generateString()
    bee = encrypt(gene)
    assert bee != gene