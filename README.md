# API Documentation for Soif Drip Irrigation and Garden Monitoring App

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/02786d3d4d1c4fb3bd7261eb69d069f2)](https://www.codacy.com/manual/forkbomb-666/drip_irrigation_server?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=forkbomb-666/drip_irrigation_server&amp;utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.org/forkbomb-666/drip_irrigation_server.svg?branch=master)](https://travis-ci.org/forkbomb-666/drip_irrigation_server) [![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

<img src="https://github.com/forkbomb-666/drip_irrigation_server/raw/master/static/plant.png" width=75 /><img src="https://github.com/forkbomb-666/drip_irrigation_server/raw/master/static/soif_logo.png" width="175" />

### BaseURL

[https://soif.herokuapp.com/](https://soif.herokuapp.com/)

### Endpoints

| Sl. | Endpoint | Usage | Method | Response Type |
| --- | --- | :-- | :-: | :-: |
| 1 | `/` | Show this Documentation | `GET` | `text/html` |
| 2 | `/getdata/now` | Get all latest sensor data updates | `GET` | `application/json` |
| 3 | `/getdata/<string:date>` | Get all sensor data for a given day. Date format to be passed : `dd-mm-yyyy` | `GET` | `application/json` |
| 4 | `/getdata/<string:date>/<string:sensor>` | Get a specific sensor data for a given day | `GET` | `application/json` |
| 5 | `/insertdata` | Insert all sensor data into database | `POST` | `application/json` |
| 6 | `/setpump` | Set moisture threshold for automatic water pump | `POST` | `application/json` |
| 7 | `/getpump` | Read the threshold value from the server | `GET` | `application/json` |
| 8 | `/deletedata/<string:date>` | Delete all sensor data for a given day | `DELETE` | `application/json` |

### JSON Templates

`/getdata/now` :

```json
{
  "humidity": 0.77, 
  "light": 425, 
  "moisture": {
    "plant0": 0.47, 
    "plant1": 0.72
  }, 
  "temparature": 33.2
}
```

`/getdata/<dd-mm-yyyy>` :

```json
{
  "moisture": {
    "plant0": [],
    "plant1": []
  },
  "temparature": [],
  "humidity": [],
  "light": []
}
```

`/getdata/<dd-mm-yyyy>/light` :

```json
{
  "records": [
    {
      "light": [
        0,
        6.67,
        5.83,
        5.83,
        6.67,
        273.33,
        600.83,
        523.33,
        6.67,
        5.83,
        6.67
      ]
    }
  ]
}
```

`/insertdata`:

```json
{
  "moisture": {
    "plant0": 0.0,
    "plant1": 0.0
  },
  "temparature": 0.0,
  "humidity": 0.0,
  "light": 0.0
}
```

`/setpump`:

```json
{"pump0": 0.0, "pump1": 0.0}
```

`/getpump` :

```json
{
  "settings": {
    "pump0": 0.0, 
    "pump1": 0.0
  }
}
```
