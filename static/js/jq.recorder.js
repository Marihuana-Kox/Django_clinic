import ('../js/jq.recorder.two.js')

$(document).ready(function() {
    var d = new Date();
    var cur_day = d.getDate()
    var year = d.getFullYear()
    var month = d.getMonth() + 1

    function addClassBeforeDays(cur_day, year, month) {
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
    }

    var d = new Date()
    var year = d.getFullYear()
    var month = d.getMonth() + 1

    $("select option[value='']:first").remove()
    $('#id_diagnos').click(function() {
        var id_dias = $(this).val()
        $.ajax({
            url: '/get_medication/' + id_dias + '/',
            type: 'GET',
            success: function(result) {
                if (result) {
                    $('#id_medication, #add-register').removeAttr('disabled')
                    $('#id_medication').html(result)
                    $("#id_diagnos option[value=1]").remove()
                }
            }
        })
    })
    $(document).on('click', '.arr', function() {
        var arr = $(this)
        var cur_data = arr.attr('name')
        var cur_yearmonth = cur_data.split('-')
        var cur_y = cur_yearmonth[0]
        var cur_m = cur_yearmonth[1]
        $.ajax({
            url: '/records/month/' + cur_y + "-" + cur_m + '/',
            type: 'GET',
            success: function(result) {
                var diagnos = $("#id_diagnos").val()
                var medical = $("#id_medication").val()
                if (diagnos && medical) {
                    $('.calendar-view').html(result)
                    $('.calendar-view').fadeIn(1000)
                    addClassBeforeDays(cur_day, year, month)
                }
            }
        })
        return false;
    })
    $(document).on('click', '.get-today', function() {
        $.ajax({
            url: '/records/month/' + year + "-" + month + '/',
            type: 'GET',
            success: function(result) {
                var diagnos = $("#id_diagnos").val()
                var medical = $("#id_medication").val()
                if (diagnos && medical) {
                    $('.calendar-view').html(result)
                    $('.calendar-view').fadeIn(1000)
                    addClassBeforeDays(cur_day, year, month)
                }
            }
        })
    })
    $('#add-register').click(function() {
        var diagnos = $("#id_diagnos").val()
        var medical = $("#id_medication").val()
        if (diagnos && medical) {
            $('.calendar-view').fadeIn(1000)
        }
    })
    $(":button").click(function() {
        $("body,html").animate({
            "scrollTop": '200'
        }, 1000);
        return false;
    });
    // $(window).scroll(function() {
    //     console.log($('body,html').scrollTop())
    // });
    return false;
})