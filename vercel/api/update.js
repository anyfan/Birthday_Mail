const api_db = require('./lib/db')
const solar2lunar = require('./lib/lunar')

const db = new api_db(process.env.API_KEY)
const s2l = new solar2lunar()

module.exports = async (req, res) => {

    var req_data = {
        "birth_y": null,
        "solar_cal": null,
        "lunar_cal": null,
        "lunar_text": null,
        "name": req.query.name,
        "mail": req.query.mail,
        "receive_solar": req.query.receive_solar,
        "receive_lunar": req.query.receive_lunar
    }

    if (req.query.birthday) {
        s2l.setdate(req.query.birthday)
        req_data["birth_y"] = s2l.birth_y()
        req_data["solar_cal"] = s2l.solar_cal()
        req_data["lunar_cal"] = s2l.lunar_cal()
        req_data["lunar_text"] = s2l.lunar_text()
    }

    if (req.query.id == null) {
        res.json({
            "err": "缺少id参数"
        })
    } else {
        db.setid(req.query.id)
        res.json(await db.update(req_data))
    }
}