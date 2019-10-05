# API Documentation for Soif Drip Irrigation and Garden Monitoring App

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/02786d3d4d1c4fb3bd7261eb69d069f2)](https://www.codacy.com/manual/forkbomb-666/drip_irrigation_server?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=forkbomb-666/drip_irrigation_server&amp;utm_campaign=Badge_Grade) [![Build Status](https://travis-ci.org/forkbomb-666/drip_irrigation_server.svg?branch=master)](https://travis-ci.org/forkbomb-666/drip_irrigation_server)

<img src="https://github.com/forkbomb-666/drip_irrigation_server/raw/master/static/plant.png" width=75 /><img src="https://github.com/forkbomb-666/drip_irrigation_server/raw/master/static/soif_logo.png" width="175" />

#### BaseURL: 

[https://drip-io.herokuapp.com/](https://drip-io.herokuapp.com/)

#### Endpoints:

| Sl. | Endpoint | Usage | Method | Response Type |
| --- | --- | :-- | :-: | :-: |
| 1 | `/` | Show this Documentation | `GET` | `text/html` |
| 2 | `/getdata/now` | Get all latest sensor data updates | `GET` | `application/json` |
| 3 | `/getdata/<string:date>` | Get all sensor data for a given day. Date format to be passed : `dd-mm-yyyy` | `GET` | `application/json` |
| 4 | `/getdata/<string:date>/<string:sensor>` | Get a specific sensor data for a given day | `GET` | `application/json` |
| 5 | `/insertdata` | Insert all sensor data into database | `POST` | `application/json` |
| 6 | `/setthreshold` | Set moisture threshold for automatic water pump | `POST` | `application/json` |
| 7 | `/getthreshold` | Read the threshold value from the server | `GET` | `application/json` |

#### JSON Templates:

`/insertdata`:

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

`/setthreshold`:

```json
{"pump0": 0.0, "pump1": 0.0}
```

