import { defineStore } from "pinia";
import type { AssetLog, AssetLogResponse, PostAssetRequest, PostAssetResponse, UsageCategory, UsageCategoryResponse } from "../types";

export const useAssetStore = defineStore('asset', () => {
  const usageCategories = ref<Array<UsageCategory>>([])
  const assetLogs = ref<Array<AssetLog>>([])

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

  async function fetchAssetLogs() {
    try {
      const { data, error } = await useFetch<AssetLogResponse>(`${apiBaseUrl}/asset`, {
        credentials: 'include'
      });
    
      if (error.value) {
        throw new Error('Failed to fetch categories');
      }
    
      setAssetLogs(data.value?.assets!);
    } catch (error) {
      console.error(error);
      clearAssetLogs();
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

  function setAssetLogs(newAssets: Array<AssetLog>) {
    assetLogs.value = newAssets
  }

  function clearAssetLogs() {
    assetLogs.value = []
  }

  return {
    assetLogs,
    usageCategories,
    fetchUsageCategory,
    fetchAssetLogs,
    postAsset,
  }
})
