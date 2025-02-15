export default defineNuxtRouteMiddleware((to, from) => {
  const userStore = useUserStore()
  if (!userStore.isAuthenticated) {
    useRouter().push("/login")
  }
})