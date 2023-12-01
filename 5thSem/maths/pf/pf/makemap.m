
function map = makemap(m)

%
% Function: makemap
%
% Input: m is the map number. We've included 3 different maps
%        feel free to make your own
%
% Output: map (100 x 100 grid, 1=occupied; 0=free)
%

map = zeros(100,100); % start with empty map

for i = 1 : 100 % make the border
   map(i, 1)  = 1;
   map(i,100) = 1;
   map(1,i)   = 1;
   map(100,i) = 1;   
end

if(m == 1)

    for i = 10 : 75 % map some lines
      map(i, 20)  = 1;
      map(i, 19)  = 1;
      map(i, 18)  = 1;
      map(i, i+10)  = 1;
      map(i+1, i+10)  = 1;
      map(i+2, i+10)  = 1;
   end
   map(10:30, 60:80) = 1; % make a square
   
elseif(m == 2) 
    
   for(i = 0.0 : .01 : 2 * 3.14159265) % make a circle
      r = 36; % circle radius
      map(50 + int8(r * cos(i)), 50 + int8(r * sin(i))) = 1;
   end
   map(43:57, 5:95) = 0; % some holes in the circle
   map(5:95, 43:57) = 0;
   map(45:55, 45:55) = 1; % a square in the center

elseif(m == 3)
   
   map(20:40, 20:40) = 1;
   map(60:80, 20:40) = 1;
   map(20:40, 60:80) = 1;
   map(60:80, 60:80) = 1;
   
elseif(m == 4)
   
   % make your own map here!
   
end