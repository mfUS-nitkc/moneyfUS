export default defineNuxtRouteMiddleware(async (to, from) => {
  const userStore = useUserStore()
  if (!userStore.isAuthenticated) {
    await userStore.fetchUser()
    if (!userStore.isAuthenticated) {
      return navigateTo('/login')
    }
  }
})