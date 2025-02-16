import { defineStore } from "pinia";
import type { GetFriendListResponse, User, UserLoginRequest, UserRegisterRequest } from "../types";

const initUser: User = {
  user_id: null,
  username: "",
  email: ""
}

export const useUserStore = defineStore('user', () => {
  const user = ref<User>(initUser);
  const isAuthenticated = computed(() => !!user.value.user_id)
  const friendList = ref<User[]>([])

  const config = useRuntimeConfig();
  const apiBaseUrl = config.public.apiBaseUrl;

  async function fetchUser() {
    try {
      const { data, error } = await useFetch<User>(`${apiBaseUrl}/user/self`, {
        credentials: 'include'
      });
    
      if (error.value) {
        throw new Error('Failed to fetch user');
      }
    
      setUser(data.value!);
    } catch (error) {
      console.error(error);
      clearUser();
    }
  }

  async function fetchFriendList() {
    try {
      const { data, error } = await useFetch<GetFriendListResponse>(`${apiBaseUrl}/friend`, {
        credentials: 'include'
      });
    
      if (error.value) {
        throw new Error('Failed to fetch user');
      }
    
      setFriendList(data.value?.friends!);
    } catch (error) {
      console.error(error);
      clearUser();
    }
  }

  async function login(request: UserLoginRequest) {
    try {
      const { data, error } = await useFetch<User>(`${apiBaseUrl}/user/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(request),
        credentials: 'include'
      });
    
      if (error.value) {
        throw new Error('Login failed');
      }
    
      setUser(data.value!);
    } catch (error) {
      console.error(error);
      clearUser();
    }
  }

  async function logout() {
    try {
      const { error } = await useFetch(`${apiBaseUrl}/user/logout`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'include'
      });

      if (error.value) throw new Error('Logout failed');
      clearUser()
    } catch (error) {
      console.error(error);
    }
  }

  async function register(request: UserRegisterRequest) {
    try {
      const { error } = await useFetch(`${apiBaseUrl}/user`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(request),
        credentials: 'include'
      });
    
      if (error.value) {
        throw new Error('Login failed');
      }
    
      return true;
    } catch (error) {
      console.error(error);
      return false;
    }
    
  }

  function setFriendList(newFriendList: Array<User>) {
    friendList.value = newFriendList;
  }

  function setUser(newUser: User) {
    user.value = newUser;
  }

  function clearUser() {
    user.value = initUser;
  }

  return {
    user,
    friendList,
    isAuthenticated,
    fetchUser,
    fetchFriendList,
    login,
    logout,
    register
  }
})
