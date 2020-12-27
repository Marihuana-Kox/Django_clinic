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
})