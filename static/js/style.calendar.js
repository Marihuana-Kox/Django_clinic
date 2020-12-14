// Здесь создан механизм стилей календаря
// Подключение и изменение классов css получение данных
// из HTML элементов. Сделано это на основе сравнивания текущей даты
// и даты полученной из объекта страницы

$(document).ready(function() {
    var d = new Date();
    var cur_day = d.getDate()
    var year = d.getFullYear()
    var month = d.getMonth() + 1
    var last_day = 0
    var last_month = 0
    var last_year = 0
    var days = ''
    $(".col-days").each(function() {
        days = $(this)
        last_day = days.html()
        last_month = $('.get-last-month').attr('id')
        last_year = $('.get-last-year').html().replace(/^0/, "")
        if (last_year < year) {
            days.css({ 'cursor': 'crosshair' }).addClass('no-active')
            days.attr('id', 'undefined')
        } else if (last_year == year && last_month < month) {
            days.css({ 'cursor': 'crosshair' }).addClass('no-active')
            days.attr('id', 'undefined')
        } else if (last_month == month && last_day < cur_day) {
            days.css({ 'cursor': 'crosshair' }).addClass('no-active')
            days.attr('id', 'undefined')
        }
    })
    $(".col-days, .col-days-today").click(function() {
        var days = $(this)
        var register_date = days.attr('id')
        $.ajax({
            url: '/register/' + register_date + '/',
            type: 'GET',
            date: { 'register_date': register_date },
            success: function(data) {
                $('.modelwindow').html(data)
            },
            failure: function(data) {
                alert('Got an error dude');
            },
        })
    })

})