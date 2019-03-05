var i = 0;
function loopit(obj) {
    i++;
    if (i > 360)
        i = 0;
    $(obj).css("transform", "rotate(" + i + "deg)")
    .css("-ms-transform", "rotate(" + i + "deg)")
    .css("-moz-transform", "rotate(" + i + "deg)")
    .css("-webkit-transform", "rotate(" + i + "deg)");
    setTimeout(function () {
        loopit(obj)
    }, 10);
}

function useceil(min, max) {
    return Math.ceil(Math.random() * (max - min + 1) + min - 1);
}


function openMenu() {
    overlay = document.createElement('div'); /* 建立一個 div element */
    overlay.id = 'overlay';
    document.body.appendChild(overlay);
    $('#overlay').on('click', function (e) {
        $('.toggle').toggleClass("active");
        $(".mainmenu").slideToggle();
        document.body.removeChild(overlay);
    });
}

$(document).on('click', '.js-form-submit', function (e) {
    e.preventDefault();
    var form = $(this).parent().parent();
    $(form).unbind();
    $(form).data("validator", null);
    $.validator.unobtrusive.parse($(form));
    if ($(form).valid())
        $(form).submit();
});

//使用者上傳
$(document).on('click', '.member-photo-submit', function (e) {
    e.preventDefault();
    if ($('#member-photo-title-input').val()) {
        $(this).prop('disabled', 'disabled');
        document.forms[0].submit();
    } else {
        alert('請輸入標題');
        return;
    }
     
});