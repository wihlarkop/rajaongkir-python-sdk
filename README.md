# Unofficial RajaOngkir SDK for Python

[RajaOngkir](https://rajaongkir.com/) is an API that provides a powerful logistics solution for integrating various
shipping functionalities in Indonesia. For RajaOngkir developer documentation you can
check [here](https://rajaongkir.com/dokumentasi)

This SDK allows you to interact with the RajaOngkir API from your Python code.

## Features

- [x] Get province (Starter and Pro Plan)
- [x] Get City (Starter and Pro Plan)
- [ ] Get Sub district (Pro Plan)
- [x] Check Cost (Starter and Pro Plan)
- [ ] Get International Origin (Pro Plan)
- [ ] Get International Destination (Pro Plan)
- [ ] Check International Cost (Pro Plan)
- [ ] Check Currency (Pro Plan)
- [ ] Check WayBill (Pro Plan)

for another feature will be update soon
## Installation

Install rajaongkir sdk

```bash
  pip install rajaongkir-python-sdk
```

## Usage/Examples

```python
from rajaongkir_python_sdk import RajaOngkirAPI

api_key = "your_api_key"
rajaongkir = RajaOngkirAPI(api_key=api_key) # init new client
response = rajaongkir.province() # for get all province
print(response)
```

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
