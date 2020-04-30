$(document).ready(function () {
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
    $('.quiz__next').on('click', function () {

        let $this = $(this),
            quiz = $($this).data("quiz");
        setTimeout(function () {
            $('.quiz__step').css('opacity', '0');
        }, 300);
        setTimeout(function () {
            $('.quiz__step').css('display', 'none');
            $(quiz).css('display', 'block');
        }, 600);
        setTimeout(function () {
            $(quiz).css('opacity', '1');
        }, 900);
    });

    $('.projects__slider').slick({
        arrows: true,
        dots: true,
        adaptiveHeight: true,
    });
    $('.reviews__slider').slick({
        arrows: true,
        dots: true,
        adaptiveHeight: true,
    });

    $('.projects__img').on('click', function () {
        let $this = $(this),
            fls = $($this).data('fls'),
            img = $($this).data('img');
        $(fls).css('display', 'flex').addClass('fls_open');
        $(img).css('display', 'block').addClass('img_open');
        setTimeout(function () {
            $(fls).css('opacity', '1');
        }, 5);
        setTimeout(function () {
            $(img).css('opacity', '1');
        }, 305)
    });
    $('.fullscreen__cross').on('click', function () {
        $('.fullscreen__img').removeClass('img_open');
        $('.fullscreen').removeClass('fls_open');
        $('.fullscreen__img').css('opacity', '0');
        setTimeout(function () {
            $('.fullscreen').css('opacity', '0');
        }, 300);
        setTimeout(function () {
            $('.fullscreen').css('display', 'none');
            $('.fullscreen__img').css('display', 'none');
        }, 605)
    });
    $('.fullscreen__next').on('click', function () {
        let curImg = $('.img_open'),
            curInd = $('.img_open').index() - 1,
            nextInd = curInd + 1,
            nextImg = $('.fls_open>.fullscreen__img').eq(nextInd);
        curImg.css({'transform': 'translateX(-200px)', 'opacity': '0'});
        setTimeout(function () {
            curImg.css({'transform': 'translateX(0)', 'display': 'none'}).removeClass('img_open');
        }, 305);

        if (nextInd == ($('.fls_open>.fullscreen__img:last').index())) {
            $('.fls_open>.fullscreen__img').eq(0).css({'display': 'block', 'transform': 'translateX(200px)'});
            setTimeout(function () {
                $('.fls_open>.fullscreen__img').eq(0).css({
                    'opacity': '1',
                    'transform': 'translateX(0)'
                }).addClass('img_open');
            }, 5)
        } else {
            nextImg.css({'display': 'block', 'transform': 'translateX(200px)'});
            setTimeout(function () {
                nextImg.css({
                    'opacity': '1',
                    'transform': 'translateX(0)'
                }).addClass('img_open');
            }, 5);
        }
    });
    $('.fullscreen__prev').on('click', function () {
        let curImg = $('.img_open'),
            curInd = $('.img_open').index() - 1,
            prevInd = curInd - 1,
            prevImg = $('.fls_open>.fullscreen__img').eq(prevInd);
        curImg.css({'transform': 'translateX(200px)', 'opacity': '0'});
        setTimeout(function () {
            curImg.css({'transform': 'translateX(0)', 'display': 'none'}).removeClass('img_open');
        }, 305);
        prevImg.css({'display': 'block', 'transform': 'translateX(-200px)'});
            setTimeout(function () {
                prevImg.css({
                    'opacity': '1',
                    'transform': 'translateX(0)'
                }).addClass('img_open');
            }, 5);
    });

});