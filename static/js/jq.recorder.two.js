$(document).ready(function() {
    // здесь происходит сам процесс записи пациентов
    // скрипт проверяет есть ли свободное время в выбранный день
    // и если нет то предлагает другой с рекомендациями
    $(document).on('click', '.btn-primary', function() {
        var medic = $('#id_medication').val()
        var ddy = $(this)
        var selected_day = ddy.attr('id').split('-')
        var day = selected_day[0]
        var month = selected_day[1]
        var year = selected_day[2]
        $.ajax({
            url: '/free_time/' + day + '-' + month + '-' + year + '-' + medic + '/',
            type: 'GET',
            success: function(result) {
                $('.hidden-block-window').fadeIn(600)
                $('.recorder-free-time').html(result)
                $('.btn-secondary').click(function() {
                    $('.hidden-block-window').fadeOut(500)
                })
            }
        })
    })
    $(document).on('click', '.select-time', function() {
        var tmblok = $(this)
        var tmselect = tmblok.text()
        if ($('.select-time').hasClass('select-time-active')) {
            $('.select-time').removeClass('select-time-active')
            tmblok.addClass('select-time-active')
            $('.info-label').text("Нажмите кнопку «выбрать».")
            $('.info-label').animate({ fontSize: "1em" }, 1000);
        } else {
            tmblok.addClass('select-time-active')
            $('.info-label').text("Нажмите кнопку «выбрать».")
            $('.info-label').animate({ fontSize: "1em" }, 1000);
        }

        console.log(tmselect)

    })
})