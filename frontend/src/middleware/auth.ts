export default defineNuxtRouteMiddleware((to, from) => {
  const userStore = useUserStore()
  if (!userStore.isAuthenticated) {
    return navigateTo('/login')
  }
})