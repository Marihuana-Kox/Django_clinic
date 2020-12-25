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
        if (register_date == 'undefined') {
            return false;
        } else {
            $('.modelwindow').fadeIn(200)
            $('.regDate').fadeIn(600)
            $('.modal-lg h3').text(register_date)
            $('.close-reg-form').click(function() {
                $('.regDate').fadeOut(600)
                $('.modelwindow').fadeOut(200)
            })
        }
    })

    // $('#add-register').click(function(a) {
    //     var date = new Date();
    //     var year = Number(date.getFullYear())
    //     var form = $('#id_disease')
    //     var item = form.val()
    //     var dob = $('#id_dob').val()

    //     if (item == 1) {
    //         form.css({ 'color': 'red' })
    //         a.preventDefault()
    //     }
    //     if (dob.length > 10) {
    //         $('#id_dob').after("<p>Год рождения неверный!</p>")
    //         $('p').delay(2000).fadeOut()
    //         a.preventDefault()
    //     } else {
    //         var list = dob.split('-')
    //         list = Number(list[0])
    //         if (list > 2010 || list < 1930) {
    //             list = year - list
    //             $('#id_dob').after("<p>Вам " + list + " лет? Ваш возраст явно некорректен!</p>")
    //             $('p').delay(3000).fadeOut()
    //             a.preventDefault()
    //         }
    //     }
    // })

    $('#id_disease').click(function() {
        var form = $(this)
        var item = form.val()
        $.ajax({
            url: 'select/' + item + '/',
            type: 'GET',
            success: function(result) {
                if (result) {
                    $('#id_service_diagnos').removeAttr('disabled')
                    $('#id_service_diagnos').html(result)
                }
            }
        })
    })
})