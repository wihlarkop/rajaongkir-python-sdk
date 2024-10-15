from typing import Final, Literal

RAJA_ONGKIR_STARTER_URL: Final = "https://api.rajaongkir.com/starter"
RAJA_ONGKIR_PRO_URL: Final = "https://pro.rajaongkir.com/api"

RAJA_ONGKIR_ACCOUNT_PLAN_STARTER: Final = "starter"
RAJA_ONGKIR_ACCOUNT_PLAN_PRO: Final = "pro"

RAJA_ONGKIR_COURIER = [
    "jne",
    "pos",
    "tiki",
    "rpx",
    "pandu",
    "wahana",
    "sicepat",
    "jnt",
    "pahala",
    "sap",
    "jet",
    "indah",
    "dse",
    "slis",
    "first",
    "ncs",
    "star",
    "ninja",
    "lion",
    "idl",
    "rex",
    "ide",
    "sentral",
    "anteraja",
    "jtl"
]

RAJA_ONGKIR_ALLOWED_FUNCTIONS_STARTER: list[str] = [
    'province',
    'city',
    'cost'
]
RAJA_ONGKIR_ALLOWED_FUNCTIONS_PRO: list[str] = [
    'province',
    'city',
    'sub_district',
    'cost',
    'international_origin',
    'international_destination',
    'international_cost',
    'currency',
    'waybill'
]

ACCOUNT_PLAN_LITERAL = Literal[RAJA_ONGKIR_ACCOUNT_PLAN_STARTER, RAJA_ONGKIR_ACCOUNT_PLAN_PRO]
