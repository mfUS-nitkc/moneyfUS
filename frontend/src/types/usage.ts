import type { BaseResponse, DateString } from "./base";

export type UsageCategory = {
  usage_category_id: string;
  usage_category_name: string;
};

export type UsageCategoryResponse = BaseResponse & {
  items: Array<UsageCategory>;
};

export type PostAssetResponse = BaseResponse & {
  created_asset_id: string;
}

export type PostAssetRequestBase = {
  amount: number;
  issued_at: DateString;
};

export type PostAssetRequestById = {
  usage_category_id: string;
} & PostAssetRequestBase;

export type PostAssetRequestByName = {
  usage_category_name: string;
} & PostAssetRequestBase;

export type PostAssetRequest =
  | PostAssetRequestById
  | PostAssetRequestByName;
