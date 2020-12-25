$(document).ready(function() {
    // здесь происходит сам процесс записи пациентов
    // скрипт проверяет есть ли свободное время в выбранный день
    // и если нет то предлагает другой с рекомендациями
    $(document).on('click', '.btn-primary', function() {
        var medic = $('#id_medication').val()
        var ddy = $(this)
        var selected_day = ddy.attr('id').split('-')
        var day = selected_day[0]
        var mont = selected_day[1]
        var year = selected_day[2]
        console.log(day + "  " + medic)
        $.ajax({
            url: '/free_time/' + day + '-' + mont + '-' + year + '-' + medic + '/',
            type: 'GET',
            success: function(result) {
                $('.hidden-block-window').html(result)
            }
        })
    })
})