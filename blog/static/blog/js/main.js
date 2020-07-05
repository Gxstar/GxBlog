$(function () {
    //设置首页封面宽高比
    var imgwidth = $(".content img").css("width");
    imgwidth = parseFloat(imgwidth)
    $(".content img").css("height", imgwidth * 0.75);
    // 设置分类页面调整显示
    $("#navbar a").removeClass("active");
    setActiveCate();
});

function setActiveCate() {
    if (ActiveCate == 0) {
        $("#index").addClass("active");
    }
    else {
        var aid = "cate" + ActiveCate.toString();
        $("#" + aid).addClass("active");
    }
}
