# wealth_tracker

`wealth_tracker` 是 一个支持各种金融数据查询的 Python 客户端。

## 安装
在项目根目录执行
```bash
pip install ./finclaw_sdk-0.1.0-py3-none-any.whl
```

## 快速开始

```python
from finclaw_sdk import FinclawClient

client = FinclawClient(api_key="<YOUR_API_KEY>")
try:
    resp = client.industry_news_viewpoints(query="最近会降息吗？/黄金行业表现如何？...")
    print(resp)
finally:
    client.close()
```