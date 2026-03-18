# wealth_tracker

`wealth_tracker` 是 一个支持各种金融数据查询的 Python 客户端。

## 安装
在项目根目录执行
```bash
pip install -e .
```

## 快速开始

```python
import wealth_tracker as sdk

pro = sdk.pro_api()
data = pro.query_agent(query="25年营业总收入前十的公司有哪些")
print(data)
```

## 常用接口

- Search：
  - `pro.query_agent(...)`
  - `pro.industry_news_viewpoints(...)`
- Stock：
  - `pro.single_stock_analysis(...)`
  - `pro.single_stock_market_daily_analysis(...)`
  - `pro.single_stock_intraday_analysis(...)`
  - `pro.single_stock_snapshot_analysis(...)`
- Sector：
  - `pro.concept_board_analysis(...)`
  - `pro.concept_board_rank_analysis(...)`
  - `pro.concept_board_detail_analysis(...)`
  - `pro.industry_crowding_analysis(...)`
  - `pro.industry_leader_mktcap_analysis(...)`
  - `pro.industry_leader_financial_analysis(...)`
  - `pro.industry_market_analysis(...)`
  - `pro.industry_financial_analysis(...)`
  - `pro.industry_valuation_analysis(...)`
  - `pro.industry_knowledge_graph(...)`
- Data Search：
  - `pro.data_search_skills()`
  - `pro.data_search_query(...)`
