---
name: wealth_tracker
description: "wealth_tracker 是 一个全面的金融skills指南。面向金融从业人员的 FinclawClient 使用说明。"
---

# 安装
```bash
git clone git@github.com:fintechclaw/wealth-tracker.git
cd wealth-tracker
pip install ./finclaw_sdk-0.1.0-py3-none-any.whl
```
# 快速开始
初始化最小可运行示例：
```python
from finclaw_sdk import FinclawClient

client = FinclawClient(api_key="<YOUR_API_KEY>")
try:
    resp = client.industry_news_viewpoints(query="最近会降息吗？/黄金行业表现如何？...")
    print(resp)
finally:
    client.close()
```

## 通用使用规则（建议先看）

- 鉴权：需要去找FinclawClient的维护人员申请体验 API Key。
- 调用风格：所有接口均为 `client.<method>(**kwargs)`。
- 股票代码建议使用带交易所后缀格式：如 `600519.SH`。

## 模块与方法速查

### 1) Search（行业/个股资讯、新闻、观点等文本分析内容）

- `client.industry_news_viewpoints(query: str, start_time: str | None = None, end_time: str | None = None, count: int = 10)`
  - 功能：搜索行业/个股问题相关的资讯、新闻、观点等文本分析内容。
  - 参数：
    - `query`（必填，`str`）：用户问题。
    - `start_time`（可选，`str | None`）：开始时间，支持 `YYYY-MM-DD` 或 `YYYY-MM-DD HH:MM:SS`。
    - `end_time`（可选，`str | None`）：结束时间，支持 `YYYY-MM-DD` 或 `YYYY-MM-DD HH:MM:SS`。
    - `count`（可选，`int`，默认 `10`）：返回条数，范围 `[1, 50]`。

### 2) Stock（个股行情、财务、基本信息、分析等）
- `client.stock_basic(thscode: str | None = None, stock_name: str | None = None, industry01: str | None = None, industry02: str | None = None, industry03: str | None = None)`
  - 功能：股票基础信息检索（可按名称/行业筛选）,其中 `thscode` 是股票代码，`stock_name` 是股票名称，`industry01`、`industry02`、`industry03` 是申万一二三级行业分类。
  - 参数要求：
    - `thscode`、`stock_name`、`industry01`、`industry02`、`industry03` 中至少有一个非 `None`。
  - 用途举例：
    - 查询600519.SH的公司中文名称、所属申万一二三级行业分类。
    - 查询stock_name="贵州茅台"的公司中文名称、所属申万一二三级行业分类。
    - 查询申万一级行业分类为“食品饮料”的所有股票信息（所属申万一二三级行业分类）。
    - 查询申万二级行业分类为“XX”的所有股票信息（所属申万一二三级行业分类）。
    - 查询申万三级行业分类为“XX”的所有股票信息（所属申万一二三级行业分类）。

- `client.single_stock_analysis(thscode: str, start_period: str | None = None, end_period: str | None = None, n_quarters: int = 12, dimensions: list[str] | None = ['盈利能力','成长性','偿债与流动性','运营效率','现金流质量'], custom_panels: dict[str, list[str]] | None = None)`
  - 功能：个股财务分析（盈利能力、成长性、偿债与流动性、运营效率、现金流质量等）。
  - 参数：
    - `thscode`（必填，`str`）：股票代码，如 `600519.SH`。
    - `start_period`（可选，`str | None`）：开始期间，如 `2022Q1` / `2022-03-31` / `20220331`三种格式均兼容。
    - `end_period`（可选，`str | None`）：结束期间，如 `2024Q4` / `2024-12-31` / `20241231`三种格式均兼容。
    - `n_quarters`（可选，`int`，默认 `12`）：未指定期间时，返回最近 N 个季度股票重要财务指标表现。
    - `dimensions`（可选，`list[str] | None`）：分析维度列表，支持 `盈利能力`、`成长性`、`偿债与流动性`、`运营效率`、`现金流质量` 五个维度，不传默认返回全部相关维度财务指标信息。
    - `custom_panels`（可选，`dict[str, list[str]] | None`）：自定义指标分组。
      - 例如：{'自定义指标维度名称':['营业总收入','营业总成本','销售费用','销售费用占营收比','净运营资本_同比']}
      - 支持的三大指标名称有：请查看 `references/fin_schema.md`。自定义指标分组时，指标名称必须在 `references/fin_schema.md` 中定义。

- `client.single_stock_market_daily_analysis(thscode: str, start_date: str | None = None, end_date: str | None = None, n_days: int = 120, trade_date: str | None = None)`
  - 功能：个股日线行情数据（每日收盘价、涨跌幅、成交额、换手率、PE(TTM)、PB等）。
  - 参数：
    - `thscode`（必填，`str`）：股票代码，如 `600519.SH`。
    - `start_date`（可选，`str | None`）：开始日期（`YYYY-MM-DD`或`YYYYMMDD`）。
    - `end_date`（可选，`str | None`）：结束日期（`YYYY-MM-DD`或`YYYYMMDD`）。
    - `n_days`（可选，`int`，默认 `120`）：未给开始/结束日期时使用。
    - `trade_date`（可选，`str | None`）：估值分位目标交易日（`YYYY-MM-DD`），默认给定时间范围内的最新交易日。

- `client.fina_mainbz(thscode: str, period: str | None = None, start_date: str | None = None, end_date: str | None = None)`
  - 功能：主营业务构成和收入情况查询。
  - 参数：
    - `thscode`（必填，`str`）：股票代码，如 `600519.SH`。
    - `period`（可选，`str | None`）：报告期，如 `20171231`（年报）、`20170630`（半年报）、`20170930`（三季报）、`20180331`（一季报）。
    - `start_date`（可选，`str | None`）：公告日范围，通常为 `YYYYMMDD`。
    - `end_date`（可选，`str | None`）：公告日范围，通常为 `YYYYMMDD`。
  - 说明：
    - 如指定获取一个报告期的主营业务构成数据设置period参数。
    - 如需获得期间范围的主营业务构成数据设置start_date和end_date参数。

- `client.top10_holders(thscode: str)`
  - 功能：前十大股东和占比查询。

- `client.monthly(ts_code: str | None = None, trade_date: str | None = None, start_date: str | None = None, end_date: str | None = None)`
  - 功能：个股历史月线。

- `client.stk_managers(thscode: str)`
  - 功能：获取公司简介、主要业务范围、公司注册地、公司官网、公司法人等信息。

### 3) Sector（申万行业分析）

- `client.industry_market_analysis(industry_level: str = "industry01", industry_name: str = "食品饮料", start_date: str | None = None, end_date: str | None = None)`
  - 功能：行业行情 K 线分析。
  - 参数：
    - `industry_level`（可选，`str`）：`industry01` / `industry02` / `industry03`。
    - `industry_name`（必填，`str`）：行业名称，如“银行”“证券”“食品饮料”。
    - `start_date`（可选，`str | None`）：开始日期（`YYYY-MM-DD`或`YYYYMMDD`）。
    - `end_date`（可选，`str | None`）：结束日期（`YYYY-MM-DD`或`YYYYMMDD`）。
  - 说明：
    - 如未指定开始/结束日期，默认返回最近 90 天数据。
    - 支持申万一二三级行业的行情查询，大部分情况industry_level可不填写，防止存在一二三级行业名称相同的情况需特殊说明。

- `client.industry_crowding_analysis(industry_name: str = "食品饮料", trade_date: str | None = None)`
  - 功能：申万行业拥挤度分析。
  - 参数：
    - `industry_name`（必填，`str`）：行业名称，如“银行”、“食品饮料”、“黄金”。
    - `trade_date`（可选，`str | None`）：交易日，`YYYY-MM-DD`或`YYYYMMDD`。
  - 说明：
    - industry_name支持申万一级行业、二级行业、三级行业。
    - trade_date不写则为最新当天日期。

- `client.industry_leader_mktcap_analysis(industry_name: str = "食品饮料", top_n: int = 10)`
  - 功能：获取行业龙头公司（按市值取前top_n家公司作为龙头公司），以及最新close价格。
  - 参数：
    - `industry_name`（必填，`str`）：行业名称，同上支持申万一二三级行业。
    - `top_n`（可选，`int`，默认 `10`）：取前 top_n 家公司作为龙头公司。
  - 说明：
    - 获取完行业龙头公司后可分别调用个股的财务、行情分析接口进一步分析行业龙头个股情况

- `client.industry_valuation_analysis(industry_level: str = "industry01", industry_name: str = "食品饮料")`
  - 功能：行业估值分析。
  - 参数：
    - `industry_name`（必填，`str`）：行业名称，万一二三级行业。
    - `industry_level`（可选，`str`）：`industry01` / `industry02` / `industry03`。一般情况下无需填写，除非同名。

- `client.industry_knowledge_graph(category: str)`
  - 功能：行业研究知识图谱。
  - 参数：
    - `category`（必填，`str`）：行业名称。返回数据包含行业重要的数据可用来做图展示、行业分析思路等。
    - 宏观研究category支持：["美国宏观", "美国宏观", "中国A股", "中国债券"]，例如需要分析当前的A股大盘、债券宏观表现等
    - 分申万子行业研究支持的列表见：references/support_category.md

### 4) Funds（基金）

- `client.funds_info(query: str)`
  - 功能：基金基础信息查询。
  - 参数：
    - `query`（必填，`str`）：基金关键词/代码。如159005.SZ/汇添富收益快钱货币A/汇添富收益

- `client.funds_market(query: str, start_date: str | None = None, end_date: str | None = None, limit: int = 60)`
  - 功能：基金行情数据查询。
  - 参数：
    - `query`（必填，`str`）：基金关键词/代码，同上。
    - `start_date`、`end_date`（可选，`str | None`）：`YYYY-MM-DD`或`YYYYMMDD`。
    - `limit`（可选，`int`，默认 `60`）：返回条数，范围通常 `1~500`。

### 5) Indexes（指数）

- `client.indexes_info(query: str)`
  - 功能：指数基础信息查询。
  - 参数：
    - `query`（必填，`str`）：指数关键词/代码。如000001.SH/上证指数/上证

- `client.indexes_market(query: str, start_date: str | None = None, end_date: str | None = None, limit: int = 60)`
  - 功能：指数行情数据查询。
  - 参数同上。

### 6) Special（市场专题/异动等深度分析）

- `client.market_report(report_type: str)`
  - 功能：A股大盘报告早报/午报/晚报，如果需要每天早上、中午、晚上总结大盘走势等综合信息调用该接口。
  - 参数：
    - `report_type`（必填，`str`），可选 `morning` / `noon` / `evening`。

- `client.anomaly_sector(trade_date: str)`
  - 功能：获取指定日期内异动板块名称和异动幅度列表。
  - 参数：
    - `trade_date`（必填，`str`），格式`YYYYMMDD`。

- `client.anomaly_sector_analyze(trade_date: str, sector_name: str)`
  - 功能：指定日期和异动板块名称对其进行深度分析，分析其背后的异动原因。
  - 参数：
    - `trade_date`（必填，`str`），格式`YYYYMMDD`。
    - `sector_name`（必填，`str`）：板块名称。

- `client.realtime_anomaly_stock()`
  - 功能：获取最近5min内的实时异动个股。
  - 参数：无。

- `client.stocks_cot_data(instruments: dict[str,int])`
  - 功能：获取当前个股和场内基金持仓组合对应的风险和关系矩阵。
  - 参数：
    - `instruments`（必填，`dict[str,int]`）：个股和基金持仓组合列表，例如 `{"000001.SZ": 100,
    "000002.SZ": 200}` 格式，str为标的代码，int对应持仓数量。

- `client.continuous_limit()`
  - 功能：获取A股大盘连板（连续涨跌停大于等于2天）情况。
  - 参数：无。

- `client.limit_info(trade_date: str)`
  - 功能：获取A股市场指定交易日的涨跌停信息。包括分申万一级行业统计涨跌停数量和对应的涨跌停个股。
  - 参数：
    - `trade_date`（必填，`str`），格式`YYYYMMDD`。
  - 说明：
    - trade_date当天如果还没有闭市则反应实时信息。

## 常见调用模板
### 1. 个股深度体检（基本面 + 估值 + 技术面）
**适用场景**：研究员需要快速对某只股票（例如“贵州茅台”）进行全方位的基本面分析、当前估值判断及技术面动向摸底。

**调用流程**：
1. **获取股票基础信息**：确认公司代码和所属申万行业。
   - `client.stock_basic(stock_name="贵州茅台")` -> 拿到 `600519.SH` 及其行业。
2. **查询公司简介与核心高管**：了解公司背景。
   - `client.stk_managers(thscode="600519.SH")`
3. **拆解主营业务构成**：看看公司到底靠什么赚钱。
   - `client.fina_mainbz(thscode="600519.SH")`
4. **全面财务诊断（近3年/12个季度）**：评估其盈利能力和成长性。
   - `client.single_stock_analysis(thscode="600519.SH", n_quarters=12)`
5. **近期行情与估值快照**：看目前的 PE(TTM)、PB 是否处于历史低位。
   - `client.single_stock_market_daily_analysis(thscode="600519.SH", n_days=120)`
6. **筹码结构分析**：看前十大股东是谁，机构占比多少。
   - `client.top10_holders(thscode="600519.SH")`
7. **补充近期舆情与观点**：看看最近市场对它的看法。
   - `client.industry_news_viewpoints(query="贵州茅台最近一季度的业绩预期如何？")`

### 2. 行业景气度与投资机会挖掘（自上而下研究）
**适用场景**：基金经理或策略研究员想要了解某个行业（例如“食品饮料”或细分赛道“白酒”）的当前景气度、市场拥挤度，并筛选出龙头标的。

**调用流程**：
1. **行业知识图谱**：快速掌握行业研究的分析框架和关键数据指标。
   - `client.industry_knowledge_graph(category="食品饮料")`
2. **行业行情回顾**：看看板块最近几个月的走势。
   - `client.industry_market_analysis(industry_name="食品饮料", start_date="2025-10-01", end_date="2026-03-20")`
3. **行业估值水平评估**：判断当前行业估值处于历史什么分位。
   - `client.industry_valuation_analysis(industry_name="食品饮料")`
4. **拥挤度预警**：判断交易是否过热，是否面临回调风险。
   - `client.industry_crowding_analysis(industry_name="食品饮料")`
5. **筛选龙头公司（Top 10）**：找出行业内市值最大的核心标的。
   - `client.industry_leader_mktcap_analysis(industry_name="食品饮料", top_n=10)`
6. **龙头个股交叉验证（循环调用）**：对上一步获取的 Top 10 公司代码，批量拉取其财务表现，对比谁的质地更好。
   - `for code in top_10_codes:`
     - `client.single_stock_analysis(thscode=code, dimensions=['盈利能力', '成长性'], n_quarters=4)`
7. **近期行业大事件与研报观点**：
   - `client.industry_news_viewpoints(query="食品饮料行业春节期间动销情况及研报观点")`
8. **进一步获取细分赛道情况**：通过基础信息接口获取细分的行业。
   - `client.stock_basic(industry01="食品饮料")`
   - 继续分析每个细分赛道的景气度、拥挤度、龙头公司等。

### 3. 市场异动复盘与归因分析（盘后作业）
**适用场景**：交易员或分析师在每天收盘后，需要快速复盘当天的市场表现，找出领涨/领跌板块，并深挖其背后的逻辑。

**调用流程**：
1. **获取全局大盘复盘报告**：看今天的宏观走势和整体情绪。
   - `client.market_report(report_type="evening")`
2. **扫描今日异动板块**：找出今天暴涨或暴跌的板块。
   - `client.anomaly_sector(trade_date="20260320")` -> 假设拿到异动板块为“黄金”。
3. **异动板块深度归因**：让 AI 分析这个板块为什么异动（政策刺激？业绩超预期？）。
   - `client.anomaly_sector_analyze(trade_date="20260320", sector_name="黄金")`
4. **验证该板块的龙头个股表现**：结合异动归因，看看龙头的表现是否印证了该逻辑。
   - `client.industry_leader_mktcap_analysis(industry_name="黄金", top_n=5)`
   - 拿代码去调 `client.single_stock_market_daily_analysis(thscode="...", n_days=5)`

### 4. 盘中实时监控与狙击（日内盯盘）
**适用场景**：高频交易员在交易时间内，需要捕捉瞬间的市场变化和个股爆发点。

**调用流程**：
1. **实时大盘情绪快照**：开盘后/午盘快速了解市场风向。
   - `client.market_report(report_type="morning")` 或 `report_type="noon"`
2. **捕获实时异动个股**：每隔几分钟轮询一次，发现资金异动股。
   - `client.realtime_anomaly_stock()` -> 假设拿到异动个股代码 `000xxx.SZ`。
3. **极速基本面排雷**：在决定跟进前，用最快速度排查该股是否有基本面硬伤（只看最近一期财务）。
   - `client.single_stock_analysis(thscode="000xxx.SZ", n_quarters=1)`
4. **极速消息面排查**：看看是不是有什么突发利好/利空。
   - `client.industry_news_viewpoints(query="000xxx.SZ 今天有什么突发利好或利空消息？", count=3)`

### 5. 基金与指数对标研究（大类资产配置）
**适用场景**：FOF 基金经理或理财顾问想要向客户推荐某只基金，需要对比该基金的历史表现与其基准指数的走势。

**调用流程**：
1. **查基金基础信息**：确认基金全称、经理、规模等。
   - `client.funds_info(query="沪深300ETF")` -> 拿到代码 `510300.SH`。
2. **拉取基金近期净值走势**：
   - `client.funds_market(query="510300.SH", limit=120)`
3. **获取对标指数信息**：
   - `client.indexes_info(query="沪深300")` -> 拿到代码 `000300.SH`。
4. **拉取对标指数走势进行对比**：
   - `client.indexes_market(query="000300.SH", limit=120)`
5. **查询宏观/大盘观点**：为客户提供资产配置的定性建议。
   - `client.industry_news_viewpoints(query="当前时点沪深300的配置价值及机构观点")`

### 6. 持仓组合风控与相关性体检（投后管理与调仓）
**适用场景**：基金经理或个人投资者在复盘自己的持仓组合（股票+场内基金）时，需要评估组合是否存在“同涨同跌”的高集中度风险，并根据风险矩阵决定是否需要调仓分散风险。

**调用流程**：
1. **输入当前持仓明细进行风控体检**：获取组合内各标的之间的相关性矩阵和潜在风险点。
   - `client.stocks_cot_data(instruments={"600519.SH": 1000, "000858.SZ": 2000, "510300.SH": 50000})`
2. **风险溯源（基本面排雷）**：如果风控体检提示某只个股（如 `000858.SZ` 五粮液）近期波动风险较大，立刻进行基本面与资金面确认。
   - `client.single_stock_analysis(thscode="000858.SZ", n_quarters=4, dimensions=['盈利能力', '现金流质量'])`
   - `client.industry_news_viewpoints(query="五粮液近期是否存在潜在利空或机构减仓动作？")`
3. **寻找替代标的（降低相关性）**：如果发现白酒持仓过度拥挤，需要切换到其他低相关性行业（如“电力”或“银行”）。
   - `client.industry_crowding_analysis(industry_name="银行")` -> 确认银行板块当前是否拥挤。
   - `client.industry_leader_mktcap_analysis(industry_name="银行", top_n=3)` -> 筛选出低估值替代龙头。

### 7. 市场短线情绪与游资炒作热度分析（打板/情绪周期研究）
**适用场景**：短线游资、打板选手或量化策略研究员，需要感受市场极度活跃资金的炒作温度，判断当前处于“退潮期”还是“主升浪”，并寻找市场最高空间板（龙头妖股）。

**调用流程**：
1. **全局涨跌停情绪扫描**：获取今天的涨跌停家数及各申万一级行业的涨停分布，判断赚钱效应。
   - `client.limit_info(trade_date="20260325")` -> 发现“计算机”和“电子”板块涨停潮。
2. **寻找市场最高度（连板梯队梳理）**：提取大盘连板股票，找出市场空间板（如5连板、6连板个股）。
   - `client.continuous_limit()` -> 获取连板股名单。
3. **定位短线妖股炒作逻辑**：对最高连板的个股（假设为 `000xxx.SZ`）进行消息面及题材挖掘，看看游资到底在炒什么概念。
   - `client.industry_news_viewpoints(query="000xxx.SZ 连板背后的核心炒作题材和市场传闻是什么？", count=5)`
4. **同板块发散与首板挖掘**：根据妖股的题材，找出同行业内尚未大幅启动的其他股票。
   - `client.industry_leader_mktcap_analysis(industry_name="计算机", top_n=10)`
   - `client.single_stock_market_daily_analysis(thscode="...", n_days=5)` -> 观察跟风股的技术形态。

### 8. 极端行情下的板块踩踏与避险分析（黑天鹅事件应对）
**适用场景**：市场遭遇突发重挫（如大盘大跌、千股跌停），研究员需要迅速厘清资金在抛售哪些板块，哪些板块在逆势抗跌（避险属性），从而制定防守策略。

**调用流程**：
1. **获取跌停重灾区数据**：查看今天的跌停板都集中在哪些行业。
   - `client.limit_info(trade_date="20260325")` -> 重点关注返回数据中的跌停统计部分。
2. **异动杀跌归因分析**：如果发现“医药生物”板块出现批量跌停，迅速让 AI 分析原因。
   - `client.anomaly_sector_analyze(trade_date="20260325", sector_name="医药生物")` -> 可能是集采降价或外围制裁传闻。
3. **逆势避险板块扫描**：找出今天逆势大涨的异动板块（例如“煤炭”或“公用事业”）。
   - `client.anomaly_sector(trade_date="20260325")`
4. **避险标的防守配置**：从抗跌的高股息行业中，筛选出基本面最扎实、现金流最好的防守标的。
   - `client.industry_leader_mktcap_analysis(industry_name="煤炭", top_n=5)`
   - `client.single_stock_analysis(thscode="...", dimensions=['现金流质量'], n_quarters=4)`

其他类似场景结合金融知识，参考上述教程进行组合调用和分析决策。