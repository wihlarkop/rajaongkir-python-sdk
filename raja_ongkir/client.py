from functools import cache
from http import HTTPStatus
from typing import Any

import httpx
from pydantic import BaseModel

from raja_ongkir.const import (
    ACCOUNT_PLAN_LITERAL,
    RAJA_ONGKIR_ACCOUNT_PLAN_PRO,
    RAJA_ONGKIR_ACCOUNT_PLAN_STARTER,
    RAJA_ONGKIR_PRO_URL,
    RAJA_ONGKIR_STARTER_URL,
)
from raja_ongkir.decorator import restricted_to_plans
from raja_ongkir.exception import (
    InvalidAccountPlanException,
    InvalidAPIKeyException,
    RajaOngkirException,
)
from raja_ongkir.schema import (
    CityQueryParams,
    ProvinceQueryParams,
    RajaOngkirBaseResponse, CostBodyRequest,
)


class RajaOngkirAPI:
    def __init__(
            self,
            api_key: str,
            account_plan: ACCOUNT_PLAN_LITERAL = RAJA_ONGKIR_ACCOUNT_PLAN_STARTER
    ):
        if not api_key:
            raise RajaOngkirException("API key is required")

        self._api_key = api_key
        self._account_plan = account_plan

        self._base_url = {
            RAJA_ONGKIR_ACCOUNT_PLAN_STARTER: RAJA_ONGKIR_STARTER_URL,
            RAJA_ONGKIR_ACCOUNT_PLAN_PRO: RAJA_ONGKIR_PRO_URL
        }.get(account_plan)

        if not self._base_url:
            raise InvalidAccountPlanException

    def __http_call_get(self, endpoint: str, query_param: BaseModel) -> httpx.Response:
        headers = {"key": self._api_key}
        query_param = query_param.model_dump(exclude_unset=True, exclude_none=True)

        try:
            response = httpx.get(url=f"{self._base_url}/{endpoint}", headers=headers, params=query_param)
        except httpx.RequestError as e:
            raise RajaOngkirException(message=f"An error occurred while making the HTTP request: {e}") from e

        if response.status_code == HTTPStatus.BAD_REQUEST:
            raise InvalidAPIKeyException()

        return response

    def __http_call_post(self, endpoint: str, data: dict) -> httpx.Response:
        headers = {"key": self._api_key}
        try:
            response = httpx.post(url=f"{self._base_url}/{endpoint}", headers=headers, data=data)
        except httpx.RequestError as e:
            raise RajaOngkirException(message=f"An error occurred while making the HTTP request: {e}") from e

        if response.status_code == HTTPStatus.BAD_REQUEST:
            raise InvalidAPIKeyException()

        return response

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_STARTER, RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    @cache
    def province(
            self,
            is_json: bool = False,
            province_id: int | None = None
    ) -> RajaOngkirBaseResponse | dict[str, Any]:
        response = self.__http_call_get(
            endpoint="province",
            query_param=ProvinceQueryParams(id=province_id)
        )
        result = RajaOngkirBaseResponse(**response.json())
        return result.model_dump(exclude_none=True, exclude_unset=True) if is_json else result

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_STARTER, RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    @cache
    def city(
            self,
            is_json: bool = False,
            city_id: int | None = None,
            province_id: int | None = None
    ) -> RajaOngkirBaseResponse | dict[str, Any]:
        response = self.__http_call_get(
            endpoint="city",
            query_param=CityQueryParams(id=city_id, province_id=province_id)
        )
        result = RajaOngkirBaseResponse(**response.json())
        return result.model_dump(exclude_none=True, exclude_unset=True) if is_json else result

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    def sub_district(self):
        return "Sub-district data"

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_STARTER, RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    def cost(self, payload: CostBodyRequest, is_json: bool = False):
        payload.account_plan = self._account_plan
        response = self.__http_call_post(
            endpoint="cost",
            data=payload.model_dump(exclude_none=True, exclude_unset=True)
        )
        result = RajaOngkirBaseResponse(**response.json())
        return result.model_dump(exclude_none=True, exclude_unset=True) if is_json else result

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    def international_origin(self):
        return "International origin data"

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    def international_destination(self):
        return "International destination data"

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    def international_cost(self):
        return "International cost data"

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    def currency(self):
        return "Currency data"

    @restricted_to_plans([RAJA_ONGKIR_ACCOUNT_PLAN_PRO])
    def waybill(self):
        return "Waybill data"
