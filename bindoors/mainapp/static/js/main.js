$(".modal_modal").each(function () {
    $(this).wrap('<div class="overlay"></div>')
});

$(".open-modal_modal").on('click', function (e) {
    e.preventDefault();
    e.stopImmediatePropagation;

    var $this = $(this),
        modal_modal = $($this).data("modal_modal");

    $(modal_modal).parents(".overlay").addClass("open");
    setTimeout(function () {
        $(modal_modal).addClass("open");
    }, 350);

    $(document).on('click', function (e) {
        var target = $(e.target);

        if ($(target).hasClass("overlay")) {
            $(target).find(".modal_modal").each(function () {
                $(this).removeClass("open");
            });
            setTimeout(function () {
                $(target).removeClass("open");
            }, 350);
        }

    });

});

$(".close-modal_modal").on('click', function (e) {
    e.preventDefault();
    e.stopImmediatePropagation;

    var $this = $(this),
        modal_modal = $($this).data("modal_modal");

    $(modal_modal).removeClass("open");
    setTimeout(function () {
        $(modal_modal).parents(".overlay").removeClass("open");
    }, 350);

});

$('a[href^="#"]').click(function (e) {
    e.preventDefault();
    const elementClick = $(this).attr("href");
    const destination = $(elementClick).offset().top;
    $('html').animate({scrollTop: destination}, 1000);
});

$(document).ready(function () {
    $('.quiz__to2').on('click', function () {
        setTimeout(function () {
            $('.quiz__1').css('opacity', '0');
        }, 300);
        setTimeout(function () {
            $('.quiz__1').css('display', 'none');
            $('.quiz__2').css('display', 'block');
        }, 600);
        setTimeout(function () {
            $('.quiz__2').css('opacity', '1');
        }, 900);
    });
    $('.quiz__to3').on('click', function () {
        setTimeout(function () {
            $('.quiz__2').css('opacity', '0');
        }, 300);
        setTimeout(function () {
            $('.quiz__2').css('display', 'none');
            $('.quiz__3').css('display', 'block');
        }, 600);
        setTimeout(function () {
            $('.quiz__3').css('opacity', '1');
        }, 900);
    });
    $('.quiz__to4').on('click', function () {
        setTimeout(function () {
            $('.quiz__3').css('opacity', '0');
        }, 300);
        setTimeout(function () {
            $('.quiz__3').css('display', 'none');
            $('.quiz__4').css('display', 'block');
        }, 600);
        setTimeout(function () {
            $('.quiz__4').css('opacity', '1');
        }, 900);
    });
    $('.quiz__to5').on('click', function () {
        setTimeout(function () {
            $('.quiz__4').css('opacity', '0');
        }, 300);
        setTimeout(function () {
            $('.quiz__4').css('display', 'none');
            $('.quiz__5').css('display', 'block');
        }, 600);
        setTimeout(function () {
            $('.quiz__5').css('opacity', '1');
        }, 900);
    });
});