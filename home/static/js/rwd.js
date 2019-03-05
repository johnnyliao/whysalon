$(document).ready(function () {

    //RWD用的選單
    $(".toggle").click(function () {
        if ($('.toggle').css('display') != 'none') {
            $('.toggle').toggleClass("active");
            $(".mainmenu").slideToggle();
            $("html,body").animate({
                scrollTop: 0
            }, 500);
        }
    });

    //RWD用的內頁選單
    var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
    if (width <= 1170) {
        var actived = $('.tab > ul > li.actived');
        if (actived) {
            $('.tab > ul').remove('li.actived');
            $('.tab > ul').append(actived);
        }

        $('.html-content table, .html-content p').each(function (i, e) {
            if ($(e).width() > $(window).width()) { $(e).css('width', '100%'); }
        });
        $('.html-content img').each(function (i, e) {
            if ($(e).width() > $(window).width()) { alert(e); $(e).css('width', '100%').css('height', 'auto').css('object-fit', 'contain'); }
            else { $(e).css('object-fit', 'contain'); }
        });
    }

    //recome變身
    $('.mainmenu-menu-nav-recome').hover(function (e) {
        $(this).find('img').prop('src', '/content/img/recome_hover.svg');
    },
    function (e) {
        $(this).find('img').prop('src', '/content/img/recome.svg');
    }
    );
    //recome用的RWD選單
    $('.recome-menu-main-active').on('click', function () {
        $('.js-recome-menu-main').slideToggle();
    });
    $('.mobile-menu-main-active').on('click', function () {
        $('.js-mobile-menu-main').slideToggle();
    });

    $('.rslogin').on('click', function (e) {
        e.preventDefault();
        location.href = $(this).attr('href');
    });


    //fb login
    //$(document).on('click', '.member-login-fb a', function (e) {
    //    e.preventDefault();
    //    var url = $(this).attr('href');
    //    var returnUrl = location.pathname;
    //    location.href = url + '?returnurl=' + returnUrl;
    //});

});


