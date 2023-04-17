# crypto-address-generator-api

The aim of this project is to create a REST api to create wallet address. At this stage it only supports two main network being Bitcoin and Ethereum

See [Setup](./docs/setup.md)

**Table of Contents**

- [Introduction](#introduction)
- [Backend Structure](#backend)

### Introduction

The aim of this project is to create an API where it can generate crypto currency wallet address for multiple networks such as `BTC`, `BTG`, `BCH`, `ETH`, `LTC`, `DASH`, `DOGE`.</br>

#### Backend

The backend is based on Python and **Django** framework as the foundation. The application uses **sqlite3** as point of storage for all the data related to each wallet. All sensitive fields are being one-way hashed after they being generated. raw data would be only visible the first time a wallet is being created in order to let user know about the seed and private key information.</br>
The backend contains 4 endpoint:

```
GET - api/healthz/
```

This endpoint in there to make sure the backend is up and running as part of a standard good practice.

```
POST - api/address/
```

Required field : `network` Can be chosen from the list mentioned above

```
GET - api/address/
```

This endpoint will get a list of wallet generated

```
GET - api/address/?wallet_id=<ID>
```

This endpoint takes an ID, and returns the corresponding
address as stored in the database.
