import type { User } from "@/types";
import type { GetLoanResponse, PostBorrowedRequest, PostBorrowedResponse, PostLendRequest, PostLendResponse, NewLoanBase, Loan, PostSplitRequest, PostSplitResponse } from "@/types/loan";
import { defineStore } from 'pinia';

export const useLoanStore = defineStore('loan', () => {
  const lendToUser = ref<User | undefined>()
  const borrowedByUser = ref<User | undefined>()

  const splitSelectedUserList = ref(new Map<string, { id: string; title: string }>())

  const lendLoanList = ref<Loan[]>([])
  const borrowedLoanList = ref<Loan[]>([])

  const config = useRuntimeConfig();
  const apiBaseUrl = config.public.apiBaseUrl;

  async function postCheckout(request: Loan) {
    try {
      const {error} = await useFetch(`${apiBaseUrl}/loan/checkout/${request.loan_id}`, {
        method: "POST",
        credentials: 'include'
      })
      if (error.value) throw new Error('Failed to post checkout Request')
      return true
    } catch (error) {
      console.error(error)
      return false;
    }
  }

  async function postLend(request: PostLendRequest) {
    try {
      const {data, error} = await useFetch<PostLendResponse>(`${apiBaseUrl}/loan/lend`, {
        method: "POST",
        body: JSON.stringify(request),
        credentials: 'include'
      })
      if (error.value) throw new Error('Failed to post Lend Request')
      return true
    } catch (error) {
      console.error(error)
      return false;
    }
  }

  async function postBorrowed(request: PostBorrowedRequest) {
    try {
      const {data, error} = await useFetch<PostBorrowedResponse>(`${apiBaseUrl}/loan/borrowed`, {
        method: "POST",
        body: JSON.stringify(request),
        credentials: 'include'
      })
      if (error.value) throw new Error('Failed to post Borrowed Request')
      return true
    } catch (error) {
      console.error(error)
      return false;
    }
  }

  async function postLoanNotify(request: Loan) {
    try {
      const {error} = await useFetch(`${apiBaseUrl}/loan/remind/${request.loan_id}`, {
        method: "POST",
        credentials: 'include'
      })
      if (error.value) throw new Error('Failed to post Notify Request')
      return true
    } catch (error) {
      console.error(error)
      return false;
    }
  }

  async function getLendList() {
    try {
      const {data, error} = await useFetch<GetLoanResponse>(`${apiBaseUrl}/loan/lend`, {
        credentials: 'include'
      })
      if (error.value) throw new Error('Failed to fetch LendList')
      setLendList(data.value?.items!)
      return true
    } catch (error) {
      console.error(error)
      return false
    }
  }

  async function getBorrowedList() {
    try {
      const {data, error} = await useFetch<GetLoanResponse>(`${apiBaseUrl}/loan/borrowed`, {
        credentials: 'include'
      })
      if (error.value) throw new Error('Failed to fetch BorrowedList')
      setBorrowedList(data.value?.items!)
      return true
    } catch (error) {
      console.error(error)
      return false
    }
  }

  async function postSplit(request: PostSplitRequest) {
    try {
      const {data, error} = await useFetch<PostSplitResponse>(`${apiBaseUrl}/split`, {
        method: "POST",
        body: JSON.stringify(request),
        credentials: 'include'
      })
      if (error.value) throw new Error('Failed to post Split Request')
      return true
    } catch (error) {
      console.error(error)
      return false;
    }
  }

  function setLendList(lends: Loan[]) {
    lendLoanList.value = lends
  }

  function setBorrowedList(borroweds: Loan[]) {
    borrowedLoanList.value = borroweds
  }

  function setLendToUser(user: User) {
    lendToUser.value = user
  }

  function setBorrowedByUser(user: User) {
    borrowedByUser.value = user
  }

  return {
    lendLoanList,
    borrowedLoanList,
    setBorrowedByUser,
    setLendToUser,
    getBorrowedList,
    getLendList,
    postBorrowed,
    postLend,
    postLoanNotify,
    postCheckout,
    postSplit,
    splitSelectedUserList,
    lendToUser,
    borrowedByUser
  }
})
