%% plotting the motion generated by the defined initial guess
function ini_guess_impact = ini_guess_motion(X_0)
global L0 L1 L2 L3 L4 var_array_length

for i = 1:var_array_length  % Examining the impact time and feasibility of the motion (geometrical constraints on the limb motion/ head and hip height with respect to the ground)
    % All cases in which impact can take place with the ground
    if X_0(i,1) > pi || X_0(i,2) < 0 || X_0(i,3) > 0 || X_0(i,3) < -pi || (L0+L1)*sin(X_0(i,1))+L2*sin(X_0(i,1)+X_0(i,2))< 0 ...
            || (L0+L1)*sin(X_0(i,1))+L2*sin(X_0(i,1)+X_0(i,2))+(L3+L4)*sin(X_0(i,1)+X_0(i,2)+X_0(i,3)) < 0
        ini_guess_impact = i-1; %Set imact time as that step (time instant)
        break
    else
        ini_guess_impact = var_array_length; % No impact predicted during the simulation time.
    end
end

for i = 1:ini_guess_impact % Plotting the motion of the generated initial guess
    plot ([0 (L0+L1)*cos(X_0(i,1)) (L0+L1)*cos(X_0(i,1))+L2*cos(X_0(i,1)+X_0(i,2)) (L0+L1)*cos(X_0(i,1))+L2*cos(X_0(i,1)+X_0(i,2))+(L3+L4)*cos(X_0(i,1)+X_0(i,2)+X_0(i,3))],...
        [0 (L0+L1)*sin(X_0(i,1)) (L0+L1)*sin(X_0(i,1))+L2*sin(X_0(i,1)+X_0(i,2)) (L0+L1)*sin(X_0(i,1))+L2*sin(X_0(i,1)+X_0(i,2))+(L3+L4)*sin(X_0(i,1)+X_0(i,2)+X_0(i,3)) ],'k');
    hold on
    axis square
    xlabel('X(m)');
    ylabel('Y(m)');
    axis([-(L0+L1+L2+L3+L4)  (L0+L1+L2+L3+L4)  -(L0+L1+L2+L3+L4)  (L0+L1+L2+L3+L4)],'square')
    figure(gcf)
    drawnow
    hold off
    pause(0.0)
end