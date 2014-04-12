% include('header.tpl')
    <div class="container">
      <style>
      <!--
        .login {
          border: 2;
        }
        .login.input {
          clear: both;
          float: left;
        }
      -->
      </style>
      <div class="login">
        <form action="/login" method="POST">
          <div class="input">Username: <input type="text" value="" name="username"></div>
          <div class="input">Password: <input type="password" value="" name="password"></div>
          <input type="submit" value="Login" name="submit_btn">
        </form>
      </div>
    </div> <!-- /container -->
% include('footer.tpl')
