import type { BaseResponse, DateString } from "./base";
import type { UsageCategory } from "./usage";

export type AssetLog = {
  asset_id: string;
  amount: number
  issued_at: DateString
  user: string
  usage_category: UsageCategory
}

export type AssetLogResponse = BaseResponse & {
  assets: AssetLog[]
}
