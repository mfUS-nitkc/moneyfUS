import { defineStore } from "pinia";
import type { PostAssetRequest, PostAssetResponse, UsageCategory, UsageCategoryResponse } from "../types";

export const useAssetStore = defineStore('asset', () => {
  const usageCategories = ref<Array<UsageCategory>>([])

  const config = useRuntimeConfig();
  const apiBaseUrl = config.public.apiBaseUrl;

  async function fetchUsageCategory() {
    try {
      const { data, error } = await useFetch<UsageCategoryResponse>(`${apiBaseUrl}/asset/category`, {
        credentials: 'include'
      });
    
      if (error.value) {
        throw new Error('Failed to fetch categories');
      }
    
      setUsageCategories(data.value!.items!);
    } catch (error) {
      console.error(error);
      clearUsageCategories();
    }
  }

  async function postAsset(request: PostAssetRequest) {
    try {
      const {error} = await useFetch<PostAssetResponse>(`${apiBaseUrl}/asset`, {
        method: "POST",
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify(request),
        credentials: 'include'
      });
      if (error.value) throw new Error('Failed to post asset');
      return true
    }
    catch (error) {
      console.error(error);
      return false
    }
  }

  function setUsageCategories(newUsageCategories: Array<UsageCategory>) {
    usageCategories.value = newUsageCategories
  }

  function clearUsageCategories() {
    usageCategories.value = []
  }

  return {
    usageCategories,
    fetchUsageCategory,
    postAsset,
  }
})
