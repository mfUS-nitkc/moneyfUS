export type BaseResponse = {
  success: true
}

export type ErrorResponse =  {
  success: false
  detail: string
}

export type UserId = string | null
export type Username = string
export type Email = string
export type Password = string

export type User = {
  user_id: UserId,
  username: Username,
  email: Email,
}

export type UserResponse =  BaseResponse & User 

export type UserLoginRequest = {
  email: Email,
  password: Password
}

export type UserRegisterRequest = {
  email: Email,
  password: Password,
  username: Username
}