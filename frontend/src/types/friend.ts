import type { BaseResponse } from "./base";
import type { User } from "./user";

export type GetFriendListResponse = BaseResponse & {
  friends: Array<User>
}