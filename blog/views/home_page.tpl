% include('header.tpl')
    <div class="container">
    % for entry in blogs[::-1]:
      <h3>{{entry[1]}}</h3>
      <p>{{entry[2]}}</p> @{{entry[3]}}
    % end
    </div> <!-- /container -->
% include('footer.tpl')
