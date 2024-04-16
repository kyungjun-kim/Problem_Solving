def solution(id_pw, db):
    if id_pw in db :
        return "login"
    else :
        if len(list(filter(lambda f: f[0] == id_pw[0], db))) > 0 :
            return "wrong pw"
        else :
            return "fail"
    return answer