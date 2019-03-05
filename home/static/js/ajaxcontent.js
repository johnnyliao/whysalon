//首頁hairstyle
$(".js-hairstyle a").on("click", function(e) {
    e.preventDefault();
    var href = $(this).attr('href');
    var title = $(this).html();
    $(".js-hairstyle li").each(function(i, e) { $(e).removeClass('active'); });
    $(this).parents('li').addClass('active');
    $.get(href, function(data) {
        $('.hairstylist-index-block').html(data);
        $('.mobile-menu-main-active-title').html(title);
        if ($(window).width() < 1170) {
            $('.js-mobile-menu-main').slideToggle();
        }
    });
});


//魔法部落
var isOK = true;
var scrollH = 0;
var intI = 1;

function initBlog(storeid) {
    //判斷ajax結束了沒
    $(document)
        .ajaxStart(function() {
            isOK = false;
        })
        .ajaxStop(function() {
            isOK = true;
        });
    $(window).scroll(function() {
        document.getElementById("loading").style.top = document.documentElement.scrollTop + "px";
        if ($(document).height() - $(window).scrollTop() - document.documentElement.clientHeight < 600) {
            //往上滾就不要動作
            if (scrollH > document.documentElement.scrollTop) {
                scrollH = document.documentElement.scrollTop;
                return;
            }
            if (isOK) {
                scrollH = document.documentElement.scrollTop;
                isOK = false;
                $.get('/hairstyle/blogdata/' + storeid, function(data) {
                    $('.blog-index-block').append(data);
                });
            }
        }
    });
}


//網友分享
function initHairSnap(storeid) {
    //判斷ajax結束了沒
    $(document)
        .ajaxStart(function() {
            isOK = false;
        })
        .ajaxStop(function() {
            isOK = true;
        });
    $(window).scroll(function() {
        document.getElementById("loading").style.top = document.documentElement.scrollTop + "px";
        if ($(document).height() - $(window).scrollTop() - document.documentElement.clientHeight < 600) {
            //往上滾就不要動作
            if (scrollH > document.documentElement.scrollTop) {
                scrollH = document.documentElement.scrollTop;
                return;
            }
            if (isOK && (document.documentElement.scrollTop - scrollH) > 200) {
                scrollH = document.documentElement.scrollTop;
                isOK = false;
                $.get('/hairstyle/memberstyledata/', function(data) {
                    $('.masonry-content').append(data);
                    $('.masonry-content').masonry('reloadItems');
                    $('.masonry-content').imagesLoaded().progress(function() {
                        $('.masonry-content').masonry('layout');
                    });
                });
            }
        }
    });
}

//流行趨勢
function initHairStyle(typeid) {
    //判斷ajax結束了沒
    $(document)
        .ajaxStart(function() {
            isOK = false;
        })
        .ajaxStop(function() {
            isOK = true;
        });
    $(window).scroll(function() {
        document.getElementById("loading").style.top = document.documentElement.scrollTop + "px";
        if ($(document).height() - $(window).scrollTop() - document.documentElement.clientHeight < 600) {
            //往上滾就不要動作
            if (scrollH > document.documentElement.scrollTop) {
                scrollH = document.documentElement.scrollTop;
                return;
            }
            if (isOK) {
                scrollH = document.documentElement.scrollTop;
                isOK = false;
                $.get('/hairstyle/listd/' + typeid, function(data) {
                    var $content = $(data);
                    $('.masonry-content')
                        .append($content)
                        .masonry('appended', $content)
                        .masonry();

                    $('.masonry-content').imagesLoaded(function() {
                        $('.masonry-content').masonry();
                    });
                });
            }
        }
    });
}


//設計師最愛
$(document).on('click', '.js-stylist-fav', function(e) {
    e.preventDefault();
    var stylistid = $(this).data('favid');
    $.post('/stylist/' + stylistid + '/SetFavorite', null, function(result) {
        if (result.code == '200') {
            alert('加入最愛成功');
            $('a[data-favid="' + stylistid + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle_red.svg)');
            $('a[data-favid="' + stylistid + '"]').find('i.fa-gratipay').css('color', 'red');

        } else {
            alert(result.message);
            $('a[data-favid="' + stylistid + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle.svg)');
            $('a[data-favid="' + stylistid + '"]').find('i.fa-gratipay').css('color', '#000');

        }

    });
});

//分店最愛
$(document).on('click', '.js-store-fav', function(e) {
    e.preventDefault();
    var storeid = $(this).data('favid');
    $.post('/salon/' + storeid + '/SetFavorite', null, function(result) {
        if (result.code == '200') {
            alert('加入最愛成功');
            $('a[data-favid="' + storeid + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle_red.svg)');
            $('a[data-favid="' + storeid + '"]').find('i.fa-gratipay').css('color', 'red');
        } else {
            alert(result.message);
            $('a[data-favid="' + storeid + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle.svg)');
            $('a[data-favid="' + storeid + '"]').find('i.fa-gratipay').css('color', '#000');

        }
    });
});

//文章最愛
$(document).on('click', '.js-article-fav', function(e) {
    e.preventDefault();
    var articleid = $(this).data('favid');
    var fav = parseInt($('.js-fav-count').html());
    console.log(fav);
    $.post('/hairstyle/SetFavorite/' + articleid, null, function(result) {
        if (result.code == '200') {
            alert('加入最愛成功');
            fav++;
            $('.js-fav-count').html(fav);
            $('a[data-favid="' + articleid + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle_red.svg)');
            $('a[data-favid="' + articleid + '"]').find('i.fa-gratipay').css('color', 'red');

        } else if (result.code == '201') {
            alert(result.message);
            fav--;
            $('.js-fav-count').html(fav);
            $('a[data-favid="' + articleid + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle.svg)');
            $('a[data-favid="' + articleid + '"]').find('i.fa-gratipay').css('color', '#000');

        } else {
            alert(result.message);
            $('a[data-favid="' + articleid + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle.svg)');
            $('a[data-favid="' + articleid + '"]').find('i.fa-gratipay').css('color', '#000');

        }
    });
});


function getFavorite() {
    $.get('/memberfav/GetFavorite', function(data) {
        if (data.code == 200) {
            $(data.favid).each(function(i, e) {
                $('a[data-favid="' + e + '"]').find('i.icon-heart-circle').css('background-image', 'url(/content/img/icon_heart_circle_red.svg)');
                $('a[data-favid="' + e + '"]').find('i.fa-gratipay').css('color', 'red');
            });
        }
    });
}

getFavorite();

//由店家找設計師
$(document).on('change', '.js-memberbox-upload-salon', function() {
    var storeid = $(this).val();
    $.get('/stylist/' + storeid + '/getstylistlist', function(data) {
        $('.js-memberbox-upload-stylist').html('');
        $(data).each(function(i, e) {
            $('.js-memberbox-upload-stylist').append('<option value=' + e.ErpID + '>　' + e.Name + '</option>');
        });
    });
});