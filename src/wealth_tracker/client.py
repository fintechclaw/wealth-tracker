from __future__ import annotations

from typing import Any, Dict, List, Optional

import httpx

from .exceptions import (
    AuthenticationError,
    PermissionDeniedError,
    RateLimitError,
    ServerError,
    ValidationError,
)


def _raise_for_status(resp: httpx.Response) -> None:
    if resp.status_code < 400:
        return

    try:
        detail = resp.json().get("detail")
    except Exception:
        detail = resp.text

    message = detail or f"HTTP {resp.status_code}"

    if resp.status_code == 400:
        raise ValidationError(message)
    if resp.status_code == 401:
        raise AuthenticationError(message)
    if resp.status_code == 403:
        raise PermissionDeniedError(message)
    if resp.status_code == 429:
        raise RateLimitError(message)
    if resp.status_code >= 500:
        raise ServerError(message)
    raise ServerError(message)


class SearchProClient:
    def __init__(self, *, base_url: str, token: str, timeout: float = 30.0) -> None:
        self.base_url = base_url.rstrip("/")
        self.token = token.strip()
        self._http = httpx.Client(timeout=timeout)

    @property
    def _headers(self) -> Dict[str, str]:
        return {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

    def close(self) -> None:
        self._http.close()

    def __enter__(self) -> "SearchProClient":
        return self

    def __exit__(self, exc_type, exc, tb) -> None:
        self.close()

    def _post(self, path: str, payload: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        resp = self._http.post(url, json=payload, headers=self._headers)
        _raise_for_status(resp)
        return resp.json()

    def _get(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        resp = self._http.get(url, params=params, headers=self._headers)
        _raise_for_status(resp)
        return resp.json()

    def query_agent(
        self,
        *,
        query: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload = {
            "query": query,
            "start_time": start_time,
            "end_time": end_time,
        }
        return self._post("/api/v1/search/query_agent", payload)

    def industry_news_viewpoints(
        self,
        *,
        query: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        count: int = 10,
    ) -> Dict[str, Any]:
        payload = {
            "query": query,
            "start_time": start_time,
            "end_time": end_time,
            "count": count,
        }
        return self._post("/api/v1/search/industry_news_viewpoints", payload)

    def reports_chunks(
        self,
        *,
        query: str,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        count: int = 10,
    ) -> Dict[str, Any]:
        payload = {
            "query": query,
            "start_time": start_time,
            "end_time": end_time,
            "count": count,
        }
        return self._post("/api/v1/search/reports_chunks", payload)

    def single_stock_analysis(
        self,
        *,
        thscode: str,
        start_period: Optional[str] = None,
        end_period: Optional[str] = None,
        n_quarters: int = 12,
        dimensions: Optional[List[str]] = None,
        custom_panels: Optional[Dict[str, List[str]]] = None,
    ) -> Dict[str, Any]:
        payload = {
            "thscode": thscode,
            "start_period": start_period,
            "end_period": end_period,
            "n_quarters": n_quarters,
            "dimensions": dimensions,
            "custom_panels": custom_panels,
        }
        return self._post("/api/v1/stock/single_stock_analysis", payload)

    def single_stock_market_daily_analysis(
        self,
        *,
        thscode: str,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        n_days: int = 120,
        trade_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload = {
            "thscode": thscode,
            "start_date": start_date,
            "end_date": end_date,
            "n_days": n_days,
            "trade_date": trade_date,
        }
        return self._post("/api/v1/stock/single_stock_market_daily_analysis", payload)

    def single_stock_intraday_analysis(
        self,
        *,
        thscode: str,
        trade_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload = {
            "thscode": thscode,
            "trade_date": trade_date,
        }
        return self._post("/api/v1/stock/single_stock_intraday_analysis", payload)

    def single_stock_snapshot_analysis(
        self,
        *,
        thscode: str,
        trade_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload = {
            "thscode": thscode,
            "trade_date": trade_date,
        }
        return self._post("/api/v1/stock/single_stock_snapshot_analysis", payload)

    def concept_board_analysis(
        self,
        *,
        concept_code: Optional[str] = None,
        concept_name: Optional[str] = None,
        trade_date: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        n_days: int = 120,
        top_n: int = 20,
        include_intraday: bool = False,
    ) -> Dict[str, Any]:
        payload = {
            "concept_code": concept_code,
            "concept_name": concept_name,
            "trade_date": trade_date,
            "start_date": start_date,
            "end_date": end_date,
            "n_days": n_days,
            "top_n": top_n,
            "include_intraday": include_intraday,
        }
        return self._post("/api/v1/sector/concept_board_analysis", payload)

    def concept_board_rank_analysis(
        self,
        *,
        trade_date: Optional[str] = None,
        top_n: int = 20,
    ) -> Dict[str, Any]:
        payload = {
            "trade_date": trade_date,
            "top_n": top_n,
        }
        return self._post("/api/v1/sector/concept_board_rank_analysis", payload)

    def concept_board_detail_analysis(
        self,
        *,
        concept_code: Optional[str] = None,
        concept_name: Optional[str] = None,
        trade_date: Optional[str] = None,
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
        n_days: int = 120,
        include_intraday: bool = False,
    ) -> Dict[str, Any]:
        payload = {
            "concept_code": concept_code,
            "concept_name": concept_name,
            "trade_date": trade_date,
            "start_date": start_date,
            "end_date": end_date,
            "n_days": n_days,
            "include_intraday": include_intraday,
        }
        return self._post("/api/v1/sector/concept_board_detail_analysis", payload)

    def industry_crowding_analysis(
        self,
        *,
        industry_level: str = "industry01",
        industry_name: str = "食品饮料",
        trade_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload = {
            "industry_level": industry_level,
            "industry_name": industry_name,
            "trade_date": trade_date,
        }
        return self._post("/api/v1/sector/industry_crowding_analysis", payload)

    def industry_leader_mktcap_analysis(
        self,
        *,
        industry_level: str = "industry01",
        industry_name: str = "食品饮料",
        trade_date: Optional[str] = None,
        top_n: int = 10,
    ) -> Dict[str, Any]:
        payload = {
            "industry_level": industry_level,
            "industry_name": industry_name,
            "trade_date": trade_date,
            "top_n": top_n,
        }
        return self._post("/api/v1/sector/industry_leader_mktcap_analysis", payload)

    def industry_leader_financial_analysis(
        self,
        *,
        industry_level: str = "industry01",
        industry_name: str = "食品饮料",
        fin_period: Optional[str] = None,
        top_n: int = 10,
    ) -> Dict[str, Any]:
        payload = {
            "industry_level": industry_level,
            "industry_name": industry_name,
            "fin_period": fin_period,
            "top_n": top_n,
        }
        return self._post("/api/v1/sector/industry_leader_financial_analysis", payload)

    def industry_market_analysis(
        self,
        *,
        industry_level: str = "industry01",
        industry_name: str = "食品饮料",
        start_date: Optional[str] = None,
        end_date: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload = {
            "industry_level": industry_level,
            "industry_name": industry_name,
            "start_date": start_date,
            "end_date": end_date,
        }
        return self._post("/api/v1/sector/industry_market_analysis", payload)

    def industry_financial_analysis(
        self,
        *,
        industry_level: str = "industry01",
        industry_name: str = "食品饮料",
        start_period: Optional[str] = None,
        end_period: Optional[str] = None,
    ) -> Dict[str, Any]:
        payload = {
            "industry_level": industry_level,
            "industry_name": industry_name,
            "start_period": start_period,
            "end_period": end_period,
        }
        return self._post("/api/v1/sector/industry_financial_analysis", payload)

    def industry_valuation_analysis(
        self,
        *,
        industry_level: str = "industry01",
        industry_name: str = "食品饮料",
    ) -> Dict[str, Any]:
        payload = {
            "industry_level": industry_level,
            "industry_name": industry_name,
        }
        return self._post("/api/v1/sector/industry_valuation_analysis", payload)

    def industry_knowledge_graph(
        self,
        *,
        category: str,
        include_raw: bool = False,
    ) -> Dict[str, Any]:
        payload = {
            "category": category,
            "include_raw": include_raw,
        }
        return self._post("/api/v1/sector/industry_knowledge_graph", payload)

    def data_search_skills(self) -> Dict[str, Any]:
        return self._get("/api/v1/data_search/skills")

    def data_search_query(
        self,
        *,
        skill_id: Optional[str] = None,
        interface_name: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        payload = {
            "skill_id": skill_id,
            "interface_name": interface_name,
            "params": params or {},
        }
        return self._post("/api/v1/data_search/query", payload)
