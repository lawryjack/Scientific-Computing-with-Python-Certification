import copy;
import random;

class Hat:

    def __init__(self, **kwargs):
        self.contents = [];  
        for key, value in kwargs.items():   
            for i in range(value):  
                self.contents.append(key);  
    
    def draw(self, number):
        try:
            balls_selected = random.sample(self.contents, number);
        except:
            balls_selected = copy.deepcopy(self.contents);
        
        for ball in balls_selected:
            self.contents.remove(ball);
        
        return balls_selected;
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments;
    M = 0;

    for i in range(N):
        copyExpectedBalls = copy.deepcopy(expected_balls);
        copyHat = copy.deepcopy(hat); 
        copyBallsDrawn = copyHat.draw(num_balls_drawn);                     #

        array = [];
        for key, value in copyExpectedBalls.items():
            for i in range(value):
                array.append(key);
        copyExpectedBalls = array;

        for ball in copyBallsDrawn:
            if ball in copyExpectedBalls:
                copyExpectedBalls.remove(ball);

        if copyExpectedBalls == []:
            M += 1;

    return M/N;
    