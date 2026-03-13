#!/usr/bin/env python3
"""
MiniMax 使用量查询脚本
用法: python3 minimax_usage.py --api-key YOUR_API_KEY
"""

import argparse
import json
import requests
import sys


def get_account_info(api_key: str) -> dict:
    """获取账户信息"""
    url = "https://api.minimax.chat/v1/account_info"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    return response.json()


def get_usage_detail(api_key: str, start_date: str = None, end_date: str = None) -> dict:
    """获取使用详情"""
    url = "https://api.minimax.chat/v1/usage/detail"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    params = {}
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date
    
    response = requests.get(url, headers=headers, params=params)
    return response.json()


def format_currency(amount: float) -> str:
    """格式化货币"""
    return f"¥{amount:.2f}"


def main():
    parser = argparse.ArgumentParser(description="查询 MiniMax 账户使用量")
    parser.add_argument("--api-key", "-k", required=True, help="MiniMax API Key")
    parser.add_argument("--start-date", "-s", help="开始日期 (YYYY-MM-DD)")
    parser.add_argument("--end-date", "-e", help="结束日期 (YYYY-MM-DD)")
    parser.add_argument("--json", "-j", action="store_true", help="输出 JSON 格式")
    
    args = parser.parse_args()
    
    # 获取账户信息
    try:
        account_info = get_account_info(args.api_key)
    except Exception as e:
        print(f"获取账户信息失败: {e}", file=sys.stderr)
        sys.exit(1)
    
    # 获取使用详情
    try:
        usage_detail = get_usage_detail(
            args.api_key, 
            args.start_date, 
            args.end_date
        )
    except Exception as e:
        print(f"获取使用详情失败: {e}", file=sys.stderr)
        usage_detail = {}
    
    # 输出结果
    if args.json:
        output = {
            "account": account_info,
            "usage": usage_detail
        }
        print(json.dumps(output, ensure_ascii=False, indent=2))
    else:
        print("=" * 50)
        print("🤖 MiniMax 账户使用量查询")
        print("=" * 50)
        
        # 账户信息
        if account_info.get("code") == 0 and "data" in account_info:
            data = account_info["data"]
            print(f"\n📊 账户信息:")
            print(f"   用户名: {data.get('user_name', 'N/A')}")
            print(f"   账户类型: {data.get('account_type', 'N/A')}")
            
            if "balance" in data:
                balance = data["balance"]
                print(f"\n💰 余额信息:")
                print(f"   总余额: {format_currency(balance.get('total_amount', 0))}")
                print(f"   赠送余额: {format_currency(balance.get('granted_amount', 0))}")
                print(f"   付费余额: {format_currency(balance.get('paid_amount', 0))}")
                print(f"   冻结金额: {format_currency(balance.get('frozen_amount', 0))}")
        
        # 使用详情
        if usage_detail.get("code") == 0 and "data" in usage_detail:
            data = usage_detail["data"]
            if "usages" in data:
                print(f"\n📈 使用详情:")
                for usage in data["usages"]:
                    model = usage.get("model", "N/A")
                    usage_amount = format_currency(usage.get("usage_amount", 0))
                    print(f"   {model}: {usage_amount}")
        
        print("\n" + "=" * 50)
        print("💡 更多信息请访问: https://platform.minimaxi.com/accountcenter")
        print("=" * 50)


if __name__ == "__main__":
    main()
