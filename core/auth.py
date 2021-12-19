import jwt
from fastapi import HTTPException, Security
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta


class AuthHandler():
    security = HTTPBearer()
    pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
    secret = "SECRET"

    def get_passwords_hash(self, password):
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hash_password):
        return self.pwd_context.verify(plain_password, hash_password)

    def encode_token(self, user_id, age):
        payload = {
            "exp": datetime.utcnow() + timedelta(days=0, minutes=5),
            "iat": datetime.utcnow(),
            'sub': user_id,
            "age": age,
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm="HS256"
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return HTTPException(status_code=401, detail="Signature has expired")
        except jwt.InvalidTokenError:
            return HTTPException(status_code=401, detail="Token is invalid")

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
        return self.decode_token(auth.credentials)

#
# z = AuthHandler()
# a = z.get_passwords_hash("grecigor")
# if z.verify_password("grecigor",a):
#     print('yes')