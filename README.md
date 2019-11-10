# Geo API

`last updated: 11-09-2019`

## Overview

Geo API is an open source API for querying geographical data. All data is sourced from open source providers.

## Getting started
You have two options to get started using the Geo API. 

#### Self Hosted
If you want to run the API on your own servers and add permission, feel free to fork the repository and make changes as needed.

Local
> docker-compose up

Production
> docker-compose -f docker-compose-prod.yml up

#### Cloud
Nomadicode maintains https://geo.nomadicode.com. The API contains the latest approved and finalized changes in this repo.


## Documentation

##### Continents
**_Response format_**
```
{
    id: int,
    name: string,
    code: string (2 chars)
}
```

**_Endpoints_**
```
/continents - Returns a list of all the continents
/continents/:id - Returns the continent matching the provided id
/continents/:code - Returns the continent matching the provided 2 character code. Case Insensitive
```
##### Countries
**_Response format_**
```
{
    id: uuid,
    name: string,
    alpha_2_code: string (2 chars),
    alpha_3_code: string (3 chars),
    calling_code: string,
    capital_city: string,
    native_name: string,
    continent: int
}
```

**_Endpoints_**
```
/countries - Returns a list of all the countries
/countries/:id - Returns the country matching the provided id
/countries/:code - Returns the country matching the provided 2 character code. Case Insensitive
/continents/(:id|:code)/countries - Returns a list of all countries on the provided continent
```

##### Regions
**_Response format_**
```
{
    id: uuid,
    name: string,
    code: string (2 chars),
    country: uuid key
}
```

**_Endpoints_**
```
/regions - Returns a list of all the regions
/regions/:id - Returns the region matching the provided id
/countries/(:id|:code)/regions - Returns a list of all regions in the provided country
```

##### Cities
> Coming soon

##### Airports
> Coming soon

## Contributing
If you find any of the provided data to be inaccurate or missing, submit a bug request with the information that is missing or incorrect.

If you find a bug in any of the endpoints, submit a bug request with steps to reproduce the error if relevant.

If you would like to fix a bug or update documentation, fork the repo and submit the changes via a pull request.

## Contributors
[Jamahl Middleton](https://github.com/Jammidd) 

## License
This package is licensed under the MIT license
