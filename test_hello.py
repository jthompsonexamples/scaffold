from hello import add # get the function from that file

def test_add(): # make a function with an expected output
    assert add(1,2) == 3