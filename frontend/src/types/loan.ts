import type { BaseResponse, DateString } from "./base";
import type { User, UserId } from "./user";

export type LoanId = string

export type Loan = {
  amount: number,
  due_date: DateString,
  loan_id: LoanId,
  lender: User,
  borrower: User,
  is_paid: boolean
}

export type NewLoanBase = {
  amount: number,
  due_date: DateString,
}

export type PostLendRequest = NewLoanBase & {
  lend_to_user_id: UserId
}

export type PostBorrowedRequest = NewLoanBase & {
  borrowed_by_user_id: UserId
}

export type PostLendResponse = BaseResponse & Loan
export type PostBorrowedResponse = BaseResponse & Loan

export type GetLoanResponse = BaseResponse & {
  items: Array<Loan>
}

export type SplitParticipant = {
  participant_id: UserId,
  amount: number
}

export type PostSplitRequest = {
  total_amount: number,
  description: string,
  due_date: DateString,
  participants: SplitParticipant[]
}

export type PostSplitResponse = BaseResponse & {
  split_id: string
} & PostSplitRequest
