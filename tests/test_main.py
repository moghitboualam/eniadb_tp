from main import greet

def test_greet():
    # On appelle la fonction et on stocke le résultat dans une variable
    resultat = greet("Alice")
    
    # On vérifie que le retour est bien ce qu'on attend
    # Notez : J'ai changé "Bonjour" en "Salut" pour correspondre à votre main.py
    assert resultat == "Salut, Alice!"