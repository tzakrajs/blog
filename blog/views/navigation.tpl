    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="#">tz</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              % from bottle import request
              % active = 'class=active'
              % r_path = request.urlparts.path
              % paths = ('/', 'Home'), \
              %         ('/about', 'About'), \
              %         ('mailto:tzakrajs@gmail.com', 'Contact')
	      % for path, label in paths:
              % 
              <li {{active if r_path == path else None}}>
                <a href="{{path}}">{{label}}</a>
              </li>
              % end
              <li {{active if r_path == '/login' else None}} style="float: right">
                <a href="/login">Login</a>
              </li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
