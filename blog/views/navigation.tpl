    <style>
    <!--
    -->
    </style>
    <div class="navbar navbar-inverse navbar-fixed-top">
      <div class="navbar-inner">
        <div class="container">
          <button type="button" class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
            <span class="icon-bar"></span>
          </button>
          <a class="brand" href="/">tz</a>
          <div class="nav-collapse collapse">
            <ul class="nav">
              % active = 'class=active'
	      % for path, label in menu:
              % 
              <li {{active if r_path == path else None}}>
                <a href="{{path}}">{{label}}</a>
              </li>
              % end
              <li {{active if r_path == '/login' else None}}>
              % try:
                <div class="dropdown">
                  <button class="btn btn-inverse dropdown-toggle sr-only" type="button" id="dropdownMenu1" data-toggle="dropdown">
                      {{username}}
                    <span class="caret"></span>
                  </button>
                  <ul class="dropdown-menu" role="menu" aria-labelledby="dropdownMenu1">
                    <li role="presentation"><a role="menuitem" tabindex="-1" href="/user/{{username}}">Profile</a></li>
                    <li role="presentation"><a role="menuitem" tabindex="-1" href="/logout">Logout</a></li>
                  </ul>
                </div>
              % except:
                <a href="/login">Login</a>
              % end
              </li>
            </ul>
          </div><!--/.nav-collapse -->
        </div>
      </div>
    </div>
