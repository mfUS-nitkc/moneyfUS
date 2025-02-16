import type { BaseResponse } from "./base";

export type UsageCategory = {
  usage_category_id: string;
  usage_category_name: string;
};

export type UsageCategoryResponse = BaseResponse & {
  items: Array<UsageCategory>;
};

export type DateString = string;

export type AssetPostResponse = BaseResponse & {
  created_asset_id: string;
}

export type AssetPostRequestBase = {
  amount: number;
  issued_at: DateString;
};

export type AssetPostRequestById = {
  usage_category_id: string;
} & AssetPostRequestBase;

export type AssetPostRequestByName = {
  usage_category_name: string;
} & AssetPostRequestBase;

export type AssetPostRequest =
  | AssetPostRequestById
  | AssetPostRequestByName;
