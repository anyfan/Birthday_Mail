const api_db = require('./lib/db')

const db = new api_db(process.env.API_KEY)

module.exports = async (req, res) => {
    let {
        id
    } = req.query


    if (id == null) {
        res.json({
            "err": "缺少id参数"
        })
    } else {
        db.setid(id)
        let resauit = await db.get(id)
        res.json(resauit)
    }

}