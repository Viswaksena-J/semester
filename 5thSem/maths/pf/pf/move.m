
function [xp, yp, dxp, dyp] = move(x, y, dx, dy, noise, ranges, speed, clearance)


%
% Function: move
%
% Input: robot coordinates x, y; velocities dx, dy
%        ranges table (for collision checking)
%        max speed for motion
%        min clearance for collision checking
%
% Output: new coordinates and velocities
%


% modify speed

dxp = max(min(dx + normrnd(0, noise), speed), -speed); % adjust speed with noise
dyp = max(min(dy + normrnd(0, noise), speed), -speed); % adjust speed with noise

% apply motion
xp = min(max(x + dxp, 1), 100);
yp = min(max(y + dyp, 1), 100);

% check for near-collision
zp = sense(xp, yp, ranges, 100, 0);

% react to near-collision
if min(zp) < clearance
  xp = x;
  yp = y;
  dxp = 0;
  dyp = 0;
end
