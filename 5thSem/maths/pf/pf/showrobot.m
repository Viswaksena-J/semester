
function showrobot(x, y, z)

%
% Function: showrobot
%
% Input: robot position (or list of positions)
%        Optional: measurement vector z
%
% Output: none
%
% Draws robot and - if available - measurements
%


if exist('z') == 1

  % show robot

  hold on
  scatter(x, y, 100, 'b','filled');

  % show sensor measurements
  xz=[x, x-z(2), x, x+z(4)];
  yz=[y-z(1), y, y+z(3), y];

  plot(xz, yz, 'go');
  for i = 1 : 4
    line([x xz(i)], [y yz(i)]);
  end

else
  % show particles
  plot(x,y,'r.');
end


