$(".sw_fte").on("click", function () {
    $(".sw_ft").addClass("hidden");
    $(".sw_fte").addClass("hidden");
    $(".sw_fts").addClass("hidden");
    $(".sw_ftp").addClass("hidden");
    $(".sw_ftet").removeClass("hidden");
    $(".sw_ftee").removeClass("hidden");
    $(".sw_fteb").removeClass("hidden");
});
$(".sw_fteb").on("click", function () {
    $(".sw_ftet").addClass("hidden");
    $(".sw_ftee").addClass("hidden");
    $(".sw_fteb").addClass("hidden");
    $(".sw_ft").removeClass("hidden");
    $(".sw_fte").removeClass("hidden");
    $(".sw_fts").removeClass("hidden");
    $(".sw_ftp").removeClass("hidden");
});
$(".sw_fts").on("click", function () {
    $(".sw_ft").addClass("hidden");
    $(".sw_fte").addClass("hidden");
    $(".sw_fts").addClass("hidden");
    $(".sw_ftp").addClass("hidden");
    $(".sw_ftst").removeClass("hidden");
    $(".sw_ftse").removeClass("hidden");
    $(".sw_ftsb").removeClass("hidden");
});
$(".sw_ftsb").on("click", function () {
    $(".sw_ftst").addClass("hidden");
    $(".sw_ftse").addClass("hidden");
    $(".sw_ftsb").addClass("hidden");
    $(".sw_ft").removeClass("hidden");
    $(".sw_fte").removeClass("hidden");
    $(".sw_fts").removeClass("hidden");
    $(".sw_ftp").removeClass("hidden");
});
$(".sw_ftp").on("click", function () {
    $(".sw_ft").addClass("hidden");
    $(".sw_fte").addClass("hidden");
    $(".sw_fts").addClass("hidden");
    $(".sw_ftp").addClass("hidden");
    $(".sw_ftpt").removeClass("hidden");
    $(".sw_ftpe").removeClass("hidden");
    $(".sw_ftpb").removeClass("hidden");
});
$(".sw_ftpb").on("click", function () {
    $(".sw_ftpt").addClass("hidden");
    $(".sw_ftpe").addClass("hidden");
    $(".sw_ftpb").addClass("hidden");
    $(".sw_ft").removeClass("hidden");
    $(".sw_fte").removeClass("hidden");
    $(".sw_fts").removeClass("hidden");
    $(".sw_ftp").removeClass("hidden");
});

$(".image-fullscreen_close").on("click", function () {
    $('.image-fullscreen').removeClass('notrans');
    setTimeout(function () {
        $('.image-fullscreen').addClass('hidden');
    }, 500);
});

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