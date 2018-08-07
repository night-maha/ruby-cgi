function frameClick() {
  var result = true;

  // 入力エラー文をリセット
  $("#s_password_error").empty();
  $("#s_id_error").empty();

  // 入力内容セット
  var s_password  = $("#s_password").val();
  var s_id  = $("#s_id").val();
  var url = "http://10.172.81.244:7110/login.cgi";


  // 入力内容チェック
  // 学籍番号
  if(s_id == ""){
      $("#s_id_error").html("<i class='fa fa-exclamation-circle'></i> 学籍番号は必須です。");
      result = false;
  }else if((!s_id.match(/^[0-9]+$/)) || (s_id.length != 5)){
      $("#s_id_error").html("<i class='fa fa-exclamation-circle'></i> 正しい学籍番号を入力してください。");
      result = false;
  }

  // パスワード
  if(s_password == ""){
      $("#s_password_error").html("<i class='fa fa-exclamation-circle'></i> パスワードは必須です。");
      result = false;
  }else if(!s_password.match(/^[a-z0-9]+$/)){
      $("#s_password_error").html("<i class='fa fa-exclamation-circle'></i> 英数字半角で入力してください。");
      result = false;
  }else if(s_password.length > 12 || s_password.length < 8){
      $("#s_password_error").html("<i class='fa fa-exclamation-circle'></i> 8字以上12字以内で入力してください。");
      result = false;
  }

 //想定していた入力だった場合、値をlogin.cgiにPOSTで送る
  if(result == true){
    var f = document.forms["stu_login"];
      f.method = "POST";
      f.submit();
    /*
    var login_data = {
      "s_id" : s_id,
      "s_password" : s_password
    };

    $.post(url, login_data)
    .done(function(data){
      console.log(data.form);
    })
    document.location.href = url;
    */
  }
}
