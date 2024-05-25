import main 
 
def test_read_main_1(): 
    phrase = 'I love machine learning!'
    assert main.translate_phrase(phrase) == 'Я люблю машинное обучение!'
    
def test_read_main_2(): 
    phrase = 'Я люблю машинное обучение!'
    assert main.translate_phrase(phrase) == 'I love machine learning!'
    
def test_read_main_3(): 
    phrase = None
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
    
def test_read_main_4(): 
    phrase = ''
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
    
def test_read_main_5(): 
    phrase = '2142112312423'
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
    
def test_read_main_6(): 
    phrase = '../,.,/.,/.,'
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
    
def test_read_main_7(): 
    phrase = '423434??///?...!!'
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
    
def test_read_main_8(): 
    phrase = '           '
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
    
def test_read_main_9(): 
    phrase = '!!???!??!?!'
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
    
def test_read_main_10(): 
    phrase = '423434      ??///?...!!'
    assert main.translate_phrase(phrase) == 'Error: Некорректная фраза для перевода'
  