$(document).ready(function () {
    $('.top_section_second .button_fixed').click(function () {
        // $('.button_fixed').css('color', 'green');
        // if ($('.button_fixed').length) {
        //     $('button_fixed').removeClass('button_fixed').addClass('button_fixed_2')
        // }
        // $(this).removeClass('button_fixed_2').addClass('button_fixed')
    })
});
$({Counter: 0}).animate({
    Counter: $('.Single').text()
}, {
    duration: 5000,
    easing: 'swing',
    step: function () {
        $('.Single').text(Math.ceil(this.Counter));
    }
});
$({Counter: 0}).animate({
    Counter: $('.Single1').text()
}, {
    duration: 6000,
    easing: 'swing',
    step: function () {
        $('.Single1').text(Math.ceil(this.Counter));
    }
});
$({Counter: 0}).animate({
    Counter: $('.Single2').text()
}, {
    duration: 7000,
    easing: 'swing',
    step: function () {
        $('.Single2').text(Math.ceil(this.Counter));
    }
});