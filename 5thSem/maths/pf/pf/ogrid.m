%
% Main program - particle filter exercise
% Sebastian Thrun and Jesse Levinson
%

% %%%%%%%%%%%%%%
%
% PARAMETERS
%

ITERATIONS = 10000; % how long to run demo for
MAP_NUMBER = 1; % which map to use
MAX_RANGE = 30; % sensor max range

PROB_PRIOR = 0.4; % prior probability of a cell being occupied
PROB_FREE  = 0.3;
PROB_OCC   = 0.6;
PROB_UNDER = 0.001;

MEASUREMENT_NOISE  = 4; % actual noise
MEASUREMENT_NOISE2 = 8; % assumed noise in filter
MOTION_NOISE  = .5; % actual noise
KIDNAP_PROBABILITY = 0.05; % actual probability of kidnapped robot
CLEARANCE = 3; % clearance to obstacles
MAX_SPEED = 4; % maximum speed


% %%%%%%%%%%%%%%
%
% INITALIZATION OF THE WORLD
%

% make the map

map = makemap(2);

grid = zeros(100,100); % start with empty map
grid(:,:) = 0.0;
logodds = zeros(100, 100);
l0 = log(PROB_PRIOR / (1 - PROB_PRIOR));
locc = log(PROB_OCC / (1 - PROB_OCC));
lfree = log(PROB_FREE / (1 - PROB_FREE));
lunder = log(PROB_UNDER / (1 - PROB_UNDER));

logodds(:,:) = l0;

% grid(:,:) = 1 - 1 / (1 + exp(logodds()));

% compute the expected distances in the map

ranges = freerange(map, MAX_RANGE);


% create the robot

[x, y, dx, dy] = initrobot(ranges, CLEARANCE); % robot


% %%%%%%%%%%%%%%
%
% RUN THE MAPPER
%

for i = 1 : ITERATIONS

  % sense
  z = sense(x, y, ranges, MAX_RANGE, MEASUREMENT_NOISE);

  % update log odds
  xz=[x, x-z(2), x, x+z(4)];
  yz=[y-z(1), y, y+z(3), y];
  x_now = int8(x);
  y_now = int8(y);
  % logodds(x_now-1:x_now+1, y_now-1:y_now+1) = logodds(x_now-1:x_now+1, y_now-1:y_now+1) + lunder - l0;
  for i = 1 : 4
      x_hit = int8(min(max(xz(i), 2), 99));
      y_hit = int8(min(max(yz(i), 2), 99));
      logodds(min(x_now, x_hit):max(x_now, x_hit), y_now) = logodds(min(x_now, x_hit):max(x_now, x_hit), y_now) + lfree - l0;
      logodds(x_now, min(y_hit, y_now):max(y_hit, y_now)) = logodds(x_now, min(y_hit, y_now):max(y_hit, y_now)) + lfree - l0;
      if(z(i) < MAX_RANGE - 0*MEASUREMENT_NOISE)
        logodds(x_hit-1:x_hit+1, y_hit-1:y_hit+1) = logodds(x_hit-1:x_hit+1, y_hit-1:y_hit+1) + locc - l0;
        logodds(x_hit, y_hit) = logodds(x_hit, y_hit) + locc - l0;
      end
  end
  
  % compute grid probabilities from log-odds representation
  for i = 1 : 100 
     for j = 1 : 100
        grid(i,j) = 1 - 1 / (1 + exp(logodds(i, j)));
     end
  end

  % display everything
  clf
  hold on
  showmap(grid);
  showrobot(x, y, z);    
  %plot(mean(Px), mean(Py),'bo');
  drawnow

  % motion
  [x, y, dx, dy] = move(x, y, dx, dy, MOTION_NOISE, ranges, MAX_SPEED, CLEARANCE); % robot motion
  if(rand() < KIDNAP_PROBABILITY) 
    [x, y, dx, dy] = initrobot(ranges, CLEARANCE); % robot moves to random new location
  end  
end

disp('........');
disp(['Simulation complete! Average lms error: ' num2str(0 / ITERATIONS)])
