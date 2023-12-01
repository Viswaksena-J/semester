% place the robot on a random unoccupied position of the map

function [x, y, dx, dy] = initrobot(ranges, clearance) 

dx = 0; % initial speed is 0
dy = 0; % initial speed is 0
found = 0;
while ~found
  x = max(1, rand * 100);
  y = max(1, rand * 100);
  z = sense(x, y, ranges, 100, 0);
  found = (min(z) >= clearance);
end