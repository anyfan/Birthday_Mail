const calendar = require("./calendar");


function solar2lunar() {
    var date, lunar_data;
    this.setdate = function (solar_data) {
        date = solar_data.split("-");
        lunar_data = calendar.solar2lunar(date[0], date[1], date[2]);
    };
    this.birth_y = function () {
        return (date[0])
    };
    this.solar_cal = function () {
        let cal = date[1] + date[2]
        return ((cal.charAt(0) == '0') ? cal.substr(1) : cal)
    };
    this.lunar_cal = function () {
        let day = lunar_data.lDay
        day = (day / 10 < 1) ? ('0' + day) : day
        return (lunar_data.lMonth.toString() + day)
    };
    this.lunar_text = function () {
        return lunar_data.gzYear + '年' + lunar_data.IMonthCn + lunar_data.IDayCn
    };
};

module.exports = solar2lunar;