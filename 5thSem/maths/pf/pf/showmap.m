
function h = showmap(map)

%
% Function: showmap
%
% Input: map
%
% Output: none
%
% Draws a map

% draw frame
%   plot([-10 110 110 -10 -10], [-10 -10 110 110 -10], 'w');


% flip map for display only

mapindx=100:-1:1;
mapflipped = map(:,mapindx);

% display

h = imshow((1-map)','InitialMagnification','fit');

% display border


