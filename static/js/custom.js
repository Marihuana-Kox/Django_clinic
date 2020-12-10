$(document).ready(function () {
    var last_day = 0
    var days = ''
    var cur_day = 0
    cur_day = parseInt($(".col-days-today").html())
    $(".col-days").each(function(){
        days = $(this)
        last_day = days.html()
        if (last_day < cur_day){
            days.css({'cursor': 'crosshair'})
        }
    })
    $(".col-days, .col-days-today").each(function(){
        var days = $(this)
        var cursor = days.css('cursor')
        if (cursor == 'pointer'){
            days.mouseover(function(){
                days.addClass('active-1d')
            })
        }
    })
})