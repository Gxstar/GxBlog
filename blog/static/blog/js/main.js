$(function(){
    $(`li[id=${ActivePage}]`).addClass('active');
    // 处理第一页最后一页按钮不可用
    if (ActivePage==1) {
        $("#FrontPage").addClass('disabled');
    };
    if(ActivePage==TotalPage) {
        $("#BackPage").addClass('disabled');
    };
    // 设置前一页后一页链接地址
    var FrontPage=ActivePage-1;
    var BackPage=ActivePage+1;
    $("#FrontPage>a").attr("href",`./?page=${FrontPage}`);
    $("#BackPage>a").attr("href",`./?page=${BackPage}`);
    //设置首页封面宽高比
    var imgwidth=$(".content img").css("width");
    imgwidth=parseFloat(imgwidth)
    $(".content img").css("height",imgwidth*0.75);
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
