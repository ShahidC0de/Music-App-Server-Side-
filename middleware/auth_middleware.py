from fastapi import HTTPException, Header
import jwt


def auth_middleware(x_auth_token = Header()):
    try:
        if not x_auth_token:
            raise HTTPException(401, 'Not auth token, Access denied')
        verified_token = jwt.decode(x_auth_token, 'pass_key', ['HS256'])
        if not verified_token:
            raise HTTPException(401, 'token verification failed, Access denied')
        uid =  verified_token.get('id')
        return {'uid': uid, 'token': x_auth_token}
    except jwt.PyJWTError:
        raise HTTPException(401, 'token is not valid')