
function z = sense(x, y, ranges, max_range, noise)


%
% Function: sense
%
% Input: robot coordinates x, y
%        ranges table 
%        max sensor range
%        noise level
%
% Output: measurement vector
%

% this is an approximation - it ignores the continuous 
% nature of the robot position


z = ranges(:,int8(round(x)), int8(round(y))); % look up distances to obstacles
z = z + normrnd(0,noise,4,1); % add some noise
z = max(min(z, max_range), 0); % clamp ranges from 0 to max_range