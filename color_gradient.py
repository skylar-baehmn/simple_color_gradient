## just a simple function for getting a color gradient between two colors
## note: this is by no means an absolute color gradient following color theory, but rather a good estimation
## for website purposes.

def get_color_gradient(rgb1, rgb2, number_of_steps):
    ## number of steps is how many colors we want in the gradient (1 step would be one value halfway between two colors)
    r1 = rgb1[0]
    g1 = rgb1[1]
    b1 = rgb1[2]
    r2 = rgb2[0]
    g2 = rgb2[1]
    b2 = rgb2[2]

    ## to get the correct step positions we will keep track of the percentage each one is on
    rgb1_step_percent = 100 - (100 / (number_of_steps + 1))
    rgb2_step_percent = (100 / (number_of_steps + 1))
    step_change_percent = (100 / (number_of_steps + 1))
    ## because they are now in the form xx% instead of .xx we will convert to decimal
    rgb1_step_percent = (rgb1_step_percent / 100)
    rgb2_step_percent = (rgb2_step_percent / 100)
    step_change_percent = (step_change_percent / 100)
    rgb_gradient_arr = []

    ## now for number of steps, we will get the value of the gradient by doing x% of rgb1 and y% of rgb2
    for i in range(0, number_of_steps):
        rgb1_at_step = [r1 * rgb1_step_percent, g1 * rgb1_step_percent, b1 * rgb1_step_percent]
        rgb2_at_step = [r2 * rgb2_step_percent, g2 * rgb2_step_percent, b2 * rgb2_step_percent]
        rgb_at_step = [rgb1_at_step[0] + rgb2_at_step[0], rgb1_at_step[1] + rgb2_at_step[1], rgb1_at_step[2] + rgb2_at_step[2]]
        rgb_gradient_arr.append(rgb_at_step)

        ## update step numbers
        rgb1_step_percent -= step_change_percent
        rgb2_step_percent += step_change_percent

    return rgb_gradient_arr    

def main():
    ## just a simple thing so it will run on console. No input validation because it almost certainly will only be used
    ## by me
    rgb1_input = input("Enter first rgb value (R G B): ")
    rgb2_input = input("Enter second rgb value (R G B): ")
    steps_input = input("Enter number of steps (how many values on gradient): ")

    ## convert input to usable code
    rgb1_input = rgb1_input.split(' ')
    rgb2_input = rgb2_input.split(' ')
    rgb1 = [int(rgb1_input[0]), int(rgb1_input[1]), int(rgb1_input[2])]
    rgb2 = [int(rgb2_input[0]), int(rgb2_input[1]), int(rgb2_input[2])]
    steps = int(steps_input)

    color_arr = get_color_gradient(rgb1, rgb2, steps)

    print(color_arr)


if __name__ == "__main__":
    main()