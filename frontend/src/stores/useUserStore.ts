import { defineStore } from "pinia";
import type { User, UserLoginRequest, UserRegisterRequest } from "../types";

const initUser: User = {
  user_id: null,
  username: "",
  email: ""
}

export const useUserStore = defineStore('user', () => {
  const user = ref<User>(initUser);
  const isAuthenticated = computed(() => !!user.value.user_id)

  const config = useRuntimeConfig();
  const apiBaseUrl = config.public.apiBaseUrl;

  async function fetchUser() {
    try {
      const response = await fetch(`${apiBaseUrl}/user/self`);
      if (!response.ok) throw new Error('Failed to fetch user');
      const data: User = await response.json();
      setUser(data);
    } catch (error) {
      console.error(error);
      clearUser();
    }
  }

  async function login({email, password}: UserLoginRequest) {
    try {
      const response = await fetch(`${apiBaseUrl}/user/login`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password })
      });
      if (!response.ok) throw new Error('Login failed');
      const data: User = await response.json();
      setUser(data);
    } catch (error) {
      console.error(error);
      clearUser();
    }
  }

  async function logout() {
    try {
      const response = await fetch(`${apiBaseUrl}/user/logout`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
      });
      if (!response.ok) throw new Error('Login failed');
      const data: User = await response.json();
      setUser(data);
    } catch (error) {
      console.error(error);
      clearUser();
    }
  }

  async function register({email, password, username}: UserRegisterRequest) {
    try {
      const response = await fetch(`${apiBaseUrl}/user`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password, username })
      });
      if (!response.ok) throw new Error('Login failed');
      return true
    } catch (error) {
      console.error(error);
      return false
    }
  }

  function setUser(newUser: User) {
    user.value = newUser;
  }

  function clearUser() {
    user.value = initUser;
  }

  return {
    user,
    isAuthenticated,
    fetchUser,
    login,
    logout,
    register
  }
})
