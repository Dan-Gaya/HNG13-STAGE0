from pydantic import BaseModel, EmailStr

class UserProfile(BaseModel):
    email: EmailStr
    name: str
    stack: str

class ProfileResponse(BaseModel):
    status: str
    user: UserProfile
    timestamp: str
    fact: str
