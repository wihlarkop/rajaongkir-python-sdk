from typing import Any, Self

from pydantic import BaseModel, Field, model_validator

from raja_ongkir.exception import RajaOngkirException
from raja_ongkir.const import ACCOUNT_PLAN_LITERAL, RAJA_ONGKIR_ACCOUNT_PLAN_STARTER, RAJA_ONGKIR_COURIER


class ProvinceResponse(BaseModel):
    province_id: str
    province: str


class ProvinceQueryParams(BaseModel):
    id: int | None = Field(default=None)


class CityResponse(BaseModel):
    city_id: str
    province_id: str
    province: str
    type: str
    city_name: str
    postal_code: str


class CityQueryParams(BaseModel):
    id: int | None = Field(default=None)
    province_id: int | None = Field(default=None)


class CostItem(BaseModel):
    value: int
    etd: str
    note: str


class Cost(BaseModel):
    service: str
    description: str
    cost: list[CostItem]


class CostResponse(BaseModel):
    code: str
    name: str
    costs: list[Cost]


class CostBodyRequest(BaseModel):
    origin: str = Field()
    origin_type: str | None = Field(default=None, alias="originType")
    destination: str = Field()
    destination_type: str = Field(default=None, alias="destinationType")
    weight: int = Field()
    courier: str = Field()
    length: int | None = Field(default=None)
    width: int | None = Field(default=None)
    height: int | None = Field(default=None)
    diameter: int | None = Field(default=None)
    account_plan: ACCOUNT_PLAN_LITERAL = Field(default=RAJA_ONGKIR_ACCOUNT_PLAN_STARTER)

    @model_validator(mode='after')
    def check_courier(self) -> Self:
        courier = self.courier.lower()
        if courier not in RAJA_ONGKIR_COURIER:
            raise RajaOngkirException(message="Invalid courier")
        return self

    def model_dump(self, exclude_none: bool = True, **kwargs: Any) -> dict[str, Any]:
        result = super().model_dump(exclude_none=exclude_none, **kwargs)

        if self.account_plan == RAJA_ONGKIR_ACCOUNT_PLAN_STARTER:
            result.pop("origin_type", None)
            result.pop("destination_type", None)
            result.pop("length", None)
            result.pop("width", None)
            result.pop("height", None)
            result.pop("diameter", None)

        result.pop("account_plan")

        return result


LIST_RESULTS = list[ProvinceResponse | CityResponse | CostResponse]
SINGLE_RESULTS = ProvinceResponse | CityResponse


class QueryResponse(BaseModel):
    id: str | None = Field(default=None)
    province_id: str | None = Field(None, alias='province')
    origin: str | None = Field(default=None)
    destination: str | None = Field(default=None)
    weight: int | None = Field(default=None)
    courier: str | None = Field(default=None)
    waybill: str | None = Field(default=None)


class StatusResponse(BaseModel):
    code: int
    description: str


class Rajaongkir(BaseModel):
    query: QueryResponse | list | None
    status: StatusResponse
    results: LIST_RESULTS | SINGLE_RESULTS | None
    original_details: CityResponse | None = Field(default=None, alias='original_details')
    destination_details: CityResponse | None = Field(default=None, alias='destination_details')


class RajaOngkirBaseResponse(BaseModel):
    raja_ongkir: Rajaongkir = Field(alias="rajaongkir")
