// $()中的函数等整个网页加载完成后才会执行
$(function () {
    function bindCaptchaBtnClick() {
        // 选择id名为captcha-btn的元素绑定点击事件
        $('#captcha-btn').click(function (event) {
            let $this = $(this); // 将js对象变为jquery对象
            let email = $("input[name='email']").val(); // 拿到邮箱的值
            if (!email) { // 如果没有邮箱值则提示输入
                alert("请先输入邮箱");
                return;
            }
            $this.off('click'); // 取消按钮的点击事件

            // 发送Ajax请求
            $.ajax('/auth/captcha?email='+email, {
                method: 'GET',
                success: (result) => {
                    if(result['code'] == 200) {
                        alert("验证码发送成功!");
                    } else {
                        alert(result["message"]);
                    }
                },
                fail: (error) => {
                    console.log(error);
                }
            })

            // 倒计时， 每1000ms执行一次函数
            let timer_num = 180;
            let timer = setInterval(function () {
                if (timer_num <= 0) {
                    $this.text('获取验证码'); // 将文本恢复
                    clearInterval(timer); // 清掉定时器
                    // 重新绑定点击事件
                    bindCaptchaBtnClick(); // 执行一下函数 目的是倒计时过了要使得用户可以重新点击获取验证码框
                    return;
                } else {
                    timer_num--;
                    $this.text(timer_num + "s"); // 显示倒计时
                }
            }, 1000);
        })
    }

    bindCaptchaBtnClick(); // 执行一下函数 目的是倒计时过了要使得用户可以重新点击获取验证码框
});