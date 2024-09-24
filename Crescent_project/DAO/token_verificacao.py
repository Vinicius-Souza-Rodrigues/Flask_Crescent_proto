from flask import session

def verificar_session(token, id):
    if not token or not id:
        return False
    
#talvez nao necessario
def verificar_integridade_token(token):
    if token != session['token']:
        return False
    
#def verificar_tempo():