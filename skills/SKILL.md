---
name: wealth-tracker-usage
description: "使用 wealth_tracker Python 客户端获取专业的金融数据和分析。"
---

# Search SDK 使用 Skill

## 快速开始

```bash
git clone https://github.com/fintechclaw/wealth-tracker.git
```

在仓库根目录内执行安装：

```bash
pip install -e .
```

## wealth_tracker 方法速查

## 1) 初始化最小可运行示例：

```python
import wealth_tracker as sdk
with sdk.pro_api() as pro:
    resp = pro.industry_news_viewpoints(query="黄金最近值得投资吗？")
    print(resp)
```

注意：复杂金融分析/投资等问题需要结合以下多个接口结果综合分析，才能得到全面准确的结论

## 2) Search
有关新闻行业资讯的文本分析接口：
query[str]：为用户关心的问题
如特别提醒某个时间范围，需指定start_time和end_time，格式为YYYY-MM-DD
count[int]：返回数量，默认 `10`，范围 `[1, 50]`
- `pro.industry_news_viewpoints(query, start_time=None, end_time=None, count=10)`

## 3) Stock
个股财务分析接口：
thscode如600519.SH表示600519股票代码，后缀.SH表示上海股票交易所（后缀必须大写）
start_period和end_period代表分析财务时间范围，默认最近12个季度的财务报表数据，如需分析其他时间范围，需指定start_period和end_period，格式为2025Q1(一年四个季度分别为Q1、Q2、Q3、Q4)
dimensions代表分析维度，默认包含["盈利能力","成长性","偿债与流动性","运营效率与营运资本","现金流质量"]相关的财务分析
- `pro.single_stock_analysis(thscode, start_period=None, end_period=None, n_quarters=12, dimensions=None)`

个股日k分析和估值分析接口：
n_days代表查看最近n天的数据，默认120天
如需查看指定日期范围的数据，需指定start_date和end_date，格式为YYYY-MM-DD
- `pro.single_stock_market_daily_analysis(thscode, start_date=None, end_date=None, n_days=120)`

## 4) Sector
每日对应的概念板块涨跌榜（Top/Bottom N） trade_date为指定日期，默认最新交易日如2026-03-17，top_n为返回数量top n和bottom n的数量，默认20
- `pro.concept_board_rank_analysis(trade_date=None, top_n=20)`

申万（一二三级）行业拥挤度分析，当前仅支持申万行业分析，industry_level为行业等级，默认industry01（申万一级行业），industry_name为行业名称，默认食品饮料，trade_date为指定日期，例如交易日2026-03-17
- `pro.industry_crowding_analysis(industry_level="industry01", industry_name="食品饮料", trade_date=None)`

申万（一二三级）行业行情k线分析
- `pro.industry_market_analysis(industry_level="industry01", industry_name="食品饮料", start_date=None, end_date=None)`

申万（一二三级）行业财务分析，注意和下面的行业龙头公司财务分析区分，这里是分析整个行业的财务情况，而不是分析行业龙头公司的财务情况
- `pro.industry_financial_analysis(industry_level="industry01", industry_name="食品饮料", start_period=None, end_period=None)`

申万（一二三级）行业龙头公司（按trade_date当日市值排序选top n家作为该行业龙头公司，分析其近期股价走势情况）
- `pro.industry_leader_mktcap_analysis(industry_level="industry01", industry_name="食品饮料", trade_date=None, top_n=10)`

申万（一二三级）行业龙头公司（按最近交易日市值排序选top n家作为该行业龙头公司，分析指定财报期fin_period如2025Q3的财务情况）
- `pro.industry_leader_financial_analysis(industry_level="industry01", industry_name="食品饮料", fin_period=None, top_n=10)`

最新交易日申万（一二三级）行业估值情况
- `pro.industry_valuation_analysis(industry_level="industry01", industry_name="食品饮料")`

行业研究分析框架（知识图谱），category[str]行业分类为内部支持的行业（多数为申万三级行业），如黄金、饮料乳品、休闲食品等
宏观分析支持category为：中国债券、中国A股、美国宏观、中国宏观
- `pro.industry_knowledge_graph(category)`

## 5) Data Search
罗列当前支持的数据查询技能有哪些，以及如何调用传参
- `pro.data_search_skills()`

基于数据查询技能ID，调用具体的数据查询接口
- `pro.data_search_query(skill_id=None, interface_name=None, params=None)`

## 6) 典型异常

- `PermissionDeniedError`：权限不足
- `RateLimitError`：超频/配额
- `ValidationError`：参数错误
- `ServerError`：服务端 5xx


