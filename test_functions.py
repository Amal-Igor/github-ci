from main import count_char, check_if_maj, check_if_special, check_if_valid_password

def test_count_char():
    input = ["Bonjour", "Salut", "ok", "nerd"]
    lst_test = []
    for word in input:
        lst_test.append(count_char(word))
    lst_exp = [7, 5, 2 , 4]
    assert lst_exp == lst_test
    
def test_check_if_maj():
    input = ["Bonjour", "Salut", "ok", "nerd"]
    lst_test = []
    for word in input:
        lst_test.append(check_if_maj(word))
    lst_exp = [True, True, False, False]
    assert lst_exp == lst_test

def test_check_if_special():
    input = ["Bonjour", "Salut*", "ok", "nerd"]
    lst_test = []
    for word in input:
        lst_test.append(check_if_special(word))
    lst_exp = [False, True, False, False]
    assert lst_exp == lst_test


def test_check_if_valid_password():
    input = ["Bonjourrrr*", "Salut*", "*okcooolzeroua", "AlorslaCestParfait*"]
    lst_test = []
    for word in input:
        lst_test.append(check_if_valid_password(word))
    lst_exp = [True, False, False, True]
    assert lst_exp == lst_test
