%
% Main program - particle filter exercise
% Sebastian Thrun and Jesse Levinson
%
clear;
% %%%%%%%%%%%%%%
%
% PARAMETERS
%

ITERATIONS = 300; % how long to run demo for
MAP_NUMBER = 2; % which map to use
MAX_RANGE = 30; % sensor max range
N = 300; % number of particles
MEASUREMENT_NOISE  = 4; % actual noise
MEASUREMENT_NOISE2 = 8; % assumed noise in filter
MOTION_NOISE  = .5; % actual noise
MOTION_NOISE2 = 1; % assumed noise in filter
KIDNAP_PROBABILITY = 0.00; % actual probability of kidnapped robot
KIDNAP_PROBABILITY2 = 0.05; % assumed probability of kidnapped robot
CLEARANCE = 3; % clearance to obstacles
MAX_SPEED = 4; % maximum speed
 img=imread('my1.bmp');


% %%%%%%%%%%%%%%
%
% INITALIZATION OF THE WORLD
%


map = makemap(MAP_NUMBER);
 map=img;
showmap(map);

% compute the expected distances in the map

ranges = freerange(map, MAX_RANGE);


% create the robot

[x, y, dx, dy] = initrobot(ranges, CLEARANCE); % robot

% %%%%%%%%%%%%%%
%
% INITALIZATION OF PARTICLES
%

% generate particles - some might end up in walls, but we dont care

Px  = min(max(rand(1,N) * 100, 1), 100);
Py  = min(max(rand(1,N) * 100, 1), 100);
Pdx = zeros(1,N);
Pdy = zeros(1,N);
Pweight = ones(1,N) / N;


% %%%%%%%%%%%%%%
%
% RUN THE PARTICLE FILTER
%

lms_sum = 0.0;
k=0; in=0;
for i = 1 : ITERATIONS

  % display iteration number and error
  lms = mean(sqrt((Px - x).^2 + (Py - y).^2));
  lms_sum = lms_sum + lms;
  disp(['Iteration: ' num2str(i) ' LMS Error: ' num2str(lms)])
   k=[k,lms];
   in=[in,i];
  % sense
  z = sense(x, y, ranges, MAX_RANGE, MEASUREMENT_NOISE);
  
  % compute particle weights 
  for n = 1 : N
    Pz = sense(Px(n), Py(n), ranges, MAX_RANGE, MEASUREMENT_NOISE);
    Pweight(n) = double(min(Pz) >= CLEARANCE); % Part 1 (collisions with walls)
    err = sum((Pz - z).^2);
   Pweight(n) = Pweight(n) * exp(-0.5 * err / MEASUREMENT_NOISE2^2);
  end
  Pweight = Pweight / sum(Pweight);


  % resample  
  n = max(round(rand * N), 1); % initial particle
  for m = 1 : N;
    leftover = rand * 0.1;  % propose random increment
    while leftover > Pweight(n) % do the search for the next element
      leftover = leftover - Pweight(n);
      n = mod(n, N) + 1;  % increment n
    end % found it!
    Px2(m) = Px(n);
    Py2(m) = Py(n);
    Pdx2(m) = Pdx(n);
    Pdy2(m) = Pdy(n);
  end
  Px = Px2;
  Py = Py2;
  Pdx = Pdx2;
  Pdy = Pdy2;

  % display everything
  clf
  hold on
  showmap(map);
  showrobot(Px, Py);
  showrobot(x, y, z);    
  plot(mean(Px), mean(Py),'bo');
  drawnow

  % motion
  [x, y, dx, dy] = move(x, y, dx, dy, MOTION_NOISE, ranges, MAX_SPEED, CLEARANCE); % robot motion
  if(rand() < KIDNAP_PROBABILITY) 
    [x, y, dx, dy] = initrobot(ranges, CLEARANCE); % robot moves to random new location
  end  
  for n = 1 : N % move particles
    [Px(n), Py(n), Pdx(n), Pdy(n)] = move(Px(n), Py(n), Pdx(n), Pdy(n), ...
					  MOTION_NOISE2, ranges, MAX_SPEED, CLEARANCE);
    if(rand() < KIDNAP_PROBABILITY2) % try a random location
      Px(n)  = min(max(rand() * 100, 1), 100);
      Py(n)  = min(max(rand() * 100, 1), 100);
      Pdx(n) = 0;
      Pdy(n) = 0;
    end
  end
end

disp('........');
disp(['Simulation complete! Average lms error: ' num2str(lms_sum / ITERATIONS)])
