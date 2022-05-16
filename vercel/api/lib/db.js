var axios = require('axios');

class db {
    constructor(API_KEY) {
        this.db_api_url = 'https://data.mongodb-api.com/app/data-hahew/endpoint/data/beta/action/'
        this.headers = {
            'Content-Type': 'application/json',
            'Access-Control-Request-Headers': '*',
            'api-key': API_KEY
        };

    }

    setid(id) {
        this.data = {
            "collection": "users",
            "database": "api",
            "dataSource": "Cluster0",
            "filter": {
                "_id": {
                    "$oid": id
                }
            }
        };
    }

    /**
     * 更新
     */
    async get() {

        const config = {
            method: 'post',
            url: this.db_api_url + 'findOne',
            headers: this.headers,
            // data: JSON.stringify(Object.assign(this.data, get_data))
            data: JSON.stringify(this.data)
        };

        let data;

        await axios(config)
            .then(function (response) {
                data = response.data;
            })
            .catch(function (error) {
                data = error;
            });

        // console.log(JSON.stringify(data));

        return data;

    }

    /**
     * 查找所有 Books 数据
     * @param id
     */
    async update(f) {

        const put_data = {}

        for (var i in f) {
            if (f[i] != null) {
                if (i == "birth_y" || i == "solar_cal" || i == "lunar_cal") {
                    put_data[i] = {
                        "$numberInt": f[i]
                    };
                } else if (i == "receive_solar" || i == "receive_lunar") {
                    put_data[i] = ((f[i]=="true")?true:false);
                } else {
                    put_data[i] = f[i];
                }
            }
        }

        const config = {
            method: 'post',
            url: this.db_api_url + 'updateOne',
            headers: this.headers,
            data: JSON.stringify(Object.assign(this.data, {
                "update": {
                    "$set": put_data
                }
            }))
        };

        // console.log(config)

        let data;

        await axios(config)
            .then(function (response) {
                data = response.data;
            })
            .catch(function (error) {
                data = error;
            });

        // console.log(JSON.stringify(data));

        return data;

    }
}

module.exports = db;