
function ranges = freerange(map, crop)

% This function returns the correct measurement for each location in map





% increment x
aux = 1-map;
for i = 1 : 100
  aux = circshift(aux, [0,1]) + 1; % move all values, add 1
  aux(1,:) = 0; % prevent circular shift at border
  aux = aux .* (1-map); % zero our map
end
ranges(1,:,:) = aux;


% increment y
aux = 1-map;
for i = 1 : 100
  aux = circshift(aux, [1,0]) + 1; % move all values, add 1
  aux(:,1) = 0; % prevent circular shift at border
  aux = aux .* (1-map); % zero our map
end
ranges(2,:,:) = aux;


% decrement x
aux = 1-map;
for i = 1 : 100
  aux = circshift(aux, [0,-1]) + 1; % move all values, add 1
  aux(100,:) = 0; % prevent circular shift at border
  aux = aux .* (1-map); % zero our map
end
ranges(3,:,:) = aux;


% decrement y
aux = 1-map;
for i = 1 : 100
  aux = circshift(aux, [-1,0]) + 1; % move all values, add 1
  aux(:,100) = 0; % prevent circular shift at border
  aux = aux .* (1-map); % zero our map
end
ranges(4,:,:) = aux;


ranges = min(ranges, crop); % crop the sensor measurements
