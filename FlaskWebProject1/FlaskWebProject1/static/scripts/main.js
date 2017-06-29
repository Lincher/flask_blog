function login() {
    layer.open({
        type: 2,
        title: '用户登录',
        shadeClose: true, //点击遮罩关闭层  
        area: ['400px', '320px'],
        content:"/static/html/login.html" //弹框显示的url  
    });
//     window.location.href='http://www.baidu.com/';
}